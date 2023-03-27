# qar5_sectionb.py (constants)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301

"""Constants for the QAR5 qapp_builder module."""

SECTION_B_TYPES = (
    ('Analytical Methods', 'Analytical Methods'),
    ('Animal Subjects', 'Animal Subjects'),
    ('Cell Culture Models', 'Cell Culture Models'),
    ('Existing Data', 'Existing Data'),
    ('Measurements', 'Measurements'),
    ('Model Application', 'Model Application'),
    ('Model Development', 'Model Development'),
    ('Software Development', 'Software Development')
)

ANALYTICAL_METHODS = {
    'b1_1': {
        'heading': 'B.1 EXPERIMENTAL DESIGN',
        'label': 'B.1.1 Analyte(s) of Interest',
        'desc': '''Identify the specific analyte(s) of interest and the
                   matrix/matrices or limitations to the range of detection
                   under investigation.'''
    },
    'b1_2': {
        'label': 'B.1.2 Experimental Design',
        'desc': '''Describe the experimental design and how it will be
                   optimized for this project. A description of the design
                   should include the rationale for the design, types and
                   number of samples required.'''
    },
    'b1_3': {
        'label': 'B.1.3 Interference and Stability',
        'desc': '''Describe any tests of interference and analyte stability.
                   If a holding time study will be conducted, describe the
                   parameters of this study.'''
    },
    'b1_4': {
        'label': 'B.1.4 Sample Requirements',
        'desc': '''Provide the requirements for samples including those field
                   collected or made in the laboratory, that will be used to
                   test the method, including matrix and presence/concentration
                   of analytes.'''
    },
    'b2_1': {
        'heading': 'B.2 SAMPLING PROCEDURES',
        'label': 'B.2.1 Preparation of Synthetic Samples',
        'desc': '''If synthetic (i.e., laboratory-prepared) samples are used,
                   describe the preparation of these samples.'''
    },
    'b2_2': {
        'label': 'B.2.2 Environmental Sampling Design',
        'desc': '''If environmental (i.e., real-world sample) samples are
                   used describe the sampling design that will be used, and
                   the steps taken to assure that representative samples are
                   collected.'''
    },
    'b2_3': {
        'label': 'B.2.3 Environmental Sampling Procedures',
        'desc': '''If environmental samples are used, discuss or reference
                   each sampling procedure.'''
    },
    'b2_4': {
        'label': 'B.2.4 Environmental Sampling Package/Shipping',
        'desc': '''If environmental samples are used, describe procedures for
                   packing and shipping samples, and provisions for maintaining
                   chain-of-custody, as applicable.'''
    },
    'b2_5': {
        'label': 'B.2.5 Sample Preservation',
        'desc': '''Specify sample preservation requirements (e.g.,
                   refrigeration, acidification, etc.) and holding times,
                   unless being determined as part of the method development.'''
    },
    'b2_6': {
        'label': 'B.2.6 Sample Naming Conventions',
        'desc': '''Describe the method for a sample naming
                   convention to uniquely identify each sample and sub
                   aliquots of samples.'''
    },
    'b3_1': {
        'heading': 'B.3 MEASUREMENT PROCEDURES',
        'label': 'B.3.1 Calibration QA/QC',
        'desc': '''Describe in detail or reference each preparation or
                   analytical procedure, equipment and instrumentation to be
                   used, if known. Include steps for preparation, measurement,
                   quality control, and reporting. Include steps for testing,
                   inspection, and maintenance of equipment and instrumentation
                   to be used.'''
    },
    'b3_2': {
        'label': 'B.3.2 Detection Limits',
        'desc': '''Include specific calibration procedures, including linearity
                   checks and initial and continuing calibration checks, and
                   detection limits.'''
    },
    'b4_1': {
        'heading': 'B.4 METHOD PERFORMANCE METRICS',
        'label': 'B.4.1 QA/QC Checks',
        'desc': '''Identify the method performance metrics (QA/QC checks) that
                   will be used to evaluate the method. These metrics could
                   include (but are not limited to) positive and negative
                   controls, sensitivity, precision, accuracy, recovery,
                   linearity, specificity, robustness, and range. For each
                   method performance metric (QA/QC check) specify the methods
                   and frequencies for performing these checks, associated
                   acceptance criteria, and corrective actions to be performed
                   if acceptance criteria are not met.'''
    },
    'b4_2': {
        'label': 'B.4.2 Method Validation',
        'desc': '''Describe in detail the method validation process (e.g.,
                   intramural laboratory, extramural laboratories, etc.).'''
    },
    'b4_3': {
        'label': 'B.4.3 Critical Supplies and Consumables',
        'desc': '''Describe as appropriate critical supplies and consumables,
                   including but not limited to, manufacturer, catalog number,
                   certifications, and receipt procedures.'''
    },
    'b5_1': {
        'heading': 'B.5 DATA VALIDATION & VERIFICATION',
        'label': 'B.5.1 Data V&V',
        'desc': '''Discuss responsibilities for conducting data review,
                   verification, and validation of data, data tables and
                   calculations. State criteria for accepting, rejecting, or
                   qualifying data. Include project-specific calculations or
                   algorithms. (May be discussed in SOP).'''
    },
    'b5_2': {
        'label': 'B.5.2 Data Assessment',
        'desc': '''Describe how the data will be assessed with regards to the
                   project objects (e.g., qualitative analysis, descriptive or
                   inferential statistics, etc.). If descriptive statistics are
                   proposed, state what tables, plots, and/or statistics (e.g.,
                   mean, median, standard error, minimum and maximum values,
                   etc.) will be used to summarize the data. If an inferential
                   method is proposed, indicate whether the method will be a
                   hypothesis test, confidence interval, or confidence limit.
                   Describe how the method will be performed.'''
    }
}

# ########################################################################
# ########################################################################
# ########################################################################

