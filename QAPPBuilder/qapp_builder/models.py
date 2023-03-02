# models.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301,E1101,W0611,C0411


"""Definition of models."""

from django.db import models
from django.utils import timezone
from accounts.models import User
from constants.qar5 import SECTION_C_INFO
from constants.utils import get_attachment_storage_path, upload_storage
from teams.models import Team


class Attachment(models.Model):
    """Class representing a file attachment to an Existing Data entry."""

    name = models.CharField(blank=False, null=False, max_length=255)
    file = models.FileField(null=True, blank=True,
                            upload_to=get_attachment_storage_path,
                            storage=upload_storage)
    uploaded_by = models.ForeignKey(User, blank=False,
                                    on_delete=models.CASCADE)

    def __str__(self):
        """Override str method to display name instead of stringified obj."""
        return self.name


class Division(models.Model):
    """Class representing EPA Divisions available to the QAPP."""

    name = models.TextField(blank=False, null=False)

    def __str__(self):
        """Override str method to display name instead of stringified obj."""
        return str(self.name)


class SectionBType(models.Model):
    """Class representing Section B Types."""

    name = models.TextField(blank=False, null=False)

    def __str__(self):
        """Override str method to display name instead of stringified obj."""
        return str(self.name)


class Qapp(models.Model):
    """Class representing a QAPP. Allows users to easily generate new QAPPs."""

    # Office of Research and Development
    # Center for Environmental Solutions & Emergency Response

    division = models.ForeignKey(Division, blank=False, null=False,
                                 related_name='divisions',
                                 on_delete=models.CASCADE)
    division_branch = models.TextField(blank=False, null=False)
    title = models.TextField(blank=False, null=False)
    qa_category = models.TextField(blank=False, null=False)
    intra_extra = models.CharField(blank=False, null=False,
                                   max_length=64)
    revision_number = models.TextField(blank=False, null=False)
    date = models.DateTimeField(blank=False, null=False,
                                default=timezone.now)
    prepared_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    strap = models.TextField(blank=False, null=False)
    tracking_id = models.TextField(blank=False, null=False)
    # List of teams with which the QAPP is shared.
    teams = models.ManyToManyField(Team, through='QappSharingTeamMap')

    def __str__(self):
        """Override str method to display name instead of stringified obj."""
        return str(self.title)


class QappSharingTeamMap(models.Model):
    """Mapping between QAPP and Teams they share."""

    added_date = models.DateTimeField(
        auto_now_add=True, blank=False, editable=False)
    qapp = models.ForeignKey(
        Qapp, blank=False, related_name='qapp_teams',
        on_delete=models.CASCADE)
    team = models.ForeignKey(Team, blank=False,
                             related_name='team_qapp',
                             on_delete=models.CASCADE)
    # Indicates if the team can edit the project.
    can_edit = models.BooleanField(blank=False, default=True)


class QappLead(models.Model):
    """
    Class representing a QAPP project lead.

    Project has a one-to-many relationship with ProjectLead(s).
    """

    name = models.TextField(blank=False, null=False)
    qapp = models.ForeignKey(Qapp, on_delete=models.CASCADE)

    def __str__(self):
        """Override str method to display name instead of stringified obj."""
        return str(self.name)


class QappApproval(models.Model):
    """Class representing the approval page of a QAPP document."""

    project_plan_title = models.TextField(blank=False, null=False)
    activity_number = models.TextField(blank=False, null=False)
    qapp = models.OneToOneField(Qapp, blank=False,
                                on_delete=models.CASCADE,
                                primary_key=False)
    # Dynamic number of signatures, one-to-many:


class QappApprovalSignature(models.Model):
    """Class representing a single signature on a QAPP Approval Page."""

    qapp_approval = models.ForeignKey(QappApproval, blank=False,
                                      on_delete=models.CASCADE)
    contractor = models.BooleanField(blank=True, null=False, default=False)
    name = models.TextField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)


class SectionA(models.Model):
    """Class representing SectionA (A.3 and later) for a given QAPP."""

    qapp = models.OneToOneField(Qapp, on_delete=models.CASCADE,
                                primary_key=True)
    # A2 is new, see Jira DAT-32
    a2 = models.TextField(blank=False, null=False)
    # Keywords input field is new, see Jira DAT-35
    a2_keywords = models.TextField(blank=False, null=False)
    # A3 WAS readonly, defaults populated in form from constants module.
    a3 = models.TextField(blank=False, null=False)
    # A4 is user input with an optional chart (a4_chart)
    a4 = models.TextField(blank=False, null=False)
    a4_chart = models.FileField(null=True, blank=True,
                                upload_to=get_attachment_storage_path)
    a5 = models.TextField(blank=False, null=False)
    a6 = models.TextField(blank=False, null=False)
    a7 = models.TextField(blank=False, null=False)
    a8 = models.TextField(blank=False, null=False)
    # A9 is mixed defaults and user input, thus we should break it up
    a9 = models.TextField(blank=False, null=False)
    a9_drive_path = models.TextField(blank=False, null=False)
    # Multi-select for the SectionB Classificiations
    sectionb_type = models.ManyToManyField(
        SectionBType, through='SectionBTypeMap')


