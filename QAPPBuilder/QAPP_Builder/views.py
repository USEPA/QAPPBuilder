# views.py (QAPP_Builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301,E1101,R0901,W0613,W0622,C0411


"""Definition of views."""

from datetime import datetime
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, \
    TemplateView, UpdateView, DeleteView
from accounts.models import User
from constants.qar5 import SECTION_A_INFO, SECTION_D_INFO, SECTION_E_INFO, \
    SECTION_F_INFO, SECTION_C_INFO
from constants.qar5_sectionb import SECTION_B_INFO
from QAPP_Builder.forms import QappForm, QappApprovalForm, QappLeadForm, \
    QappApprovalSignatureForm, SectionAForm, SectionBForm, \
    SectionDForm, RevisionForm, ReferencesForm, SectionCForm
from QAPP_Builder.models import Qapp, QappApproval, QappLead, \
    QappApprovalSignature, SectionA, SectionB, SectionC, SectionD, \
    QappSharingTeamMap, Revision, References
from teams.models import Team, TeamMembership


@login_required
@staff_member_required
def web_dev_tools(request, *args, **kwargs):
    """
    Go to the web developer page with custom admin functionality.

    - Includes various custom admin functionality.
    - Includes button to remove extra new line characters/spaces from QAPP data
    """
    return render(request, 'web_dev.html', {})


@login_required
@staff_member_required
def clean_qapps(request, *args, **kwargs):
    """
    Clean QAPP Data.

    - Remove extra new line characters and spaces.
    - Convert QA_Category to the proper value.
    """
    sections_a = SectionA.objects.all()
    for sect in sections_a:
        # Clean Section A
        a3_clean = sect.a3.replace('\r\n', ' ').replace('    ', ' ')
        a9_clean = sect.a9.replace('\r\n', ' ').replace('    ', ' ')
        a9_clean = a9_clean.replace('QA QA', 'QA')
        if 'B' in sect.qapp.qa_category:
            a9_clean = a9_clean.replace('QA Category A', sect.qapp.qa_category)
        else:
            a9_clean = a9_clean.replace('QA Category B', sect.qapp.qa_category)
        sect.a3 = a3_clean
        sect.a9 = a9_clean
        sect.save()
    return render(request, 'web_dev.html', {})


def contact(request):
    """Render the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'main/contact.html',
        {
            'title': 'Contact',
            'year': datetime.now().year,
        }
    )


def get_qapp_all():
    """Get all QAPP data regardless of user or team."""
    return Qapp.objects.all()


class QappIndex(LoginRequiredMixin, TemplateView):
    """Class to return the first page of the Existing Data flow."""

    template_name = 'qapp_index.html'

    def get_context_data(self, **kwargs):
        """
        Override default method to send data to the template.

        Specifically, want to send a list of users and teams to select from.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['teams'] = Team.objects.all()
        return context


class QappList(LoginRequiredMixin, ListView):
    """Class for listing this user's (or all if admin) QAPP objects."""

    model = Qapp
    template_name = 'qapp_list.html'
    context_object_name = 'qapp_list'

    def get_context_data(self, **kwargs):
        """
        Override the default method to send data to the template.

        Specifically, include the user or team information
        for this list of data.
        """
        context = super().get_context_data(**kwargs)
        path = self.request.path.split('/')
        p_id = path[len(path) - 1]
        p_type = path[len(path) - 2]
        if p_type == 'user':
            context['p_user'] = User.objects.get(id=p_id)
        elif p_type == 'team':
            context['team'] = Team.objects.get(id=p_id)
        return context

    def get_queryset(self):
        """Get a list of QAPP objects based on the provided user or team ID."""
        path = self.request.path.split('/')
        p_id = path[len(path) - 1]
        p_type = path[len(path) - 2]
        if p_type == 'user':
            return get_qar5_for_user(p_id)
        if p_type == 'team':
            return get_qar5_for_team(p_id)
        return get_qapp_all()


def check_can_edit(qapp, user):
    """
    Check if the provided user can edit the provided qapp.

    All of the user's member teams are checked as well as the user's
    super user status or qapp ownership status.
    """
    # Check if any of the user's teams have edit privilege:
    user_teams = TeamMembership.objects.filter(
        member=user).values_list('team', flat=True)

    for team in user_teams:
        data_team_map = QappSharingTeamMap.objects.filter(
            qapp=qapp, team=team).first()
        if data_team_map and data_team_map.can_edit:
            return True

    # Check if the user is super or owns the qapp:
    return user.is_superuser or qapp.prepared_by == user