ANIMAL_CELL = {
    'b1_1': {
        'heading': 'B.1 EXPERIMENTAL DESIGN',
        'label': 'B.1.1 Animal Subjects Tested',
        'desc': '''<b>In Vivo:</b>  Discuss and characterize the choice of
                   animal subjects to be tested, including ACUP/LAPR
                   references, if applicable, in addressing the project
                   objectives (ACUP = Animal Care and Use Protocol, previously
                   known as the LAPR = Laboratory Animal Protocol Report).
                   These documents address the regulatory animal care and use
                   ethics requirements.)
                   <b>In Vitro:</b> Discuss the culture model to be used
                   in addressing the project objectives.'''
    },
    'b1_2': {
        'label': 'B.1.2 Chemicals, Materials, Stressors',
        'desc': '''Discuss the choice of chemicals, materials, or other
                   stressors to be tested in addressing the project objectives.
                   Discuss the reasoning as to why this model was selected and
                   most appropriate in addressing the project's objectives.'''
    },
    'b1_3': {
        'label': 'B.1.3 Independent Variables',
        'desc': '''Discuss independent variables to be manipulated.'''
    },
    'b1_4': {
        'label': 'B.1.4 Dependent Variables',
        'desc': '''Discuss dependent variables to be measured'''
    },
    'b1_5': {
        'label': 'B.1.5 Physical/Behavioral Metrics',
        'desc': '''Discuss metrics, physical or behavioral features, or
                   dependent variables to be measured or observed (e.g.,
                   survival/lethality, reaction time, cell appearance or
                   morphology of organs, weight, viability, gene expression,
                   behavioral changes, etc.).'''
    },
    'b2_1': {
        'heading': 'B.2 METHODS AND EXPERIMENTAL DETAIL',
        'label': 'B.2.1 Determining Test Group',
        'desc': '''Describe the method for determining test group treatment,
                   number, and size (dose limits; power calculations).'''
    },
    'b2_2': {
        'label': 'B.2.2 Methods for Controls and Test Groups',
        'desc': '''Describe study controls (blinding, standard curves,
                   positive/negative controls, replicates, sentinel, sham
                   animals, etc.) If applicable, describe the test group
                   assignment method and identification for individual animal
                   subjects (randomization, tagging, group housing).'''
    },
    'b2_3': {
        'label': 'B.2.3 Sample Collection',
        'desc': '''Provide details of sample collection, identification,
                   storage, analysis, the chain of custody, etc.'''
    },
    'b2_4': {
        'label': 'B.2.4 Project Personnel',
        'desc': '''List the project personnel/collaborators and their roles.'''
    },
    'b2_5': {
        'label': 'B.2.5 SOPs',
        'desc': '''List and attach all operating procedures or protocols and
                   ensure that they include adequate quality control.'''
    },
    'b2_6': {
        'label': 'B.2.6 Other SOPs',
        'desc': '''Describe the procedures to be used for any activities that
                   are not covered by existing operating procedures or
                   protocols. Ensure that appropriate quality control is
                   included in the description (e.g., +/- controls, standard
                   curves, limits of detection, etc.)'''
    },
    'b2_7': {
        'label': 'B.2.7 Non-Measurement Data',
        'desc': '''Identify any types of data obtained from non-measurement
                   sources (i.e., databases, programs, literature files) and
                   describe the intended use, acceptance criteria, and
                   limitations for the use of such data.'''
    },
    'b3_1': {
        'heading': 'B.3 EQUIPMENT AND SUPPLIES',
        'label': 'B.3.1 Equipment',
        'desc': '''List major equipment (make, model).  Discuss calibration,
                   performance evaluation criteria, etc., and frequency of
                   such processes for the equipment.'''
    },
    'b3_2': {
        'label': 'B.3.2 Supplies',
        'desc': '''List critical supplies/consumables (name, source, amount,
                   expiration dates, if any).'''
    },
    'b4_1': {
        'heading': 'B.4 DATA COLLECTION AND ANALYSIS',
        'label': 'B.4.1 Datasets',
        'desc': '''List and describe datasets to be collected
                   (analog, electronic, etc.).'''
    },
    'b4_2': {
        'label': 'B.4.2 V&V',
        'desc': '''Describe data verification procedures used to ensure
                   reporting of accurate data'''
    },
    'b4_3': {
        'label': 'B.4.3 Data Validation',
        'desc': '''Describe data validation procedures used to ensure data met
                   quality requirements. Describe what will be done with data
                   that falls outside quality criteria (e.g., rejection,
                   flagging, etc.).'''
    },
    'b4_4': {
        'label': 'B.4.4 Statistical Analysis',
        'desc': '''Describe planned statistical analysis following the guidance of
                   <a href="https://intranet.ord.epa.gov/cop-statistics/communities-practice-cop-statistics">
                   https://intranet.ord.epa.gov/cop-statistics/communities-practice-cop-statistics</a>'''
    }
}

# ########################################################################
# ########################################################################
# ########################################################################

# TODO: Make sure all references to this template are removed:
# CELL_CULTURE_METHODS

# ########################################################################
# ########################################################################
# ########################################################################