class SectionBTypeMap(models.Model):
    """
    Section A to Section B Type Map.

    Mapping for many-to-many relationship between
    Section A and its Section B Types.
    """

    sectiona = models.ForeignKey(
        SectionA, blank=False, on_delete=models.CASCADE)
    sectionb_type = models.ForeignKey(
        SectionBType, blank=False, on_delete=models.CASCADE)


class SectionB(models.Model):
    """
    Class representing the entirety of SectionB for a given QAPP.

    Instead of creating a Section B class for each of the Section B Types,
    there will instead be one class with extra nullable fields. There
    will likely still be multiple forms for the different Section B Types.
    """

    qapp = models.ForeignKey(Qapp, on_delete=models.CASCADE)
    sectionb_type = models.ForeignKey(
        SectionBType, on_delete=models.CASCADE)

    b1_1 = models.TextField(blank=True, null=True)
    b1_2 = models.TextField(blank=True, null=True)
    b1_3 = models.TextField(blank=True, null=True)
    b1_4 = models.TextField(blank=True, null=True)
    b1_5 = models.TextField(blank=True, null=True)
    b1_6 = models.TextField(blank=True, null=True)
    b1_7 = models.TextField(blank=True, null=True)

    b2_1 = models.TextField(blank=True, null=True)
    b2_2 = models.TextField(blank=True, null=True)
    b2_3 = models.TextField(blank=True, null=True)
    b2_4 = models.TextField(blank=True, null=True)
    b2_5 = models.TextField(blank=True, null=True)
    b2_6 = models.TextField(blank=True, null=True)
    b2_7 = models.TextField(blank=True, null=True)
    b2_8 = models.TextField(blank=True, null=True)

    b3_1 = models.TextField(blank=True, null=True)
    b3_2 = models.TextField(blank=True, null=True)
    b3_3 = models.TextField(blank=True, null=True)
    b3_4 = models.TextField(blank=True, null=True)
    b3_5 = models.TextField(blank=True, null=True)
    b3_6 = models.TextField(blank=True, null=True)
    b3_7 = models.TextField(blank=True, null=True)
    b3_8 = models.TextField(blank=True, null=True)
    b3_9 = models.TextField(blank=True, null=True)
    b3_10 = models.TextField(blank=True, null=True)

    b4_1 = models.TextField(blank=True, null=True)
    b4_2 = models.TextField(blank=True, null=True)
    b4_3 = models.TextField(blank=True, null=True)
    b4_4 = models.TextField(blank=True, null=True)
    b4_5 = models.TextField(blank=True, null=True)

    b5_1 = models.TextField(blank=True, null=True)
    b5_2 = models.TextField(blank=True, null=True)
    b5_3 = models.TextField(blank=True, null=True)
    b5_4 = models.TextField(blank=True, null=True)
    b5_5 = models.TextField(blank=True, null=True)

    b6_1 = models.TextField(blank=True, null=True)
    b6_2 = models.TextField(blank=True, null=True)
    b6_3 = models.TextField(blank=True, null=True)

    class Meta:
        """Meta data definitions for SectionB class."""

        # Tell the model that these two fields are unique together.
        # This is similar to declaring a composite primary key:
        unique_together = ('qapp', 'sectionb_type')


class SectionC(models.Model):
    """Class representing the entirety of SectionC for a given QAPP."""

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, primary_key=True)
    # c1 WAS readonly, defaults populated in form from constants module.
    c1 = models.TextField(blank=False, null=False, default=SECTION_C_INFO[0])
    # c2 WAS readonly, defaults populated in form from constants module.
    c2 = models.TextField(blank=False, null=False, default=SECTION_C_INFO[1])


class SectionD(models.Model):
    """Class representing the entirety of SectionD for a given QAPP."""

    qapp = models.OneToOneField(
        Qapp, on_delete=models.CASCADE, primary_key=True)
    d1 = models.TextField(blank=False, null=False)
    d2 = models.TextField(blank=False, null=False)
    d3 = models.TextField(blank=False, null=False)


# NOTE: All references are stored and retrievable from
#       EXISTING DATA TRACKING SECTION THIS TOOL
class References(models.Model):
    """Class used to store references for the related QAPP."""

    qapp = models.OneToOneField(Qapp, on_delete=models.CASCADE,
                                primary_key=True)
    references = models.TextField(blank=True, null=True)


class Revision(models.Model):
    """
    Class used to track revisions of QAPPs.

    This model has a many-to-one relationship with the Qapp model.
    This model is referenced in the front-end as Section F.1
    """

    qapp = models.ForeignKey(Qapp, blank=False,
                             on_delete=models.CASCADE)
    revision = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    effective_date = models.DateTimeField(blank=False, null=False,
                                          default=timezone.now)
    initial_version = models.TextField(
        blank=False, null=False)