class QappEdit(LoginRequiredMixin, UpdateView):
    """View for editing the details of an existing Qapp instance."""

    model = Qapp
    form_class = QappForm
    template_name = 'qapp_edit.html'

    def get(self, request, *args, **kwargs):
        """
        GET QAPP Edit page.

        Override default get request so we can verify the user has
        edit privileges, either through super status or team membership.
        """
        pkey = kwargs.get('pk')
        qapp = Qapp.objects.filter(id=pkey).first()
        if check_can_edit(qapp, request.user):
            # We need to make sure we return a QappApproval form for editing:
            qapp_approval = QappApproval.objects.filter(qapp_id=pkey).first()
            approval_form = QappApprovalForm(instance=qapp_approval)
            return render(request, self.template_name,
                          {'object': qapp, 'form': QappForm(instance=qapp),
                           'approval_form': approval_form})

        reason = 'You cannot edit this QAPP.'
        return HttpResponseRedirect('/detail/%s' % pkey, 401, reason)

    def form_valid(self, form, *args, **kwargs):
        """Qapp Edit Form validation and redirect."""
        # Verify the current user has permissions to modify this QAPP:
        obj = form.save(commit=False)
        if not check_can_edit(obj, self.request.user):
            reason = 'You cannot edit this QAPP.'
            return HttpResponseRedirect(
                '/detail/%s' % obj.id, 401, reason)

        obj.save()
        # Prepare and insert teams data.
        if form.cleaned_data['teams']:
            form_teams = form.cleaned_data['teams']

            # Remove any team maps that have been deselected:
            remove_teams = QappSharingTeamMap.objects.filter(
                qapp=obj).exclude(team__in=form_teams)

            for team in remove_teams:
                team.delete()

            # Insert or update selected team maps:
            for team in form_teams:
                data_team_map = QappSharingTeamMap.objects.filter(
                    qapp=obj, team=team).first()
                # Create new team map if not exists:
                if not data_team_map:
                    data_team_map = QappSharingTeamMap()
                    data_team_map.team = team
                    data_team_map.qapp = obj
                # Update (or set) the can_edit field:
                data_team_map.can_edit = form.cleaned_data['can_edit']
                data_team_map.save()
        # Return back to the details page:
        return HttpResponseRedirect('/detail/' + str(obj.id))