EXISTING_DATA = {
    'b1_1': {
        'heading': 'B.1 DATA DESCRIPTION, ACQUISITION AND COLLECTION ',
        'label': 'B.1.1 Existing Data',
        'desc': '''Identify the existing data types needed to meet the research
                   objective(s). This includes but not limited to census data,
                   GIS data, models and their outputs, toxicity and exposure
                   data from published studies, environmental fate data, site
                   and time sampling events (e.g. meteorology, topography).'''
    },
    'b1_2': {
        'label': 'B.1.2 Data Requirements',
        'desc': '''Specify requirements related to the type of data. This
                   includes but not limited to data format, the age of data,
                   geographical representation, temporal representation, and
                   technological representation, as applicable. Existing data
                   can be from computer databases, programs, literature files,
                   or other historical sources.'''
    },
    'b1_3': {
        'label': 'B.1.3 Existing Data Sources',
        'desc': '''Identify the source(s) for the existing data. This
                   information can be presented as a table that includes the
                   rationale for selecting the source(s) identified. You will
                   need to discuss if the data sources have well-documented
                   QA/QC procedures. If a data set is considered “higher
                   quality” than another, the rationale for this decision
                   should be documented.'''
    },
    'b1_4': {
        'label': 'B.1.4 Data Gathering Method(s)',
        'desc': '''Describe the planning process for data gathering.
                   Systematic Review of literature can be employed and
                   described here.'''
    },
    'b2_1': {
        'heading': 'B.2 DATA EVALUATION, CURATION, AND USE',
        'label': 'B.2.1 Data Source Preservation',
        'desc': '''Describe the process used to maintain the original data
                   sources. For example, how and where are journal articles,
                   reports, databases, etc. saved or preserved.'''
    },
    'b2_2': {
        'label': 'B.2.2 Data Cleaning',
        'desc': '''Describe the operating process that takes place to clean
                   the data of anomalies (i.e. spelling errors, missing values,
                   improper entries, etc.).'''
    },
    'b2_3': {
        'label': 'B.2.3 Data Selectivity',
        'desc': '''Describe the acceptance criteria for the selection or
                   omission of data (or data sets) and then describe the
                   process (including documentation) of the acceptance
                   criteria. (e.g., using EPA's five General Assessment
                   Factors or using measurement data criteria such as accuracy,
                   precision, representativeness, completeness, and
                   comparability). See References.'''
    },
    'b2_4': {
        'label': 'B.2.4 Data Quality',
        'desc': '''Describe the procedures for determining the
                   quality of the existing data.'''
    },
    'b2_5': {
        'label': 'B.2.5 Peer Review Status',
        'desc': '''To what extent has independent peer review been conducted
                   of the data set or study method and results, and how were
                   the conclusions of this review taken into account?'''
    },
    'b2_6': {
        'label': 'B.2.6 Data/Information Format Conversion',
        'desc': '''Describe the process of converting data (or information)
                   from one format to another. Usually the format of a source
                   data into the required format of a new destination
                   system.'''
    },
    'b2_7': {
        'label': 'B.2.7 Data Curation Process Verification',
        'desc': '''Describe the existing verification process of the data
                   curation activities including how and where these
                   verifications are documented. Include how each of the
                   described processes are documented that they have been
                   completed.'''
    },
    'b2_8': {
        'label': 'B.2.8 Research Use',
        'desc': '''Describe how the existing data/information will be used in
                   the research effort (e.g., augment or replace existing
                   data/information, verify or validate
                   existing data/information).'''
    },
    'b2_9': {
        'label': 'B.2.9 Data Applicability/Usefulness',
        'desc': '''How useful or applicable is the scientific, statistical, or
                   economic theory applied in the study or data set to the
                   Agency's intended use of the analysis?'''
    },
    'b2_10': {
        'label': 'B.2.10 Usage Restraints',
        'desc': '''What constraints are there on the usage of the information
                   or data (e.g. legal, logistical, programmatic,
                   privacy/confidentiality, language barriers, etc.'''
    },

    'b3_1': {
        'heading': 'B.3 DATA MANAGEMENT AND DOCUMENTATION',
        'label': 'B.3.1 Management Requirements',
        'desc': '''Document the hardware, software, and personnel requirements
                   for managing and incorporating existing data into the
                   project.'''
    },
    'b3_2': {
        'label': 'B.3.2 Data Storage',
        'desc': '''Describe how data will be stored, shared, and secured'''
    },
    'b3_3': {
        'label': 'B.3.3 Special Access/Storage Requirements',
        'desc': '''Describe if existing data contains CBI or PII and address
                   special agreements, special access certifications and
                   storage requirements that apply'''
    },
    'b3_4': {
        'label': 'B.3.4 Metadata Storage',
        'desc': '''How and where will metadata be recorded? (i.e., data
                   source, originating organization, report title,
                   type of information) '''
    },
    'b3_5': {
        'label': 'B.3.5 Translation Procedure(s)',
        'desc': '''Describe procedures used to ensure that errors in
                   translation are minimized'''
    },
    'b3_6': {
        'label': 'B.3.6 Data Access Management',
        'desc': '''Describe measures taken to prevent unauthorized or
                   accidental editing of data, such as version control
                   procedures and internal database audit logs'''
    },
    'b3_7': {
        'label': 'B.3.7 Original Data Integrity',
        'desc': '''Describe procedures used to ensure that existing data
                   maintain their original integrity and quality as they are
                   migrated into current project'''
    },

    'b4_1': {
        'heading': 'B.4 DATA VERIFICATION AND VALIDATION',
        'label': 'B.4.1 IV&V',
        'desc': '''Describe the extent in which there has been independent
                   verification or validation of the data set or study method
                   and result'''
    },
    'b4_2': {
        'label': 'B.4.2 IV&V Results',
        'desc': '''Describe where results of the independent reviews of the
                   data set are documented'''
    },
    'b4_3': {
        'label': 'B.4.3 IV&V Corrective Action',
        'desc': '''Describe how the corrective action process of the
                   independent reviews of the data sets occur and how these
                   corrective actions are documented'''
    },
    'b4_4': {
        'label': 'B.4.4 Mathematical/Statistical Procedures',
        'desc': '''Discuss any mathematical or statistical procedures (such
                   as outlier analyses or goodness-of-fit tests) that will
                   identify whether individual data values within existing
                   data sets should be rejected, transformed, or otherwise
                   qualified before any statistical analysis'''
    },
    'b4_5': {
        'label': 'B.4.5 Data Validation Procedures',
        'desc': '''Describe any data validation procedures to be applied to
                   the existing data to ensure the use of accurate and
                   representative project data that are fit-for-purpose
                   in addressing the research question'''
    },
    'b4_6': {
        'label': 'B.4.6 Cross-Validation',
        'desc': '''Describe if any cross validation is used. Cross-validation
                   is a resampling procedure that is a useful technique when
                   the goal is either model prediction accuracy (minimizing
                   prediction error) or determining the right model for
                   interpretation.  For example: cross validation can be used
                   to evaluate the accuracy of models on a limited data
                   sample'''
    },
}

# ########################################################################
# ########################################################################
# ########################################################################

