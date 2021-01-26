# qar5.py (constants)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301

"""Add docstring."""

#######################################################
# Constants and Strings for the QAPP module Section A.
A2_DEFINITIONS_ACRONYMS = 'Add definitions or ' + \
    'acronyms here. If none enter (N/A).'

A3_DISTRIBUTION_LIST = 'Quality Assurance Project Plans and Standard ' + \
    'Operating Procedures shall be controlled through documented ' + \
    'approvals as required by Section 5.3 of the Office of Research ' + \
    'and Development Quality Management Plan. The project lead will ' + \
    'be responsible for distribution of the current signed approved ' + \
    'version of the QA Project Plan to project participants shown ' + \
    'in Section A.4. Signed approved versions of SOPs will be ' + \
    'available to project staff through the ORD@Work SOP intranet ' + \
    'site. Signature approved electronic copies of this QA Project Plan, ' + \
    'SOPs, and any associated QA assessment reports, will also be ' + \
    'maintained in ORD QA Track. The project lead will be responsible ' + \
    'for timely communications with all involved participants and will ' + \
    'retain copies of all management reports, memoranda, and ' + \
    'correspondence between research task personnel.'

A4_PROJECT_TASK_ORGANIZATION = 'Identify the individuals and ' + \
    'organizations participating in the research and discuss their ' + \
    'specific roles and responsibilities. Include and all persons ' + \
    'responsible for implementation. QA manager position must ' + \
    'indicate independence from unit collecting/using data.  ' + \
    'A table summarizing this information is recommended.'

A5_PROBLEM_DEFINITION_BACKGROUND = 'State the specific problem to be ' + \
    'solved, decision to be made, or outcome to be achieved. Include ' + \
    'sufficient background information to provide a historical, ' + \
    'scientific, and regulatory perspective for this particular project.'

A6_PROJECT_DESCRIPTION = 'Provide a high-level discussion of how, when, ' + \
    'and where the research effort will be conducted over the duration ' + \
    'of the study.  Include any research questions or hypotheses, ' + \
    'purpose objectives, any dependencies e.g., on other projects, ' + \
    'certain funding levels, a certain measure of success at early ' + \
    'stages of the project, etc., and any critical issues. This ' + \
    'could optionally include information on potential impact or ' + \
    'customer partner concerns. or equipment requirements. Provide an ' + \
    'estimated timeline for completion of key tasks e.g., QA Project ' + \
    'Plan and Health and Safety Plan development, data collect, etc. ' + \
    'with respect to the target dates for the research project deliverables.'

A7_QUALITY_OBJECTS_CRITERIA = 'Discuss the quality objectives for the ' + \
    'project and the performance criteria to achieve those objectives. ' + \
    'EPA requires the use of a systematic planning process to define ' + \
    'these quality objectives and performance criteria. State project ' + \
    'objectives and limits, both qualitatively and quantitatively. ' + \
    'State and characterize measurement quality objectives ' + \
    'as to applicable action levels or criteria.'

A8_SPECIAL_TRAINING_CERTIFICATION = 'Identify and describe any ' + \
    'specialized training or certifications needed by personnel in ' + \
    'order to successfully complete the project or task. Discuss how ' + \
    'such training will be provided and how the necessary skills ' + \
    'will be assured and documented.'

A9_DOCUMENTS_RECORDS = 'Research activities must be documented according ' + \
    'to the requirements of ORD QA Policies titled Scientific ' + \
    'Recordkeeping: Paper, Scientific Recordkeeping Electronic, and ' + \
    'Quality Assurance Quality Control Practices for ORD Laboratory and ' + \
    'Field-Based Research, as well as requirements defined in this QA ' + \
    'Project Plan. The ORD QA Policies require the use of research ' + \
    'notebooks and the management of research records, both paper and ' + \
    'electronic, such that project research data generation may continue ' + \
    'even if a researcher or an analyst participating in the project ' + \
    'leaves the project staff. Electronic project records can be ' + \
    'maintained by the project lead on using this ' + \
    '<a href="/existingdata"> QAPP Builder Tool' + \
    '</a> or can ' + \
    'be stored on the ORD network drive, List file path where files ' + \
    'are stored. Electronic Records shall be maintained in a manner that ' + \
    'maximizes the confidentiality, accessibility, and integrity of the ' + \
    'data. ORD PPM Section 13.6 provides guidance on the maintenance of ' + \
    'electronic records for ORD. Records retention: Records that are ' + \
    'generated under this research effort will be retained in accordance ' + \
    'with EPA Records Schedule 1035, and as required by Section 5.1 of ' + \
    'the ORD Quality Management Plan for __category__ Projects.'

