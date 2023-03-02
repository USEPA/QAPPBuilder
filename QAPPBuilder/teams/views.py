# views.py (accounts)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301,R0901,E1101,R0912
"""
Team management views.

Available functions:
- Create the form view
- View to edit a team name
- Team Management Form
"""

from datetime import datetime
from io import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView, status, Http404
from rest_framework import permissions
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic import FormView, ListView
from django.test.client import RequestFactory
from accounts.models import User
from teams.forms import TeamManagementForm, Team
from teams.models import TeamMembership
from teams.serializers import TeamSerializer, UserSerializer, \
    TeamMembershipSerializer, TeamMembershipModifySerializer


def is_user_member(user, team=None):
    """
    Check user membership.

    Check if the given user is a member of the given team or if the user is
    a member of any team when team=None.
    """
    if team:
        return TeamMembership.objects.filter(team_id=team.id,
                                             member_id=user.id).exists()
    return TeamMembership.objects.filter(member_id=user.id).exists()


def can_user_edit_team(user, team_id):
    """
    Check if a user can edit a team.

    Check team membership and user super status to
    decide if the given user can modify the given team.
    """
    membership = TeamMembership.objects.filter(team_id=team_id,
                                               member_id=user.id).first()
    return membership.can_edit or user.is_superuser


class TeamListView(LoginRequiredMixin, ListView):
    """
    New class to return a teams list view.

    This will serve as the management view where users can view their teams,
    edit their teams, and create new teams.
    """

    model = Team
    context_object_name = 'teams'
    template_name = 'team_list.html'

    def get_queryset(self):
        """
        Get a list of teams.

        Override the default queryset with the set of teams of
        which the requesting user is member.
        """
        user = self.request.user
        return Team.objects.filter(
            members=user).order_by('name').select_related(
                "created_by", "last_modified_by").prefetch_related(
                    "team_memberships", "team_memberships__member").all()