MEASUREMENTS_AND_MONITORING = {
    'b1_1': {
        'heading': 'B.1 EXPERIMENTAL DESIGN',
        'label': 'B.1.1 Analyte(s) of Interest & Matrix/Matrices',
        'desc': 'Identify the specific analyte(s) of interest and the ' +
                'matrix/matrices. Classify each measurement parameter ' +
                'as either critical or needed for information only.'
    },
    'b1_2': {
        'label': 'B.1.2 Sampling and/or Experimental Design',
        'desc': 'Describe sampling and/or experimental design to ' +
                'generate the data needed to evaluate the research ' +
                'objectives. A description of the design should ' +
                'include the rationale for the design and types ' +
                'and number of samples required, including any ' +
                'field or experimental QC samples.'
    },
    'b1_3': {
        'label': 'B.1.3 Sampling Locations & Frequency',
        'desc': 'Identify sampling locations and frequency of sampling.'
    },
    'b2_1': {
        'heading': 'B.2 SAMPLING PROCEDURES',
        'label': 'B.2.1 Non-Synthetic (real-world sample) Samples',
        'desc': 'If non-synthetic (i.e., real-world sample) ' +
                'samples are used describe the sampling design that ' +
                'will be used, and the steps taken to assure that ' +
                'representative samples are collected.'
    },
    'b2_2': {
        'label': 'B.2.2 Synthetic (lab-prepared) Samples',
        'desc': 'If synthetic (i.e., laboratory-prepared) ' +
                'samples are used, describe the preparation of these samples.'
    },
    'b2_3': {
        'label': 'B.2.3 Decontamination Procedures',
        'desc': 'Describe the decontamination procedures for any ' +
                'sampling equipment that will be reused to ' +
                'prevent cross contamination.'
    },
    'b2_4': {
        'label': 'B.2.4 Sample Containers & Quantities',
        'desc': 'Provide a list of sample containers, sample quantities ' +
                'to be collected, and the sample amount required for ' +
                'each analysis, including QC sample analysis.'
    },
    'b2_5': {
        'label': 'B.2.5 Labeling',
        'desc': 'Describe labeling (information to be included) ' +
                'and uniquely numbering each sample.'
    },
    'b2_6': {
        'label': 'B.2.6 Sample Preservation',
        'desc': 'Specify sample preservation requirements ' +
                '(e.g., refrigeration, acidification, etc.) ' +
                'and sample hold times.'
    },
    'b2_7': {
        'label': 'B.2.7 Calibration Procedures',
        'desc': 'If non-synthetic (i.e., real-world sample) samples ' +
                'are used describe procedures for packing and shipping ' +
                'samples, and provisions for maintaining ' +
                'chain-of-custody, as applicable.'
    },
    'b3_1': {
        'heading': 'B.3 MEASUREMENT PROCEDURES',
        'label': 'B.3.1 Field Analyses',
        'desc': 'For field analyses (including in-line measurements), ' +
                'describe in detail or reference each field sample ' +
                'analysis method and instrumentation to be used. ' +
                'Include steps for instrument calibration, ' +
                'measurement, quality control, and documentation of results.'
    },
    'b3_2': {
        'label': 'B.3.2 Lab Analyses',
        'desc': 'For laboratory analyses, describe in detail or ' +
                'reference each sample preparation method (e.g., ' +
                'sample extractions) and analytical methods, equipment ' +
                'and instrumentation to be used. Include steps for ' +
                'preparation, calibration, measurement, quality ' +
                'control, and reporting.'
    },
    'b3_3': {
        'label': 'B.3.3 Specific Calibration Procedures',
        'desc': 'Include specific calibration procedures, including ' +
                'linearity checks and initial and continuing calibration ' +
                'checks, and detection limits.'
    },
    'b4_1': {
        'heading': 'B.4 METHOD PERFORMANCE METRICS',
        'label': 'B.4.1 Method QC check',
        'desc': 'For each analysis method QC check (e.g., blanks, ' +
                'control samples, duplicates, matrix spikes, surrogates) ' +
                'specify the frequencies for performing these checks, ' +
                'associated acceptance criteria, and corrective actions ' +
                'to be performed if acceptance criteria are not met.'
    },
}

# ########################################################################
# ########################################################################
# ########################################################################