# A9_RECORDS_RETENTION = """
#    Records retention: Records that are generated under this research effort
#    will be retained in accordance with EPA Records Schedule 1035, and as
#    required by Section 5.1 of the ORD Quality Management Plan for QA Category
#    A Projects.
# """

SECTION_A_INFO = {
    'a2': A2_DEFINITIONS_ACRONYMS,
    'a3': A3_DISTRIBUTION_LIST,
    'a4': A4_PROJECT_TASK_ORGANIZATION,
    'a5': A5_PROBLEM_DEFINITION_BACKGROUND,
    'a6': A6_PROJECT_DESCRIPTION,
    'a7': A7_QUALITY_OBJECTS_CRITERIA,
    'a8': A8_SPECIAL_TRAINING_CERTIFICATION,
    'a9': A9_DOCUMENTS_RECORDS
    # 'A.9 Documents and Records': [A9_DOCUMENTS_RECORDS, A9_RECORDS_RETENTION]
}

SECONDARY_DATA_OPTIONS = (
    ('Analytical Methods', 'Analytical Methods'),
    ('Animal Subjects', 'Animal Subjects'),
    ('Cell Culture Models', 'Cell Culture Models'),
    ('Existing Data', 'Existing Data'),
    ('Measurements', 'Measurements'),
    ('Model Application', 'Model Application'),
    ('Model Development', 'Model Development'),
    ('Software Development', 'Software Development')
)

B1_SECONDARY_DATA = 'Identify the Existing Data and Information ' + \
    'needed to meet the ' + \
    'research objectives. If covered in project QAPP cite. If N/A type N/A.'

B1_EXISTING_DATA = 'Describe how the existing data information will be ' + \
    'used in the research effort e.g. augment or replace existing data ' + \
    'information, verify or validate existing data information. If ' + \
    'covered in project QAPP cite. If N/A type N/A.'

B1_DATA_REQUIREMENTS = 'Specify requirements relating to the type of ' + \
    'data, the age of data, geographical representation, temporal ' + \
    'representation, and technological representation, as applicable. ' + \
    'If covered in project QAPP cite. If N/A type N/A.'

B1_DATABASES_MAPS_LITERATURE = '(1) Information and data used to site ' + \
    'or time sampling events meteorology, geology, etc.\r\n ' + \
    '(2) Anecdotal or other information triggering the study\r\n ' + \
    '(3) Toxicity, exposure, and environmental fate data\r\n ' + \
    '(4) Models and their output\r\n ' + \
    '(5) Census data\r\n ' + \
    '(6) GIS data.\r\n ' + \
    'If covered in project QAPP cite. If N/A type N/A.'

B1_NON_QUALITY_CONSTRAINTS = 'Identify any non-quality constraints on ' + \
    'the Existing Data and Information information that affect its ' + \
    'use in the research ' + \
    'effort e.g., legal, programmatic, privacy confidentiality i.e. is ' + \
    'it proprietary or CBI. If supporting an office, region or program ' + \
    'check on applicability of the project decision, examples may ' + \
    'include: CAA Credible Evidence Revisions FR 62:36 Feb. 24 1997 or ' + \
    'Federal Rule of Evidence 702. If covered in ' + \
    'project QAPP cite. If N/A type N/A.'

B2_SECONDARY_DATA_SOURCES = 'Identify the sources for the Existing Data ' + \
    'and Information. Describe the planning process for data ' + \
    'gathering and how ' + \
    'the project ensures that data or information collected are of ' + \
    'sufficient quality to satisfy the needs of the research effort. ' + \
    'If covered in project QAPP cite. If N/A type N/A.'