class TeamCreateView(FormView):
    """Class containing the view to create a new team."""

    form_class = TeamManagementForm
    template = 'team_create.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Display the project create form."""
        form = TeamManagementForm()
        return render(request, self.template, {'form': form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Save the changes to the user form."""
        form = self.form_class(request.POST)
        if form.is_valid():
            team_instance = form.save(commit=False)
            # Team creator.
            team_instance.created_by = request.user
            # When and by whom the project was created.
            date_now = datetime.now()
            team_instance.created_date = date_now
            team_instance.created_by = request.user
            # When and by whom the project was last modified.
            team_instance.last_modified_date = date_now
            team_instance.last_modified_by = request.user
            # Save the project
            team_instance.save()

            # Add a membership for the requesting user.
            membership_instance = TeamMembership()
            membership_instance.added_date = date_now
            membership_instance.member = request.user
            membership_instance.team = team_instance
            membership_instance.is_owner = True
            membership_instance.can_edit = True
            membership_instance.save()

            return HttpResponseRedirect(
                reverse('team_manage', kwargs={'team_id': team_instance.id}))

        return render(request, self.template, locals())


class TeamEditView(FormView):
    """View to edit a team name."""

    template = 'team_edit.html'
    form_class = TeamManagementForm

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Display the project create form."""
        ctx = {}
        ctx['team_id'] = kwargs["team_id"] if kwargs is not None and \
            'team_id' in kwargs else None
        if ctx['team_id'] is not None:
            if can_user_edit_team(request.user, ctx['team_id']):
                ctx['team_data'] = APITeamDetailView.as_view()(
                    request, team_id=ctx['team_id'],
                    format='json').rendered_content
                ctx['team'] = JSONParser().parse(BytesIO(
                    ctx['team_data']))['name']
                return render(request, self.template, ctx)
        return HttpResponseRedirect('/teams/list/')

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Save the changes to the user form."""
        ctx = {}
        ctx['params'] = request.POST
        ctx['team_id'] = kwargs["team_id"] if kwargs is not None and \
            'team_id' in kwargs else None

        if ctx['team_id'] is not None:
            if not can_user_edit_team(request.user, ctx['team_id']):
                return HttpResponseRedirect('/teams/list/')

            # Update the team name.
            ctx['team_obj'] = Team.objects.get(id=ctx['team_id'])
            if ctx['team_obj'] is not None:
                ctx['name'] = ctx['params']['name'] if \
                    'name' in ctx['params'] else None
                ctx['name'] = ctx['name'].strip()
                if ctx['name'] is not None and ctx['name']:
                    ctx['team_obj'].name = ctx['name']
                    ctx['team_obj'].save()
                else:
                    ctx['error_msg'] = "Invalid team name."
            else:
                ctx['error_msg'] = "Invalid team id specified."

            # Retrieve the updated data and render the view.
            get_request = RequestFactory().get('/')
            get_request.user = request.user
            ctx['team_data'] = APITeamDetailView.as_view()(
                get_request, team_id=ctx['team_id'],
                format='json').rendered_content
            ctx['team'] = JSONParser().parse(BytesIO(ctx['team_data']))
            # return render(request, self.template, ctx)
            return HttpResponseRedirect('/teams/list/')

        # We should never get here, so just redirect to the dashboard.
        return HttpResponseRedirect(reverse('dashboard'))


class TeamManagementView(FormView):
    """Class containing methods to manage teams."""

    template = 'team_manage.html'
    form_class = TeamManagementForm

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Display the project create form."""
        ctx = {}
        ctx['team_id'] = kwargs["team_id"] if kwargs is not None and \
            'team_id' in kwargs else None
        if ctx['team_id'] is not None:
            ctx['team_data'] = APITeamDetailView.as_view()(
                request, team_id=ctx['team_id'],
                format='json').rendered_content
            ctx['team'] = JSONParser().parse(BytesIO(ctx['team_data']))
            ctx['nonmembers_data'] = APITeamMembershipListView.as_view()(
                request, team_id=ctx['team_id'], nonmember=1,
                format='json').rendered_content
            ctx['nonmembers'] = JSONParser().parse(
                BytesIO(ctx['nonmembers_data']))

            membership = TeamMembership.objects.filter(
                team_id=ctx['team_id'], member_id=request.user).first()
            ctx['user_can_edit'] = membership.can_edit

            return render(request, self.template, ctx)
        return HttpResponseRedirect('/teams/list/')

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Save the changes to the user form."""
        ctx = {}
        ctx['params'] = request.POST
        ctx['command'] = ctx['params']["command"] if \
            "command" in ctx['params'] else None
        ctx['team_id'] = kwargs["team_id"] if kwargs is not None and \
            'team_id' in kwargs else None
        if not can_user_edit_team(request.user, ctx['team_id']):
            return HttpResponseRedirect('/teams/list/')

        ctx['team_obj'] = Team.objects.filter(id=ctx['team_id']).first()
        if ctx['team_obj'] is not None and ctx['command'] is not None:
            # If the request.user cannot edit the current team, do nothing.
            membership = TeamMembership.objects.filter(
                team_id=ctx['team_id'], member_id=request.user).first()
            ctx['user_can_edit'] = membership.can_edit
            if not membership.can_edit:
                return HttpResponseRedirect('/teams/team/%s/manage' %
                                            ctx['team_id'])

            if ctx['command'] == 'adduser':
                # Add a user membership to the team.
                user_id = int(ctx['params']['user_id']) if \
                    'user_id' in ctx['params'] else None
                if user_id is not None:
                    # Check if the user already has a membership, this can
                    # happen if the user reloads the page.
                    ctx['membership_list'] = TeamMembership.objects.filter(
                        team_id=ctx['team_id'], member_id=user_id).all()
                    no_membership_list = ctx['membership_list'] is \
                        None or not ctx['membership_list']
                    if no_membership_list:
                        # Add a membership.
                        ctx['member_obj'] = User.objects.get(id=user_id)
                        ctx['membership'] = TeamMembership()
                        ctx['membership'].added_date = datetime.now()
                        ctx['membership'].team = ctx['team_obj']
                        ctx['membership'].member = ctx['member_obj']
                        ctx['membership'].can_edit = False
                        ctx['membership'].is_owner = False
                        ctx['membership'].save()
                else:
                    ctx['error_msg'] = "Invalid user id specified."

            elif ctx['command'] == 'deleteuser':
                # Remove a user membership.
                user_id = int(ctx['params']['user_id']) if \
                    'user_id' in ctx['params'] else None
                if user_id is not None:
                    # Add a membership.
                    ctx['membership'] = TeamMembership.objects.get(
                        team_id=ctx['team_id'], member_id=user_id)
                    if ctx['membership'] is not None:
                        ctx['membership'].delete()
                else:
                    ctx['error_msg'] = "Invalid user id specified."

            elif ctx['command'] == 'updatename':
                # Update the team name.
                if ctx['team_obj'] is not None:
                    ctx['name'] = ctx['params']['name'] if \
                        'name' in ctx['params'] else None
                    ctx['name'] = ctx['name'].strip()
                    if ctx['name'] is not None and ctx['name']:
                        ctx['team_obj'].name = ctx['name']
                        ctx['team_obj'].save()
                    else:
                        ctx['error_msg'] = "Invalid team name."
                else:
                    ctx['error_msg'] = "Invalid team id specified."

            elif ctx['command'] == 'canedit':
                # Change this user's can_edit status.
                user_id = int(ctx['params']['user_id']) if \
                    'user_id' in ctx['params'] else None
                ctx['can_edit'] = ctx['params']['can_edit'] if \
                    'can_edit' in ctx['params'] else None
                if user_id is not None and ctx['can_edit'] is not None:
                    # Get the membership object:
                    ctx['membership'] = TeamMembership.objects.get(
                        team_id=ctx['team_id'], member_id=user_id)
                    if ctx['membership'] is not None:
                        ctx['membership'].can_edit = ctx['can_edit']
                        ctx['membership'].save()

            # Retrieve the updated data and render the view.
            get_request = RequestFactory().get('/')
            get_request.user = request.user

            ctx['team_data'] = APITeamDetailView.as_view()(
                get_request, team_id=ctx['team_id'],
                format='json').rendered_content
            ctx['team'] = JSONParser().parse(BytesIO(ctx['team_data']))
            ctx['nonmembers_data'] = APITeamMembershipListView.as_view()(
                get_request,
                team_id=ctx['team_id'],
                nonmember=1,
                format='json').rendered_content
            ctx['nonmembers'] = JSONParser().parse(
                BytesIO(ctx['nonmembers_data']))
            return render(request, self.template, ctx)

        # We should never get here, so just redirect to the dashboard.
        return HttpResponseRedirect(reverse('dashboard'))


#########################
# REST Api Team views
#########################


class APITeamListView(APIView):
    """Get a JSON list of all teams (GET) or create a new team (POST)."""

    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        """Return all teams the current user is a member of."""
        # Get the list of teams to exclude.
        exclude = kwargs.get('exclude', None)
        if exclude is None:
            exclude_json = self.request.query_params.get('exclude', None)
            if exclude_json is not None:
                exclude = JSONParser().parse(BytesIO(exclude_json))

        if exclude is not None:
            teams = (Team.objects.exclude(id__in=exclude).filter(
                members=request.user).order_by('name').select_related(
                    "created_by", "last_modified_by").prefetch_related(
                        "team_memberships", "team_memberships__member").all())
        else:
            teams = (Team.objects.filter(
                members=request.user).order_by('name').select_related(
                    "created_by", "last_modified_by").prefetch_related(
                        "team_memberships", "team_memberships__member").all())

        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """Create a new team."""
        serializer = TeamSerializer(data=request.data,
                                    context={'request': request})
        if serializer.is_valid():
            team = serializer.save()
            # Add a membership for the requesting user.
            membership_instance = TeamMembership()
            membership_instance.added_date = datetime.now()
            membership_instance.member = request.user
            membership_instance.team = team
            membership_instance.is_owner = True
            membership_instance.can_edit = False
            membership_instance.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APITeamDetailView(APIView):
    """Read, Update, Delete for Team objects."""

    permission_classes = (permissions.IsAuthenticated, )

    @classmethod
    def get_object(cls, p_id, user):
        """
        Get team details.

        Retrieve a team and its membership based on the provided user and p_id.
        """
        try:
            team = (Team.objects.select_related(
                "created_by", "last_modified_by").prefetch_related(
                    "team_memberships",
                    "team_memberships__member").get(id=p_id))
            for membership in team.team_memberships.all():
                if user == membership.member:
                    return team, membership
            raise Http404
        except Team.DoesNotExist as team_does_not_exist:
            raise Http404 from team_does_not_exist

    def get(self, request, team_id, *args, **kwargs):
        """Get details for the specified team."""
        (team, _membership) = self.get_object(team_id, request.user)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    def put(self, request, team_id, *args, **kwargs):
        """
        Update an existing team.

        :param request:
        :param team_id:
        :param format:
        :return:
        """
        (team, membership) = self.get_object(team_id, request.user)
        if not membership.can_edit:
            return Response({"detail": "current user cannot edit this team"},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = TeamSerializer(team,
                                    data=request.data,
                                    context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, team_id, *args, **kwargs):
        """
        Delete a team.

        :param team_id:
        :param request:
        :param format:
        :return:
        """
        (team, membership) = self.get_object(team_id, request.user)
        if not membership.can_edit:
            return Response({"detail": "current user cannot delete this team"},
                            status=status.HTTP_400_BAD_REQUEST)

        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class APITeamMembershipListView(APIView):
    """Get a list of team members or users who are not team members."""

    permission_classes = (permissions.IsAuthenticated, )

    @classmethod
    def get_object(cls, p_id, user):
        """Get team memberships for the provided user and p_id."""
        try:
            team = (Team.objects.prefetch_related(
                "team_memberships", "team_memberships__member").get(id=p_id))
            team_memberships = team.team_memberships.all()
            for membership in team_memberships:
                if user == membership.member:
                    return team_memberships
            raise Http404
        except Team.DoesNotExist as team_does_not_exist:
            raise Http404 from team_does_not_exist

    def get(self, request, team_id, *args, **kwargs):
        """Get the membership information for the specified team."""
        # If query param "nonmember" is set, returns users not on this team.
        nonmember = kwargs.get('nonmember', None)
        nonmember = request.query_params.get(
            'nonmember', None) if nonmember is None else nonmember
        if nonmember is not None:
            users = User.objects.exclude(member_memberships__team_id=team_id
                                         ).order_by('last_name').all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        team_memberships = self.get_object(team_id, request.user)
        serializer = TeamMembershipSerializer(team_memberships, many=True)
        return Response(serializer.data)

    def post(self, request, team_id, *args, **kwargs):
        """Add a new membership for a user."""
        # Add the team info to the data.
        request.data["team"] = team_id
        serializer = TeamMembershipModifySerializer(data=request.data)
        if serializer.is_valid():
            # Make sure the membership doesn't already exist.
            existing_membership = TeamMembership.objects.filter(
                team__id=team_id, member__id=request.data["member"]).first()
            if existing_membership is not None:
                return Response("user is already a member of this team",
                                status=status.HTTP_400_BAD_REQUEST)
            membership = serializer.save()
            display_serializer = TeamMembershipSerializer(instance=membership)
            return Response(display_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APITeamMembershipDetailView(APIView):
    """Get a list of team members or users who are not team members."""

    permission_classes = (permissions.IsAuthenticated, )

    @classmethod
    def get_object(cls, membership_id, user):
        """
        Get team membership details.

        Get current membership information for the
        provided user and membership_id.
        """
        try:
            current_membership = (TeamMembership.objects.select_related(
                "member", "team").get(id=membership_id))
            # Make sure this user can view this team information.
            for membership in current_membership.team.team_memberships.all():
                if user == membership.member:
                    return current_membership, membership.can_edit
            raise Http404
        except Team.DoesNotExist as team_does_not_exist:
            raise Http404 from team_does_not_exist

    def get(self, request, _team_id, membership_id, *args, **kwargs):
        """Get details for the specified team."""
        (membership,
         _current_user_can_edit) = self.get_object(membership_id, request.user)
        serializer = TeamMembershipSerializer(instance=membership)
        return Response(serializer.data)

    def put(self, request, team_id, membership_id, *args, **kwargs):
        """
        Update an existing team.

        :param membership_id:
        :param request:
        :param team_id:
        :param format:
        :return:
        """
        (membership,
         current_user_can_edit) = self.get_object(membership_id, request.user)
        if not current_user_can_edit:
            return Response({"detail": "calling user cannot edit this team"},
                            status=status.HTTP_400_BAD_REQUEST)

        request.data["team"] = team_id
        request.data["member"] = membership.member.id
        serializer = TeamMembershipModifySerializer(membership,
                                                    data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, _team_id, membership_id, *args, **kwargs):
        """Delete the specified team membership."""
        (membership,
         current_user_can_edit) = self.get_object(membership_id, request.user)
        if not current_user_can_edit:
            return Response({"detail": "calling user cannot edit this team"},
                            status=status.HTTP_400_BAD_REQUEST)
        membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