MODEL_APPLICATION = {
    'b1_1': {
        'heading': 'B.1 MODEL SPECIFICATION',
        'label': 'B.1.1 Conceptual Model',
        'desc': 'Describe the conceptual model, including key ' +
                'processes, system compartments, system boundaries, ' +
                'temporal and spatial scales, and fluxes into and ' +
                'out of the problem domain.'
    },
    'b1_2': {
        'label': 'B.1.2 Modeling Analysis',
        'desc': 'Describe how the modeling analysis fits into a larger ' +
                'project and its relationship to other efforts with ' +
                'separate QAPPs (if applicable).'
    },
    'b2_1': {
        'heading': 'B.2 MODEL SELECTION',
        'label': 'B.2.1 Model Functionality Requirements',
        'desc': 'Identify requirements for model functionality, e.g., ' +
                'accuracy, spatial and/or temporal discretization, ' +
                'run time, linkage to other models, etc.'
    },
    'b2_2': {
        'label': 'B.2.2 Hardware OS Specs',
        'desc': 'Specify computer hardware and operating system ' +
                'requirements, if applicable.'
    },
    'b2_3': {
        'label': 'B.2.3 SOPs Model Evaluation',
        'desc': 'Describe model evaluation procedures, such as ' +
                'comparisons to other available models, assessment of ' +
                'previous applications of the model, and any ' +
                'validation/verification activities.'
    },
    'b2_4': {
        'label': 'B.2.4 I/O Model Coupling',
        'desc': 'Employ more than one model loosely coupled together ' +
                '(i.e., output from one or more models serving as input to ' +
                'another model), provide an overview of the system design, ' +
                'including a diagram showing transfer of data between ' +
                'models.  (For projects that involve model integration ' +
                '(e.g., embedding one model within another or tight ' +
                'coupling of two or more models), see "Requirements ' +
                'for Model Development Projects" for additional guidance.)'
    },
    'b2_5': {
        'label': 'B.2.5 Model Assumptions',
        'desc': 'Discuss the appropriateness of model assumptions in ' +
                'the context of the project objectives.'
    },
    'b3_1': {
        'heading': 'B.3 MODEL PARAMETERIZATION AND CALIBRATION',
        'label': 'B.3.1 Model Input Parameters',
        'desc': 'List or describe the model input parameters ' +
                'that are needed for the analysis. '
    },
    'b3_2': {
        'label': 'B.3.2 Data Sources',
        'desc': 'Identify potential data sources of measured/observed ' +
                'values for model parameters that will be obtained ' +
                'from secondary sources.'
    },
    'b3_3': {
        'label': 'B.3.3 Assessment Criteria',
        'desc': 'State the criteria that will be used to assess whether ' +
                'or not the reported data are of sufficient quality.'
    },
    'b3_4': {
        'label': 'B.3.4 Outliers | Missing Data',
        'desc': 'Describe procedures for identifying outliers and ' +
                'handling outliers or missing data (imputation ' +
                'procedures). (See "Requirements for Projects Using ' +
                'Existing Data" for additional guidance.)'
    },
    'b3_5': {
        'label': 'B.3.5 Tools or Algorithms',
        'desc': 'Identify the tools or algorithms that will be used to ' +
                'estimate the parameter values, or model parameters that ' +
                'will be computationally estimated.  '
    },
    'b3_6': {
        'label': 'B.3.6 Rationale',
        'desc': 'Discuss the rationale for using the selected estimation ' +
                'approaches and characterize the range of applicability ' +
                'of these estimation approaches.'
    },
    'b3_7': {
        'label': 'B.3.7 Calibration Dataset ',
        'desc': 'Identify potential sources for a calibration dataset ' +
                'for model parameters that will be estimated ' +
                'through model calibration.  '
    },
    'b3_8': {
        'label': 'B.3.8 Criteria',
        'desc': 'State the criteria that will be used to assess whether ' +
                'or not the dataset is of sufficient quality.  '
    },
    'b3_9': {
        'label': 'B.3.9 Calibration SOPs',
        'desc': 'Describe the calibration procedures (e.g., ' +
                'weighting functions, optimization algorithms, etc.).'
    },
    'b3_10': {
        'label': 'B.3.10 Goodness-of-fit Criteria',
        'desc': 'State the goodness-of-fit criteria for ' +
                'acceptance of the parameter value.'
    },
    'b4_1': {
        'heading': 'B.4 MODEL PERFORMANCE ASSESSMENT',
        'label': 'B.4.1 V&V | IV&V SOPs',
        'desc': 'Describe any procedures that will be used to validate ' +
                'the results of the modeling analysis, e.g. through ' +
                'comparisons of the model predictions against observed ' +
                'data collected in field or laboratory studies.'
    },
    'b4_2': {
        'label': 'B.4.2  V&V | IV&V Source Code',
        'desc': 'Describe any verification procedures that will be used ' +
                'to assess whether these programs are performing as ' +
                'expected, if additional code or scripts are to be ' +
                'developed (e.g., to create model input files, process ' +
                'model output, or couple models together).'
    },
    'b4_3': {
        'label': 'B.4.3 Model Parameter Sensitivity Analysis',
        'desc': 'Describe any procedures that will be used for ' +
                'model parameter sensitivity analysis.'
    },
    'b4_4': {
        'label': 'B.4.4 Parameter Uncertainty',
        'desc': 'Describe any procedures that will be used to evaluate ' +
                'the impact of parameter uncertainty on model results.'
    },
    'b4_5': {
        'label': 'B.4.5 Tuning Parameters | Spatial/Temporal Discretization',
        'desc': 'Describe any procedures that will be used to assess the ' +
                'impact of tuning parameters or spatial/temporal ' +
                'discretization on model results.'
    },
    'b5_1': {
        'heading': 'B.5 INTERPRETATION OF MODEL RESULTS',
        'label': 'B.5.1 Statistical SOPs',
        'desc': 'Describe any statistical procedures that will be used ' +
                'to summarize the model output.  '
    },
    'b5_2': {
        'label': 'B.5.2 Data Transformations',
        'desc': 'Describe any data transformations that will be applied ' +
                'to the model output (e.g., for scaling or bias adjustment)'
    },
    'b6_1': {
        'heading': 'B.6 DOCUMENTATION',
        'label': 'B.6.1 I/O Requirements',
        'desc': 'Specify the requirements for project documentation ' +
                '(e.g., model input/output files; results of model ' +
                'performance assessment; scripts or source code; ' +
                'post-processed model output).'
    },
    'b6_2': {
        'label': 'B.6.2 Amendments to QAPP',
        'desc': 'Identify QAPP elements that may need to be ' +
                'updated as the project moves forward and describe the ' +
                'procedures for QAPP amendment and distribution.'
    }
}

# ########################################################################
# ########################################################################
# ########################################################################