class QappCreate(LoginRequiredMixin, CreateView):
    """Class for creating new QAPPs (Quality Assurance Project Plans)."""

    model = Qapp
    template_name = 'qapp_create.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Return a view with an empty form for creating a new QAPP."""
        return render(
            request, 'qapp_create.html',
            {'form': QappForm(user=request.user),
             'project_lead_class': QappLeadForm})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Process the post request with a new QAPP form filled out."""
        form = QappForm(request.POST, user=request.user)
        if form.is_valid():
            obj = form.save(commit=False)
            # Assign current user as the prepared_by
            obj.prepared_by = request.user
            obj.save()
            # Prepare and insert teams data.
            if form.cleaned_data['teams']:
                for team in form.cleaned_data['teams']:
                    data_team_map = QappSharingTeamMap()
                    data_team_map.can_edit = form.cleaned_data['can_edit']
                    data_team_map.team = team
                    data_team_map.qapp = obj
                    data_team_map.save()

            return HttpResponseRedirect(
                '/approval/create?qapp_id=%d' % obj.id)

        return render(request, 'qapp_create.html', {'form': form})


class QappDetail(LoginRequiredMixin, DetailView):
    """Class for viewing an existing (newly created) QAPP."""

    model = Qapp
    template_name = 'qapp_detail.html'

    def get_context_data(self, **kwargs):
        """
        Get details for the given QAPP object.

        Verify all data is availablke and check if the
        requesting user has edit permissions.
        """
        context = super().get_context_data(**kwargs)
        context['project_leads_list'] = QappLead.objects.filter(
            qapp=context['object'])
        context['project_approval'] = QappApproval.objects.get(
            qapp=context['object'])
        context['project_approval_signatures'] = \
            QappApprovalSignature.objects.filter(
                qapp_approval=context['project_approval'])
        context['SECTION_A_INFO'] = SECTION_A_INFO
        if not check_can_edit(context['object'], self.request.user):
            context['edit_message'] = \
                'You cannot edit this QAPP.'
        return context


class ProjectLeadCreate(LoginRequiredMixin, CreateView):
    """Class for creating new QAPP Project Lead."""

    model = QappLead
    template_name = 'SectionA/project_lead_create.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Return a view with an empty form for creating a new Project Lead."""
        qapp_id = request.GET.get('qapp_id', 0)
        qapp = Qapp.objects.get(id=qapp_id)

        if check_can_edit(qapp, request.user):
            form = QappLeadForm({'qapp': qapp})
            ctx = {'form': form, 'qapp_id': qapp_id}
            return render(request, self.template_name, ctx)

        reason = 'You cannot edit this QAPP.'
        return HttpResponseRedirect('/detail/%s' % qapp_id, 401, reason)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Process the post request with a new Project Lead form filled out."""
        form = QappLeadForm(request.POST)
        qapp_id = request.POST.get('qapp', None)
        qapp = Qapp.objects.get(id=qapp_id)

        if check_can_edit(qapp, request.user):
            if form.is_valid():
                form.save(commit=True)
                return HttpResponseRedirect(
                    '/detail/%s' % qapp_id)
            ctx = {'form': form, 'qapp_id': qapp_id}
            return render(request, self.template_name, ctx)

        reason = 'You cannot edit this QAPP.'
        return HttpResponseRedirect('/detail/%s' % qapp_id, 401, reason)


class ProjectLeadDelete(LoginRequiredMixin, DeleteView):
    """Class view for deleting approval signatures."""

    model = QappLead
    template_name = 'SectionA/confirm_delete.html'

    def get_success_url(self):
        """Return the user to the detail page on successful Delete."""
        return '/detail/%s' % self.object.qapp.id

    def dispatch(self, *args, **kwargs):
        """Ensure the user has permissions before deleting project leads."""
        pkey = kwargs.get('pk')
        instance = QappLead.objects.filter(id=pkey).first()
        if instance:
            user = self.request.user
            if check_can_edit(instance.qapp, user) or user.is_superuser:
                return super().dispatch(*args, **kwargs)
        return HttpResponseRedirect(self.get_success_url)


class ProjectLeadEdit(LoginRequiredMixin, UpdateView):
    """Class view for editing project leads."""

    model = QappLead
    form_class = QappLeadForm
    template_name = 'SectionA/project_lead_create.html'

    def get(self, request, *args, **kwargs):
        """
        GET Project Lead Edit page.

        Override default get request so we can verify the user has
        edit privileges, either through super status or team membership.
        """
        pkey = kwargs.get('pk')
        obj = self.model.objects.filter(id=pkey).first()
        if check_can_edit(obj.qapp, request.user):
            return render(request, self.template_name,
                          {'object': obj,
                           'form': self.form_class(instance=obj),
                           'qapp_id': obj.qapp.id})

        reason = 'You cannot edit this data.'
        return HttpResponseRedirect(
            '/detail/%s' % obj.qapp.id, 401, reason)

    def post(self, request, *args, **kwargs):
        """Process the post request with a modified Existing Data form."""
        pkey = kwargs.get('pk')
        instance = self.model.objects.filter(id=pkey).first()
        qapp = instance.qapp
        if check_can_edit(qapp, request.user):
            form = self.form_class(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/detail/%s' % qapp.id)

            return render(request, self.template_name, {'form': form})

        reason = 'You cannot edit this data.'
        return HttpResponseRedirect('/detail/%s' % qapp.id, 401, reason)


class ProjectApprovalCreate(LoginRequiredMixin, CreateView):
    """
    Create the base approval page with no signatures.

    Approval signatures will be added after the title and number.
    """

    template_name = 'SectionA/qapp_approval_create.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Return a view with an empty form for creating a new QAPP."""
        qapp_id = request.GET.get('qapp_id', 0)
        qapp = Qapp.objects.get(id=qapp_id)

        if check_can_edit(qapp, request.user):
            form = QappApprovalForm({'qapp': qapp})
            ctx = {'form': form, 'qapp_id': qapp_id}
            return render(request, self.template_name, ctx)

        reason = 'You cannot edit this QAPP.'
        return HttpResponseRedirect('/detail/%s' % qapp_id, 401, reason)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Process the post request with a new Project Lead form filled out."""
        form = QappApprovalForm(request.POST)
        qapp_id = form.data.get('qapp', '')
        qapp = Qapp.objects.get(id=qapp_id)

        if check_can_edit(qapp, request.user):
            if form.is_valid():
                form.save(commit=True)
                return HttpResponseRedirect('/detail/%s' % qapp_id)

            ctx = {'form': form, 'qapp_id': qapp_id}
            return render(request, self.template_name, ctx)

        reason = 'You cannot edit this QAPP.'
        return HttpResponseRedirect('/detail/%s' % qapp_id, 401, reason)


class ProjectApprovalEdit(LoginRequiredMixin, UpdateView):
    """View for editing the details of an existing Qapp Approval page."""

    model = QappApproval
    form_class = QappApprovalForm
    template_name = 'SectionA/qapp_approval_edit.html'

    def get(self, request, *args, **kwargs):
        """
        GET Project Approval Edit page.

        Override default get request so we can verify the user has
        edit privileges, either through super status or team membership.
        """
        pkey = kwargs.get('pk')
        qapp = Qapp.objects.filter(id=pkey).first()
        if check_can_edit(qapp, request.user):
            # We need to make sure we return a QappApproval form for editing:
            qapp_approval = QappApproval.objects.filter(qapp_id=pkey).first()
            return render(request, self.template_name,
                          {'object': qapp_approval, 'qapp_id': pkey,
                           'form': QappApprovalForm(instance=qapp_approval)})

        reason = 'You cannot edit this QAPP.'
        return HttpResponseRedirect('/detail/%s' % pkey, 401, reason)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Save the changes to the form."""
        pkey = kwargs.get('pk')
        instance = QappApproval.objects.filter(qapp_id=pkey).first()
        if check_can_edit(instance.qapp, request.user):
            form = QappApprovalForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/detail/%s' % pkey)
            return render(request, self.template_name,
                          {'qapp_id': pkey, 'form': form})

        reason = 'You cannot edit this QAPP.'
        return HttpResponseRedirect('/detail/%s' % pkey, 401, reason)