B2_PROCESS = 'Describe the process for acceptance rejection and ' + \
    'inclusion exclusion of Existing Data and Information to support ' + \
    'research objectives e.g., to exclude potential bias. If covered in ' + \
    'project QAPP cite. If N/A type N/A.'

B2_RATIONALE = 'Discuss the rationale for selecting the sources ' + \
    'identified. If a hierarchy of sources exists for the gathering of ' + \
    'Existing Data and Information, specify that hierarchy. If covered in ' + \
    'project QAPP cite. If N/A type N/A.'

B2_PROCEDURES = 'Describe the procedures for determining the quality of ' + \
    'the Existing Data and Information. Identify criteria for ' + \
    'evaluating data or ' + \
    'information quality e.g., using EPAs five General Assessment ' + \
    'Factors or using measurement data criteria such as accuracy, ' + \
    'precision, representativeness, completeness, and comparability. ' + \
    'Note Existing published data from sources such as governmental ' + \
    'databases which have well-documented QA QC procedures may not ' + \
    'require additional evaluation for quality. If covered in project ' + \
    'QAPP cite. If N/A type N/A.'

B2_DISCLAIMER = 'If the quality of the Existing Data and ' + \
    'Information will not be ' + \
    'evaluated by EPA, state this in the QAPP and require one of the ' + \
    'following disclaimer statements to be added to any research product ' + \
    'requiring clearance: EPA is distributing this information solely as ' + \
    'a public service. Insert name of information source is responsible ' + \
    'for the quality of this information. EPAs distribution of this ' + \
    'information does not represent or imply endorsement by EPA. or The ' + \
    'research presented was not performed or funded by EPA and was not ' + \
    'subject to EPAs quality system requirements. The views ' + \
    'expressed in this product are those of the authors and do not ' + \
    'necessarily represent the views or the policies of the U.S. ' + \
    'Environmental Protection Agency. If covered in project ' + \
    'QAPP cite. If N/A type N/A.'

B3_PROCESS = 'Describe the process for documenting and tracking sources ' + \
    'used and the information that will be recorded for the ' + \
    'Existing Data and Information ' + \
    'collected e.g. data source, originating organization, report ' + \
    'title, type of information, date. If covered in project ' + \
    'QAPP cite. If N/A type N/A'

B4_EXISTING_DATA_TRACKING = 'Existing data sources are tracked and ' + \
    'logged in CESER application Existing Data and Information Search ' + \
    'Tool https://134.67.216.106 under CESER ' + \
    'QAPP K-LRTD-0032360-QP-1-0. If covered in project QAPP ' + \
    'cite. If N/A type N/A.'

SECTION_B_INFO = {
    'b1_0': SECONDARY_DATA_OPTIONS, 'b1_1': B1_SECONDARY_DATA,
    'b1_2': B1_EXISTING_DATA, 'b1_3': B1_DATA_REQUIREMENTS,
    'b1_4': B1_DATABASES_MAPS_LITERATURE, 'b1_5': B1_NON_QUALITY_CONSTRAINTS,
    'b2_1': B2_SECONDARY_DATA_SOURCES, 'b2_2': B2_PROCESS,
    'b2_3': B2_RATIONALE, 'b2_4': B2_PROCEDURES, 'b2_5': B2_DISCLAIMER,
    'b3': B3_PROCESS, 'b4': B4_EXISTING_DATA_TRACKING
}

#######################################################
# Constants and Strings for the QAPP module Section C.
# This TEXT needs to be added automatically for C.1
C1_ASSESSMENTS_RESPONSE_ACTIONS = 'For __category__ projects, at least ' + \
    'one QA audit is required per ORD QA Policy titled Use of the Graded ' + \
    'Approach for Quality Assurance of Research.  A technical systems ' + \
    'audit TSA will be completed within one year of the initial QA ' + \
    'Project Plan approval date for this research effort. The TSA ' + \
    'will be conducted in accordance with ORD QA Policy titled Audits ' + \
    'of Technical and Quality Systems. Draft publications resulting from ' + \
    'this project will undergo ORD clearance in STICS prior to ' + \
    'dissemination as required by ORD Policy titled ORD Clearance Policy ' + \
    'and Procedures and CESER SOP titled Standard Operating ' + \
    'Procedure for Product Clearance.'