MODEL_DEVELOPMENT = {
    'b1_1': {
        'heading': 'B.1 MODEL DESIGN',
        'label': 'B.1.1 Conceptual Model',
        'desc': 'Describe the conceptual model, including key ' +
                'processes, system compartments, system boundaries, ' +
                'temporal and spatial scales, and fluxes into ' +
                'and out of the problem domain.'
    },
    'b1_2': {
        'label': 'B.1.2 Existing model(s)',
        'desc': 'If the project builds upon a previously developed ' +
                'model, describe the existing model and identify what ' +
                'modifications and enhancements are needed to meet ' +
                'project objectives.'
    },
    'b1_3': {
        'label': 'B.1.3 Model Development Relationship',
        'desc': 'Describe how the model development fits into a larger ' +
                'project and its relationship to related efforts (e.g., ' +
                'field or lab studies, software or application ' +
                'development, etc) with separate QAPPs, if applicable.'
    },
    'b2_1': {
        'heading': 'B.2 MODEL DERIVATION',
        'label': 'B.2.1 Mathematical Representation',
        'desc': 'Describe the mathematical representation of the ' +
                'processes of interest. For mechanistic models, state ' +
                'the governing equation and describe what each term in ' +
                'the equation represents. For empirical/statistical models, ' +
                'identify the attributes that will be considered for ' +
                'inclusion in the model based on their hypothesized ' +
                'effect on the modeled outcome.'
    },
    'b2_2': {
        'label': 'B.2.2 Statistical | Numerical Approaches',
        'desc': 'Describe the statistical and/or numerical approaches ' +
                'that will be used to derive, implement, ' +
                'and parameterize/calibrate the model.'
    },
    'b2_3': {
        'label': 'B.2.3 Empirical | Statistical Models',
        'desc': 'For empirical/statistical models (e.g., regression, ' +
                'classification or clustering), describe the ' +
                'calibration/training dataset that will be used ' +
                'to derive fixed model parameters (e.g., ' +
                'regression coefficients or weights).'
    },
    'b2_4': {
        'label': 'B.2.4 Potential Data Sources',
        'desc': 'Identify potential data sources of measured/observed ' +
        'values. State the criteria that will be used to assess ' +
        'whether or not the reported data are of sufficient ' +
        'quality.  Describe procedures for identifying outliers ' +
        'and handling outliers or missing data (imputation procedures).'
    },
    'b2_5': {
        'label': 'B.2.5 Calibration Procedures',
        'desc': 'Describe the calibration procedures (e.g., weighting ' +
                'functions, optimization algorithms, etc.), and state ' +
                'the goodness-of-fit criteria for acceptance of ' +
                'the model parameter value.'
    },
    'b2_6': {
        'label': 'B.2.6 Numerical Errors Checks',
        'desc': 'For mechanistic models, describe any procedures that ' +
                'will be used to check for numerical errors (e.g., ' +
                'checks for mass balance errors or violations of ' +
                'boundary conditions).'
    },
    'b3_1': {
        'heading': 'B.3 VALIDATION, VERIFICATION, AND TESTING',
        'label': 'B.3.1 Verification Procedures',
        'desc': 'Describe the verification procedures that will be used ' +
        'to assess whether model algorithms are performing as expected.'
    },
    'b3_2': {
        'label': 'B.3.2 Validation Procedures',
        'desc': 'Describe the validation procedures that will be used to ' +
                'assess whether model results are representative ' +
                'of measured or observed data.'
    },
    'b3_3': {
        'label': 'B.3.3 Data Sources',
        'desc': 'Identify potential data sources of measured/observed ' +
                'values. State the criteria that will be used to assess ' +
                'whether or not the reported data are of sufficient quality.'
    },
    'b3_4': {
        'label': 'B.3.4 Outliers | Missing Data',
        'desc': 'Describe procedures for identifying outliers and ' +
                'handling outliers or missing data (imputation procedures).'
    },
    'b3_5': {
        'label': 'B.3.5 Additional Testing',
        'desc': 'Describe any additional testing that will be ' +
                'conducted, e.g., comparison of model accuracy or ' +
                'computational efficiency against existing models.'
    },
    'b3_6': {
        'label': 'B.3.6 SOPs Model Parameter Sensitivity Analysis',
        'desc': 'Describe any procedures that will be used for ' +
                'model parameter sensitivity analysis.'
    },
    'b3_7': {
        'label': 'B.3.7 SOPs Parameter Uncertainty',
        'desc': 'Describe any procedures that will be used to evaluate ' +
                'the impact of parameter uncertainty on model results'
    },
    'b3_8': {
        'label': 'B.3.8 SOPs Tuning Parameters | ' +
                 'Spatial/Temporal Discretization',
        'desc': 'Describe any procedures that will be used to assess ' +
                'the impact of tuning parameters or spatial/temporal ' +
                'discretization on model results.'
    },
    'b3_9': {
        'label': 'B.3.9 Peer Review Process',
        'desc': 'Describe the level of internal and external peer ' +
                'review that is needed for the model.'
    },
    'b4_1': {
        'heading': 'B.4 DOCUMENTATION',
        'label': 'B.4.1 Project Documentation',
        'desc': 'Specify the requirements, format and location ' +
                'for project documentation.'
    },
    'b4_2': {
        'label': 'B.4.2 Calibration Datasets | SOPs',
        'desc': 'Include model development documentation that may ' +
                'include derivations of governing equations and ' +
                'descriptions of calibration datasets and procedures.'
    },
    'b4_3': {
        'label': 'B.4.3 I/O Data',
        'desc': 'Include model performance assessment documentation ' +
                'that may include model input/output files used for ' +
                'verification, verification and testing; and quantitative ' +
                'or qualitative analysis of model performance.'
    },
    'b4_4': {
        'label': 'B.4.4 Source Code SCM',
        'desc': 'Include a description of documentation related to ' +
                'the development of scripts and/or source code to implement ' +
                'the model should specify the programming environment and ' +
                'version used, and identify any code repositories (e.g., ' +
                'Bitbucket and GitHub) used to archive and document coding ' +
                'issues and their resolution. If applicable, see ' +
                '"Requirements for Software and Application Development ' +
                'Projects" for additional QAPP requirements related the ' +
                'development of software applications.'
    },
    'b4_5': {
        'label': 'B.4.5 Disclaimers',
        'desc': 'Describe how model assumptions, constraints and ' +
                'applicability domain will be documented in associated ' +
                'publications and user guidance materials.'
    }
}

# ########################################################################
# ########################################################################
# ########################################################################