class ProjectApprovalSignatureCreate(LoginRequiredMixin, CreateView):
    """Class for creating new QAPP Project Approval Signatures."""

    model = QappApprovalSignature
    template_name = 'SectionA/project_approval_signature_create.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """
        GET Project Approval Signature Create page.

        Return a view with an empty form for creating a new Approval
        Signature.
        """
        qapp_id = request.GET.get('qapp_id', 0)
        qapp = Qapp.objects.get(id=qapp_id)
        if check_can_edit(qapp, request.user):
            qapp_approval = QappApproval.objects.get(qapp=qapp)
            form = QappApprovalSignatureForm(
                {'qapp': qapp, 'qapp_approval': qapp_approval})
            ctx = {'form': form, 'qapp_id': qapp_id}
            return render(request, self.template_name, ctx)

        reason = 'You cannot edit this QAPP.'
        return HttpResponseRedirect('/detail/%s' % qapp_id, 401, reason)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Process the post request with a new Project Lead form filled out."""
        form = QappApprovalSignatureForm(request.POST)
        approval_id = request.POST.get('qapp_approval', None)
        approval = QappApproval.objects.get(id=approval_id)
        qapp_id = approval.qapp.id

        if check_can_edit(approval.qapp, request.user):
            if form.is_valid():
                form.save(commit=True)
                return HttpResponseRedirect(
                    '/detail/%s' % qapp_id)
            ctx = {'form': form, 'qapp_id': qapp_id}
            return render(request, self.template_name, ctx)

        reason = 'You cannot edit this QAPP.'
        return HttpResponseRedirect('/detail/%s' % qapp_id, 401, reason)


class ProjectApprovalSignatureDelete(LoginRequiredMixin, DeleteView):
    """Class view for deleting approval signatures."""

    model = QappApprovalSignature
    template_name = 'SectionA/confirm_delete.html'

    def get_success_url(self):
        """Return the user to the detail page on successful Delete."""
        return '/detail/%s' % self.object.qapp_approval.qapp.id

    def dispatch(self, *args, **kwargs):
        """Ensure the user has permissions before deleting signatures."""
        pkey = kwargs.get('pk')
        instance = QappApprovalSignature.objects.filter(id=pkey).first()
        if instance:
            qapp = instance.qapp_approval.qapp
            user = self.request.user
            if check_can_edit(qapp, user) or user.is_superuser:
                return super().dispatch(*args, **kwargs)
        return HttpResponseRedirect(self.get_success_url)