# This TEXT needs to be added automatically for C.2
C2_REPORTS_TO_MANAGEMENT = 'Results of QA audits will be reported in ' + \
    'accordance with ORD QA Policy titled Audits of Technical and ' + \
    'Quality Systems.  Implementation of corrective actions for audit ' + \
    'findings will be verified by the QA Manager, and status of ' + \
    'implementation tracked through closure. Required approvals for ' + \
    'draft publications undergoing ORD clearance is documented in STICS.'

C3_QUALITY_METRICS = 'For each process measurement and analytical ' + \
    'method, identify the required QC checks (e.g., blanks, control ' + \
    'samples, duplicates, matrix spikes, surrogates), the frequencies ' + \
    'for performing these checks, associated acceptance criteria, and ' + \
    'corrective actions to be performed if acceptance criteria are not ' + \
    'met. Any additional project-specific QA objectives (e.g., ' + \
    'completeness, mass balance) shall be presented, ' + \
    'including acceptance criteria.'

SECTION_C_DEFAULTS = {
    'C.1 Assessments and Response Actions': C1_ASSESSMENTS_RESPONSE_ACTIONS,
    'C.2 Reports to Management': C2_REPORTS_TO_MANAGEMENT
}
SECTION_C_INFO = {
    0: C1_ASSESSMENTS_RESPONSE_ACTIONS,
    1: C2_REPORTS_TO_MANAGEMENT
}

#######################################################
# Constants and Strings for the QAPP module Section D.
D1_DATA_REVIEW_VERIFICATION_VALIDATION = 'Itemize the information and ' + \
    'records which must be included in the data report package and ' + \
    'specify the reporting format for hard copy and any electronic ' + \
    'forms. Records can include raw data, data from other sources such ' + \
    'as databases or literature, field logs, sample preparation and ' + \
    'analysis logs, instrument printouts, model input and output files, ' + \
    'and results of calibration and QC checks. Discuss responsibilities ' + \
    'for conducting data review data generator, verification second ' + \
    'reviewer, and validation independent reviewer. State criteria for ' + \
    'accepting, rejecting, or qualifying data; include project-specific ' + \
    'calculations or algorithms. See Agency guidance document titled ' + \
    'Guidance on Environmental Data Verification and Data Validation.'

D2_VERIFICATION_VALIDATION_METHODS = 'Describe the process for ' + \
    'conducting data verification and validation reviews. Identify ' + \
    'issue resolution procedure and responsible individuals. Identify ' + \
    'the method for conveying results to data users. Provide examples ' + \
    'of any forms or checklists to be used.'

D3_RECONCILIATION_USER_REQUIREMENTS = 'Describe how the data will be ' + \
    'summarized or analyzed e.g., qualitative analysis, descriptive or ' + \
    'inferential statistics to meet the project objectives. If ' + \
    'descriptive statistics are proposed, state what tables, plots, ' + \
    'and/or statistics e.g., mean, median, standard error, minimum and ' + \
    'maximum values will be used to summarize the data. If an ' + \
    'inferential method is proposed, indicate whether the method will ' + \
    'be a hypothesis test, confidence interval, or confidence limit and ' + \
    'describe how the method will be performed.'

SECTION_D_INFO = {
    'd1': D1_DATA_REVIEW_VERIFICATION_VALIDATION,
    'd2': D2_VERIFICATION_VALIDATION_METHODS,
    'd3': D3_RECONCILIATION_USER_REQUIREMENTS,
}

#######################################################
# Constants and Strings for the QAPP module Section E.
E1_REFERENCES = 'All references are stored and retrievable from ' + \
    'EXISTING DATA TRACKING SECTION THIS TOOL'

SECTION_E_INFO = {
    'E.1 REFERENCES': E1_REFERENCES
}

#######################################################
# Constants and Strings for the QAPP module Section F.
F1_REVISION_HISTORY = ''

SECTION_F_INFO = {
    'F.1 REVISION HISTORY': F1_REVISION_HISTORY
}