SOFTWARE_DEVELOPMENT = {
    'b1_1': {
        'heading': 'B.1 REQUIREMENTS',
        'label': 'B.1.1 Identify Users',
        'desc': 'Identify the users of the software and describe any ' +
                'special user roles or tasks that will be required. ' +
                'Describe the minimum skill-level(s) or qualification(s) ' +
                'that the software user must possess prior to ' +
                'operating/using the software.'
    },
    'b1_2': {
        'label': 'B.1.2 Define Critical Functionality',
        'desc': 'Provide a list and/or graphical representation(s) of the ' +
                'critical functions that the software system implements. ' +
                'Developer should map the key/critical software design ' +
                'requirements to the important performance/operational ' +
                'areas of the software.'
    },
    'b1_3': {
        'label': 'B.1.3 System Requirements',
        'desc': 'Explain and describe the system requirements which ' +
                'implement the software functionality, including external ' +
                'interfaces (e.g., Graphical User Interfaces [GUIs], and ' +
                'operational interfaces, which are used by other software ' +
                'programs, to call subroutines from the main software ' +
                'program, as applicable, etc.), performance requirements, ' +
                'and design constraints. System requirements should ' +
                'consider computer (and external) hardware, Graphical User ' +
                'Interfaces [GUIs], operating system software, interfaces ' +
                'with other software/models/databases, minimum and maximum ' +
                'software functionality, operational performance, network ' +
                'communications, computer security, system access, and ' +
                'software and database backup and recovery.  Each ' +
                'requirement should be uniquely identified, and defined, so ' +
                'that its existence and implementation can be objectively ' +
                'verified and validated (e.g., tested). The term ' +
                '"requirements" encompasses the areas of computer and ' +
                'external hardware Graphical User Interface(s), operating ' +
                'system software, interfaces with other ' +
                'software/models/databases, minimum and maximum software ' +
                'functionality, operational performance, network ' +
                'communications computer security, system access, and ' +
                'software and database back and recovery.'
    },
    'b1_4': {
        'label': 'Performance and Design Constraints',
        'desc': 'Describe any anticipated performance, and design ' +
                'constraints. Explain the factors (controllable or ' +
                'uncontrollable) that influence the design and operational ' +
                'behavior of the software/model. Describe the mitigation ' +
                'strategies chosen to address these performance and design ' +
                'constraints as applicable.'
    },
    'b1_5': {
        'label': 'System Hardware and OS Requirements',
        'desc': 'Specify computer hardware (e.g., computer memory storage ' +
        'requirement, computer hard disk/permanent storage requirements, ' +
        'internal system processor clock speed, number of computer nodes or ' +
        'clusters, etc.) and operating system requirements (e.g., Windows ' +
        '10, MacOS, Linux, Unix, single-threaded or multi-threaded ' +
        'configuration, etc.).'
    },
    'b1_6': {
        'label': 'Requirements Selection',
        'desc': '''Describe the process for the collection of software/model
                   requirements. This includes who will be involved in
                   providing the requirements, (e.g., System Owner, System
                   stakeholders, specific users) and who collects, collates,
                   and documents the software/model requirements. Identify the
                   method for selecting the design requirements for subsequent
                   review, (e.g., Requirements Traceability Matrix [RTM], Jira
                   Requirements Management, etc.). Identify when requirements
                   will be approved by the customer or system owner in the
                   Software Development Life Cycle (SDLC).'''
    },
    'b1_7': {
        'label': 'Naming Convention',
        'desc': '''Describe the naming convention to be used for each
                   software/model design requirement, and how version control
                   (of requirements) will be maintained. Recommend
                   incorporation of this information within a Requirements
                   Traceability Matrix (RTM)).'''
    },
    # ########################################################################
    'b2_1': {
        'heading': 'B.2 SYSTEM DESIGN',
        'label': 'B.2.1 System Design',
        'desc': '''Provide an overview of the system design, including block
                   diagrams displaying relationships between major program
                   modules, hardware devices (e.g., computers, storage systems,
                   external computer-controlled systems, etc.), databases,
                   external applications, tools, and models, and data
                   input/output processes, data rates, and data storage
                   requirements.'''
    },
    'b2_2': {
        'label': 'B.2.2 Components and Subcomponents',
        'desc': '''Describe the components and subcomponents of the software
                   design, including databases, tools, interfaces to external
                   hardware and software, and internal interfaces
                   (including GUIs). The description should link the software
                   structure to the functional requirements.'''
    },
    'b2_3': {
        'label': 'B.2.3 Rationale of Hardware/Software',
        'desc': '''Provides the rationale for selecting the proposed hardware,
                   software tools, and databases as explained and described in
                   the systems requirement document, systems design document,
                   scope of work (SOW), performance work statement (PWS),
                   workplan, etc., as applicable.
                   An example rationale for selecting an RTM:
                   A Requirements Traceability Matrix (RTM) is used to trace
                   all Functional Requirements (FRs) back to system
                   objectives, to ensure all System Design (SD) elements are
                   included.
                   Changes at this stage should produce an amendment or update
                   to the QAPP. Evaluation of the FRs, and the relationships
                   between requirements, and the checks for correctness,
                   consistency, completeness, accuracy, readability, and
                   testability, should occur after this phase is completed.
                   Developer should assess how well the FRs satisfy the
                   System Design (SD) objectives.'''
    },
    # ########################################################################
    'b3_1': {
        'heading': 'B.3 SYSTEM DOCUMENTATION',
        'label': 'B.3.1 Documentation Requirements',
        'desc': '''Specify the requirements for documentation of, the methods,
                   processes, and facilities used to maintain, store, secure,
                   and preserve the document-controlled versions, and related
                   artifacts of, the product software during all phases of the
                   software development life cycle (e.g., requirements
                   documents, design documents, configuration management plans,
                   test plans,  operations manuals, software source code (for
                   models, tools, database, applications [e.g., Application
                   Programming Interfaces (APIs)], etc.), and user's guides.'''
    },
    'b3_2': {
        'label': 'B.3.2 Software and Hardware Documentation',
        'desc': '''Describes the procedures for controlling, documenting, and
                   archiving all changes to software and hardware. Describes
                   the use of software configuration management, software
                   version control, code repository management, and product
                   release management (e.g., BitBucket, GitHub, etc.).'''
    },
    'b3_3': {
        'label': 'B.3.3 Software Configuration Management (SCM)',
        'desc': '''Identifies the software used to archive, control, document,
                   save, and recover changes made to the system software
                   source code. GitHub, Bitbucket, and ORD Application
                   Inventory used to track Open Source Software (OSS).'''
    },
    # ########################################################################
    'b4_1': {
        'heading': 'B.4 CODING AND IMPLEMENTATION',
        'label': 'B.4.1 Development Process',
        'desc': '''Describe how the operational software system is developed
                   from the design specifications. Explains and describes the
                   rational for using ether the sequential/waterfall software
                   development model or the Agile/spiral software development
                   model.
                   *For Agile, developers must clearly document project
                   concepts and prioritize initial development environment and
                   associated requirements. Developers must identify team
                   members and contributors to the project.'''
    },
    'b4_2': {
        'label': 'B.4.2 Testing Process',
        'desc': '''Describes how the requirements for functionality, external
                   interfaces, performance, and design constraints will be
                   tested, verified, and validated (e.g., describes the testing
                   regime for the software [unit test, component test, software
                   integration test, system test, quality assurance/quality
                   control test, user acceptance test (UAT), etc.]).'''
    },
    'b4_3': {
        'label': 'B.4.3 Software Versioning, Release, and Delivery',
        'desc': '''Describes the software versioning, release, and delivery
                   process and how it is managed, including software versions
                   for alpha and beta testing, user acceptance testing (UAT),
                   and training materials, including user manuals.'''
    },
    'b4_4': {
        'label': 'B.4.4 Software Operational Scenarios',
        'desc': '''Describe how the model will be applied in different
                   operational situations, and details the required model
                   inputs (provide detailed information on the data input
                   format[s] and the external interfaces that feed into the
                   model) and outputs (provide detailed information on the
                   model output format[s] and the external interfaces that
                   the model feeds into). Explains the required operational
                   conditions that must be present to apply the model, and
                   notes that the steps required to achieve the required setup
                   to apply the model will be fully documented in a user
                   manual, test procedure, and/or operations manual for the
                   model/software. Applicable to models, databases, tools,
                   and application programming interfaces (APIs).'''
    },
    # ########################################################################
    'b5_1': {
        'heading': 'B.5 VERIFICATION AND VALIDATION',
        'label': 'B.5.1 Testing Strategy',
        'desc': '''Describe the testing strategy that will be used, along with
                   the procedures for each planned test. These tests can
                   include routines that assess the operation of the software,
                   including processing of inputs, format of outputs, testing
                   of module/function internal logic/algorithms, etc.,
                   validation, and verification of the software functions.
                   Testing may include, but is not limited to, individual
                   module tests, integration tests, system testing, user
                   acceptance testing, and alpha, and beta testing, etc.
                   Verification: The process of determining whether the
                   products of a given stage of the software development life
                   cycle fulfills the requirements established during the
                   previous stage.
                   Validation: The process of evaluating software at the end of
                   the software development process (acceptance testing
                   activity in the testing stage) to ensure compliance with
                   software requirements.'''
    },
    'b5_2': {
        'label': 'B.5.2 Review Process',
        'desc': '''Describe the review process for the software's Graphical
                   User Interface (GUI) and output reports. Ensures that
                   document summary or synthesis statements accurately
                   represent the underlying data used/processed, and its
                   limitations.  System documents check for, and provide
                   correct interpretation of results, promote clarity of
                   discussion, contain appropriate citations and references,
                   and has correct spelling and grammar.'''
    },
    'b5_3': {
        'label': 'B.5.3 Results Validation',
        'desc': '''Describes the procedures for checking the correctness of
                   software outputs and the validity checks for the format(s)
                   of model inputs, e.g., checks that input parameters are
                   within the acceptable range of values, and/or are consistent
                   and applicable, given the subject area (scientific domain)
                   of the model.'''
    },
    'b5_4': {
        'label': 'B.5.4 Agency Conformity',
        'desc': '''Describes how the developed software product conforms to
                   customer and Agency requirements, and whether the software
                   product fulfills its intended use, and user expectations.
                   This includes analysis, evaluation, review, inspection,
                   assessment, and testing of the software product, and the
                   processes used to produce the software product, and its
                   associated documentation.'''
    },
    'b5_5': {
        'label': 'B.5.5 Acceptable Failure Rate',
        'desc': '''For each type of testing conducted, identifies the
                   acceptable overall maximum failure rate (e.g., 5%), to
                   proceed with software/model production. Describe how the
                   failure rate will be calculated. Identify the testers for
                   each test, and what qualifies them as a tester. Identify
                   the individual(s) responsible for signing off on testing
                   results (i.e., table displayed below provides a template.).
                   Describe what will occur if the failure rate is
                   unacceptable.'''
    },
    # ########################################################################
    'b6_1': {
        'heading': 'MAINTENANCE AND USER SUPPORT',
        'label': 'B.6.1 Post-Release Maintenance',
        'desc': '''Describe the procedures for maintenance and user support
                   when the software or data generated by the project is
                   distributed or deployed outside of the ORD center that
                   initiated the development of the software product. Project
                   Document(s), including the software source code header for
                   each code module, must clearly state that EPA owns the
                   operational software, its source code, object code,
                   databases, and documents, etc., with unlimited rights to
                   its use,  transfer, and final disposition.'''
    },
    'b6_2': {
        'label': 'B.6.2 User Access and Training',
        'desc': '''Describe how user will be granted access to the system
                   and any training required.'''
    },
    'b6_3': {
        'label': 'B.6.3 Training Material and User Guides',
        'desc': '''Describe type of training materials/user manuals/system
                   guides that will be developed. Identify who will develop
                   them, and how they will be delivered or made
                   accessible to the users.'''
    }
}

# ########################################################################
# ########################################################################
# ########################################################################

SECTION_B_INFO = {
    "Existing Data": EXISTING_DATA,
    "Software Development": SOFTWARE_DEVELOPMENT,
    "Model Development": MODEL_DEVELOPMENT,
    "Model Application": MODEL_APPLICATION,
    "Measurements": MEASUREMENTS_AND_MONITORING,
    "Analytical Methods": ANALYTICAL_METHODS,
    # "Cell Culture Models": CELL_CULTURE_METHODS,
    "Animal Cell Studies": ANIMAL_CELL
}