class ProjectApprovalSignatureEdit(LoginRequiredMixin, UpdateView):
    """Class view for editing approval signatures."""

    model = QappApprovalSignature
    form_class = QappApprovalSignatureForm
    template_name = 'SectionA/project_approval_signature_create.html'

    def get(self, request, *args, **kwargs):
        """
        Override default GET request.

        Verify the user has edit privileges, either through super
        status or team membership.
        """
        pkey = kwargs.get('pk')
        obj = self.model.objects.filter(id=pkey).first()
        if check_can_edit(obj.qapp_approval.qapp, request.user):
            return render(request, self.template_name,
                          {'object': obj,
                           'form': self.form_class(instance=obj),
                           'qapp_id': obj.qapp_approval.qapp.id})

        reason = 'You cannot edit this data.'
        return HttpResponseRedirect(
            '/detail/%s' % obj.qapp_approval.qapp.id, 401, reason)

    def post(self, request, *args, **kwargs):
        """Process the post request with a modified Existing Data form."""
        pkey = kwargs.get('pk')
        instance = self.model.objects.filter(id=pkey).first()
        qapp = instance.qapp_approval.qapp
        if check_can_edit(qapp, request.user):
            form = self.form_class(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/detail/%s' % qapp.id)

            return render(request, self.template_name, {'form': form})

        reason = 'You cannot edit this data.'
        return HttpResponseRedirect('/detail/%s' % qapp.id, 401, reason)


class SectionAView(LoginRequiredMixin, TemplateView):
    """Class for processing QAPP Section A (A.3 and later) information."""

    template_name = 'SectionA/index.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Return the index page for QAPP Section A (A.3 and later)."""
        assert isinstance(request, HttpRequest)
        qapp_id = request.GET.get('qapp_id', None)
        qapp = Qapp.objects.get(id=qapp_id)
        existing_section_a = SectionA.objects.filter(qapp=qapp).first()

        if existing_section_a:
            form = SectionAForm(instance=existing_section_a)

        else:
            form = SectionAForm({'qapp': qapp,
                                 'a3': SECTION_A_INFO['a3'],
                                 'a9': SECTION_A_INFO['a9'].replace(
                                     '__category__', qapp.qa_category)})

        edit_message = ''
        if not check_can_edit(qapp, request.user):
            edit_message = 'You cannot edit this QAPP.'

        return render(request, self.template_name,
                      {'title': 'QAPP Section A', 'qapp_id': qapp_id,
                       'SECTION_A_INFO': SECTION_A_INFO, 'form': form,
                       'edit_message': edit_message})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Process the post request with a SectionA form filled out."""
        ctx = {'qapp_id': request.GET.get('qapp_id', None),
               'SECTION_A_INFO': SECTION_A_INFO, 'title': 'QAPP Section A'}

        qapp = Qapp.objects.get(id=ctx['qapp_id'])
        if not check_can_edit(qapp, request.user):
            reason = 'You cannot edit this QAPP.'
            return HttpResponseRedirect(
                '/SectionA?qapp_id=%s' % qapp.id, 401, reason)

        existing_section_a = SectionA.objects.filter(qapp=qapp).first()

        # Update if existing, otherwise insert new:
        if existing_section_a:
            ctx['form'] = SectionAForm(instance=existing_section_a,
                                       data=request.POST)
        else:
            ctx['form'] = SectionAForm(request.POST)

        if ctx['form'].is_valid():
            ctx['obj'] = ctx['form'].save(commit=True)
            ctx['save_success'] = 'Successfully Saved Changes!'
        else:
            return self.get(request, ctx)

        return render(request, self.template_name, ctx)


class SectionBView(LoginRequiredMixin, TemplateView):
    """Class for processing QAPP Section B information."""

    template_name = 'SectionB/index.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Return the index page for QAPP Section B."""
        assert isinstance(request, HttpRequest)
        qapp_id = request.GET.get('qapp_id', None)
        qapp = Qapp.objects.get(id=qapp_id)
        sectiona = SectionA.objects.filter(qapp_id=qapp_id).first()

        # TODO: Need to figure out the proper way to handle this...
        # if not sectiona:
        #     reason = 'Select a Section B Type and click "Save Changes" ' + \
        #         'before moving onto the next page!'
        #     return HttpResponseRedirect(
        #         '/SectionA?qapp_id=%s' % qapp_id, 302, reason)

        selected_sectionb_types = sectiona.sectionb_type.all()

        edit_message = ''
        if not check_can_edit(qapp, request.user):
            edit_message = 'You cannot edit this QAPP.'

        if not sectiona or not selected_sectionb_types:
            form = SectionAForm({'qapp': qapp,
                                 'a3': SECTION_A_INFO['a3'],
                                 'a9': SECTION_A_INFO['a9']})
            error_message = 'Please select one or more Section B Types ' + \
                'from the list before moving onto the next page, Section B.'
            return render(request, 'SectionA/index.html',
                          {'title': 'QAPP Section A', 'qapp_id': qapp_id,
                           'SECTION_A_INFO': SECTION_A_INFO, 'form': form,
                           'error_message': error_message,
                           'edit_message': edit_message})

        sectionb_type_id = request.GET.get('sectionb_type', None)
        if not sectionb_type_id:
            sectionb_type = selected_sectionb_types[0]
        else:
            sectionb_type = selected_sectionb_types.filter(
                id=int(sectionb_type_id)).first()

        existing_section_b = SectionB.objects.filter(
            qapp=qapp, sectionb_type=sectionb_type).first()

        if existing_section_b:
            form = SectionBForm(
                instance=existing_section_b,
                section_b_info=SECTION_B_INFO[
                    existing_section_b.sectionb_type.name])

        else:
            # Start with whatever the first sectionb_type is:
            form = SectionBForm(
                {'qapp': qapp, 'sectionb_type': sectionb_type},
                section_b_info=SECTION_B_INFO[sectionb_type.name])

        return render(request, self.template_name,
                      {'title': 'QAPP Section B', 'qapp_id': qapp_id,
                       'SECTION_B_INFO': SECTION_B_INFO[sectionb_type.name],
                       'form': form, 'sectionb_type': sectionb_type,
                       'selected_sectionb_types': selected_sectionb_types,
                       'edit_message': edit_message})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Process the post request with a SectionB form filled out."""
        ctx = {'qapp_id': request.GET.get('qapp_id', None),
               'SECTION_B_INFO': SECTION_B_INFO, 'title': 'QAPP Section B'}

        qapp = Qapp.objects.get(id=ctx['qapp_id'])
        if not check_can_edit(qapp, request.user):
            reason = 'You cannot edit this QAPP.'
            return HttpResponseRedirect(
                '/SectionB?qapp_id=%s' % qapp.id, 401, reason)

        sectionb_type_id = request.POST.get('sectionb_type')
        ctx['sectionb_type'] = qapp.sectiona.sectionb_type.filter(
            id=sectionb_type_id).first()

        existing_section_b = SectionB.objects.filter(
            qapp=qapp, sectionb_type=ctx['sectionb_type']).first()

        ctx['selected_sectionb_types'] = qapp.sectiona.sectionb_type.all()

        # Update if existing, otherwise insert new:
        if existing_section_b:
            ctx['form'] = SectionBForm(
                instance=existing_section_b, data=request.POST,
                section_b_info=SECTION_B_INFO[ctx['sectionb_type'].name])
        else:
            ctx['form'] = SectionBForm(
                request.POST,
                section_b_info=SECTION_B_INFO[ctx['sectionb_type'].name])

        if ctx['form'].is_valid():
            ctx['obj'] = ctx['form'].save(commit=True)
            ctx['save_success'] = 'Successfully Saved Changes!'

        return render(request, self.template_name, ctx)


class SectionCView(LoginRequiredMixin, TemplateView):
    """Class for processing QAPP Section C information."""

    template_name = 'SectionC/index.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Return the index page for QAPP Section C."""
        assert isinstance(request, HttpRequest)
        qapp_id = request.GET.get('qapp_id', None)
        qapp = Qapp.objects.get(id=qapp_id)
        existing_section_c = SectionC.objects.filter(qapp=qapp).first()

        if existing_section_c:
            form = SectionCForm(instance=existing_section_c)

        else:
            form = SectionCForm({'qapp': qapp,
                                 'c1': SECTION_C_INFO[0].replace(
                                     '__category__', qapp.qa_category),
                                 'c2': SECTION_C_INFO[1]})

        edit_message = ''
        if not check_can_edit(qapp, request.user):
            edit_message = 'You cannot edit this QAPP.'

        return render(request, self.template_name,
                      {'title': 'QAPP Section C', 'qapp_id': qapp_id,
                       'form': form, 'edit_message': edit_message})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Process the post request with a SectionC form filled out."""
        ctx = {'qapp_id': request.GET.get('qapp_id', None),
               'SECTION_C_INFO': SECTION_C_INFO, 'title': 'QAPP Section C'}

        qapp = Qapp.objects.get(id=ctx['qapp_id'])
        if not check_can_edit(qapp, request.user):
            reason = 'You cannot edit this QAPP.'
            return HttpResponseRedirect(
                '/SectionC?qapp_id=%s' % qapp.id, 401, reason)

        existing_section_c = SectionC.objects.filter(qapp=qapp).first()

        # Update if existing, otherwise insert new:
        if existing_section_c:
            ctx['form'] = SectionCForm(instance=existing_section_c,
                                       data=request.POST)
        else:
            ctx['form'] = SectionCForm(request.POST)

        if ctx['form'].is_valid():
            ctx['obj'] = ctx['form'].save(commit=True)
            ctx['save_success'] = 'Successfully Saved Changes!'

        return render(request, self.template_name, ctx)


class SectionDView(LoginRequiredMixin, TemplateView):
    """Class for processing QAPP Section D information."""

    template_name = 'SectionD/index.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Return the index page for QAPP Section D."""
        assert isinstance(request, HttpRequest)
        qapp_id = request.GET.get('qapp_id', None)
        qapp = Qapp.objects.get(id=qapp_id)
        edit_message = ''
        if not check_can_edit(qapp, request.user):
            edit_message = 'You cannot edit this QAPP.'
        existing_section_d = SectionD.objects.filter(qapp=qapp).first()

        if existing_section_d:
            form = SectionDForm(instance=existing_section_d)

        else:
            form = SectionDForm({'qapp': qapp})

        return render(request, self.template_name,
                      {'title': 'QAPP Section D', 'qapp_id': qapp_id,
                       'SECTION_D_INFO': SECTION_D_INFO,
                       'form': form, 'edit_message': edit_message})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Process the post request with a SectionD form filled out."""
        ctx = {'qapp_id': request.GET.get('qapp_id', None),
               'SECTION_D_INFO': SECTION_D_INFO, 'title': 'QAPP Section D'}

        qapp = Qapp.objects.get(id=ctx['qapp_id'])
        if not check_can_edit(qapp, request.user):
            reason = 'You cannot edit this QAPP.'
            return HttpResponseRedirect(
                '/SectionD?qapp_id=%s' % qapp.id, 401, reason)

        existing_section_d = SectionD.objects.filter(qapp=qapp).first()

        # Update if existing, otherwise insert new:
        if existing_section_d:
            ctx['form'] = SectionDForm(instance=existing_section_d,
                                       data=request.POST)
        else:
            ctx['form'] = SectionDForm(request.POST)

        if ctx['form'].is_valid():
            ctx['obj'] = ctx['form'].save(commit=True)
            ctx['save_success'] = 'Successfully Saved Changes!'

        return render(request, self.template_name, ctx)


class SectionEView(LoginRequiredMixin, TemplateView):
    """Class for processing QAPP Section E information."""

    template_name = 'SectionE/index.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Return the index page for QAPP Section E."""
        assert isinstance(request, HttpRequest)
        qapp_id = request.GET.get('qapp_id', None)
        qapp = Qapp.objects.get(id=qapp_id)
        edit_message = ''
        if not check_can_edit(qapp, request.user):
            edit_message = 'You cannot edit this QAPP.'
        existing_references = References.objects.filter(qapp=qapp).first()

        # Update if existing, otherwise insert new:
        if existing_references:
            form = ReferencesForm(instance=existing_references)
        else:
            form = ReferencesForm({'qapp': qapp})

        return render(request, self.template_name,
                      {'title': 'QAPP Section E', 'qapp_id': qapp_id,
                       'SECTION_E_INFO': SECTION_E_INFO, 'form': form,
                       'edit_message': edit_message})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Process the post request with a SectionE form filled out."""
        ctx = {'qapp_id': request.GET.get('qapp_id', None),
               'SECTION_E_INFO': SECTION_E_INFO, 'title': 'QAPP Section E'}

        qapp = Qapp.objects.get(id=ctx['qapp_id'])
        if not check_can_edit(qapp, request.user):
            reason = 'You cannot edit this QAPP.'
            return HttpResponseRedirect(
                '/SectionE?qapp_id=%s' % qapp.id, 401, reason)

        existing_references = References.objects.filter(qapp=qapp).first()

        # Update if existing, otherwise insert new:
        if existing_references:
            ctx['form'] = ReferencesForm(instance=existing_references,
                                         data=request.POST)
        else:
            ctx['form'] = ReferencesForm(request.POST)

        if ctx['form'].is_valid():
            ctx['obj'] = ctx['form'].save(commit=True)
            ctx['save_success'] = 'Successfully Saved Changes!'

        return render(request, self.template_name, ctx)


class SectionFView(LoginRequiredMixin, TemplateView):
    """Class for processing QAPP Section F information, REVISIONS."""

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Return the index page for QAPP Section F."""
        assert isinstance(request, HttpRequest)
        qapp_id = request.GET.get('qapp_id', None)
        qapp = Qapp.objects.get(id=qapp_id)
        edit_message = ''
        if not check_can_edit(qapp, request.user):
            edit_message = 'You cannot edit this QAPP.'
        revisions = Revision.objects.filter(qapp_id=qapp_id)
        return render(request, 'SectionF/index.html',
                      {'title': 'QAPP Section F', 'qapp_id': qapp_id,
                       'SECTION_F_INFO': SECTION_F_INFO,
                       'revisions': revisions, 'edit_message': edit_message})


class RevisionCreate(LoginRequiredMixin, CreateView):
    """Class for creating new Revisions of a given QAPP."""

    template_name = 'SectionF/revision_create.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """Return a view with an empty form for creating a new QAPP."""
        qapp_id = request.GET.get('qapp_id', 0)
        qapp = Qapp.objects.get(id=qapp_id)
        form = RevisionForm({'qapp': qapp})
        ctx = {'form': form, 'qapp_id': qapp_id}

        return render(request, self.template_name, ctx)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        """Process the post request with a new Project Lead form filled out."""
        form = RevisionForm(request.POST)
        qapp_id = form.data.get('qapp', '')
        qapp = Qapp.objects.filter(id=qapp_id).first()
        if not check_can_edit(qapp, request.user):
            reason = 'You cannot edit this QAPP.'
            return HttpResponseRedirect(
                '/revisions?qapp_id=%s' % qapp.id, 401, reason)
        # datetime_str = form.data['effective_date']
        # datetime_obj = datetime.strptime(datetime_str, DATETIME_FORMAT)
        # form.data['effective_date'] = datetime_obj
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(
                '/SectionF?qapp_id=%s' % qapp_id)

        ctx = {'form': form, 'qapp_id': qapp_id}
        return render(request, self.template_name, ctx)


def get_qar5_for_user(user_id, qapp_id=None):
    """Get all qapps created by a User."""
    user = User.objects.get(id=user_id)
    if qapp_id:
        return Qapp.objects.filter(id=qapp_id)
    return Qapp.objects.filter(prepared_by=user)


def get_qar5_for_team(team_id, qapp_id=None):
    """Get all data belonging to a team."""
    team = Team.objects.get(id=team_id)
    include_qapps = QappSharingTeamMap.objects.filter(
        team=team).values_list('qapp', flat=True)

    if qapp_id:
        return Qapp.objects.filter(
            id__in=include_qapps).filter(id=qapp_id).first()

    return Qapp.objects.filter(id__in=include_qapps)


def get_qapp_info(user, qapp_id):
    """Return all pieces of a qapp in a dictionary."""
    ctx = {}
    ctx['qapp'] = get_qar5_for_user(user.id, qapp_id).first()

    # Only return this if the user has access to it via super, owner, or team:
    # db_user = User.objects.get(id=user.id)

    if ctx['qapp'] or user.is_superuser or ctx['qapp'].prepared_by == user:
        ctx['qapp_leads'] = QappLead.objects.filter(qapp_id=qapp_id)
        ctx['qapp_approval'] = QappApproval.objects.filter(
            qapp_id=qapp_id).first()
        if ctx['qapp_approval']:
            ctx['signatures'] = QappApprovalSignature.objects.filter(
                qapp_approval_id=ctx['qapp_approval'].id)
        ctx['section_a'] = SectionA.objects.filter(qapp_id=qapp_id).first()
        ctx['section_b'] = SectionB.objects.filter(qapp_id=qapp_id).all()
        ctx['section_c'] = SectionC.objects.filter(qapp_id=qapp_id).first()
        ctx['section_d'] = SectionD.objects.filter(qapp_id=qapp_id).first()
        ctx['references'] = References.objects.filter(qapp_id=qapp_id).first()
        ctx['revisions'] = Revision.objects.filter(qapp_id=qapp_id)
        ctx['title'] = str(ctx['qapp'])
        return ctx

    return None
