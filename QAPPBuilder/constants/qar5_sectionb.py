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
        'desc': '''Describe how data will be stored, shared, and secured.'''
    },
    'b3_3': {
        'label': 'B.3.3 Special Access/Storage Requirements',
        'desc': '''Describe if existing data contains CBI or PII and address
                   special agreements, special access certifications and
                   storage requirements that apply.'''
    },
    'b3_4': {
        'label': 'B.3.4 Metadata Storage',
        'desc': '''How and where will metadata be recorded? (i.e., data
                   source, originating organization, report title,
                   type of information).'''
    },
    'b3_5': {
        'label': 'B.3.5 Translation Procedure(s)',
        'desc': '''Describe procedures used to ensure that errors in
                   translation are minimized.'''
    },
    'b3_6': {
        'label': 'B.3.6 Data Access Management',
        'desc': '''Describe measures taken to prevent unauthorized or
                   accidental editing of data, such as version control
                   procedures and internal database audit logs.'''
    },
    'b3_7': {
        'label': 'B.3.7 Original Data Integrity',
        'desc': '''Describe procedures used to ensure that existing data
                   maintain their original integrity and quality as they are
                   migrated into current project.'''
    },

    'b4_1': {
        'heading': 'B.4 DATA VERIFICATION AND VALIDATION',
        'label': 'B.4.1 IV&V',
        'desc': '''Describe the extent in which there has been independent
                   verification or validation of the data set or study method
                   and result.'''
    },
    'b4_2': {
        'label': 'B.4.2 IV&V Results',
        'desc': '''Describe where results of the independent reviews of the
                   data set are documented.'''
    },
    'b4_3': {
        'label': 'B.4.3 IV&V Corrective Action',
        'desc': '''Describe how the corrective action process of the
                   independent reviews of the data sets occur and how these
                   corrective actions are documented.'''
    },
    'b4_4': {
        'label': 'B.4.4 Mathematical/Statistical Procedures',
        'desc': '''Discuss any mathematical or statistical procedures (such
                   as outlier analyses or goodness-of-fit tests) that will
                   identify whether individual data values within existing
                   data sets should be rejected, transformed, or otherwise
                   qualified before any statistical analysis.'''
    },
    'b4_5': {
        'label': 'B.4.5 Data Validation Procedures',
        'desc': '''Describe any data validation procedures to be applied to
                   the existing data to ensure the use of accurate and
                   representative project data that are fit-for-purpose
                   in addressing the research question.'''
    },
    'b4_6': {
        'label': 'B.4.6 Cross-Validation',
        'desc': '''Describe if any cross validation is used. Cross-validation
                   is a resampling procedure that is a useful technique when
                   the goal is either model prediction accuracy (minimizing
                   prediction error) or determining the right model for
                   interpretation.  For example: cross validation can be used
                   to evaluate the accuracy of models on a limited data
                   sample.'''
    },
}

# ########################################################################
# ########################################################################
# ########################################################################

MEASUREMENTS_AND_MONITORING = {
    'b1_1': {
        'heading': 'B.1 PROJECT DESIGN',
        'label': 'B.1.1 Experimental Design',
        'desc': '''Describe experimental design to generate the. data needed to
                   meet the research objectives. A description of the design
                   should include the rationale for the design, sample types
                   and number of samples required.'''
    },
    'b1_2': {
        'label': 'B.1.2 Analytes of Interest',
        'desc': '''Identify the specific analyte(s) of interest and the
                   matrix/matrices. Identify any required method detection
                   limits, reporting limits or critical thresholds (e.g.
                   screening levels, maximum contaminant level (MCL)) for
                   each analyte.'''
    },
    'b1_3': {
        'label': 'B.1.3 Limitations and Challenges',
        'desc': '''Describe any limitations or special challenges that are
                   anticipated and plans to mitigate those
                   limitations/challenges (e.g. matrix interferences, sample
                   homogeneity, representativeness, completeness, site
                   access, etc.).'''
    },
    # ############################################
    'b2_1': {
        'heading': 'B.2 FIELD COLLECTION',
        'label': 'B.2.1 Sampling Locations and Frequency',
        'desc': '''Identify sampling locations, type of sample collection,
                   and frequency. If locations are not predetermined, describe
                   the process and criteria for site selection.'''
    },
    'b2_2': {
        'label': 'B.2.2 Field Sampling Design',
        'desc': '''Describe the field sampling design used to generate the
                   data needed to meet the research objectives and the steps
                   taken to assure that representative samples are collected
                   (e.g. minimum sample amount for analysis, sample
                   accessories, homogenization, holding times, containers
                   types, preservation, quenching agents, contingency plans,
                   etc.)'''
    },
    'b2_3': {
        'label': 'B.2.3 Labeling, Packing, and Shipping',
        'desc': '''Describe procedures for labeling, packing, and shipping
                   field samples, and provisions for maintaining
                   chain-of-custody, as applicable. (See Appendix B for
                   example chain of custody.).'''
    },
    'b2_4': {
        'label': 'B.2.4 Field Records',
        'desc': '''Describe the use of project specific field records that
                   provide objective evidence of actions taken and observations
                   made. Examples of field records include (but not limited
                   to): field logbook entries, field collection forms, field
                   measurement data log, chain of custody forms, photographs,
                   maps, field inspection forms, etc. (See EPA QA Field
                   Activities Procedure for more details.)'''
    },
    'b2_5': {
        'label': 'B.2.5 Field Equipment Use',
        'desc': '''Describe the procedures for field equipment use (e.g.
                   decontamination, calibration, storage etc.) and sample
                   collection. Reference SOPs or methods used where applicable.
                   This information may be summarized in a table
                   (See Appendix A, also see EPA QA Field Activities Procedure
                   for more details.)'''
    },
    # ############################################
    'b3_1': {
        'heading': 'B.3 MEASUREMENT PROCEDURES',
        'label': 'B.3.1 Field Analysis Methods and Instrumentation',
        'desc': '''For field measurements/analyses (including in-line
                   measurements), reference (e.g. SOP, method) each field
                   sample analysis method and instrumentation to be used.
                   This information may be summarized in a table (see Appendix
                   A for examples). If SOPs/methods will not be developed or
                   are not currently available, describe in detail the
                   procedural steps including steps for standard/reagent
                   preparation, sample preparation, sample analysis,
                   quality control, and documentation of results.'''
    },
    'b3_2': {
        'label': 'B.3.2 Laboratory Analysis Methods and Instrumentation',
        'desc': '''For laboratory measurements/analyses, describe in detail or
                   reference (e.g. SOP, method) each sample analysis method
                   and instrumentation to be used. If SOPs/methods will not
                   be developed or are not currently available, describe in
                   detail the procedural steps including steps for
                   standard/reagent preparation, sample preparation, sample
                   analysis, quality control, and documentation of results.
                   This information may be summarized in a table (see Appendix
                   A for examples).'''
    },
    'b3_3': {
        'label': 'B.3.3 Logging',
        'desc': '''Identify any sample logs, bench sheets, prep logs, analysis
                   logs, etc., used, the format (e.g., paper or electronic)
                   and where they are maintained.'''
    },
    # ############################################
    'b4_1': {
        'heading': 'B.4 METHOD PERFORMANCE METRICS',
        'label': 'B.4.1 QA Procedures',
        'desc': '''Include or reference specific calibration quality control
                   procedures, including tuning, instrument performance checks,
                   linearity checks, initial and continuing calibration checks,
                   determination of detection limits.'''
    },
    'b4_2': {
        'label': 'B.4.2 QC Corrective Actions',
        'desc': '''Describe the type, frequency, acceptance criteria and
                   corrective actions to be taken of each experimental QC
                   samples (field and/or lab). This information may be
                   summarized in a table (see Appendix A for examples) It is
                   recommended, if possible, that controls for bias and
                   precision should be considered (e.g. blanks, replicates,
                   spikes) at a minimum (see Appendix C for examples).'''
    },
    'b4_3': {
        'label': 'B.4.3 Supply and Consumable QA',
        'desc': '''Describe or any special procedures (or reference a SOP)
                   to verify the quality, cleanliness, integrity, etc.
                   of supplies and consumables.'''
    },
    # ############################################
    'b5_1': {
        'heading': 'B.5 DATA REVIEW, VERIFICATION, and VALIDATION',
        'b5_1_1': {
            'heading': 'B.5.1 DATA REPORT PACKAGES',
            'label': '''B.5.1.1 Internal Data Packages''',
            'desc': '''For Internal Data packages: Itemize the
                       information and records which must be included and
                       specify the reporting format for hard copy and
                       electronic forms. See Appendix D, Table D1 for
                       example records.'''
        },
        'b5_1_2': {
            'label': 'B.5.1.2 External Data Packages',
            'desc': '''For External Data Packages: Itemize the information
                       and records which must be included in the external data
                       report and specify the reporting format for hard copy
                       and any electronic forms. See Appendix D, Table D1 for
                       records that may be included. Researcher should consult
                       customer (e.g., Regions, States, Tribes, Municipalities,
                       etc.) on what to include in the external data report.'''
        },
        # #######################
        'b5_2_1': {
            'heading': 'B.5.2 DATA REVIEW PACKAGES',
            'label': 'B.5.2.1 Data Review Personnel',
            'desc': '''Identify who is responsible for reviewing the data.
                       If multiple people are involved, a table can be created
                       to show who is responsible for each analysis.'''
        },
        'b5_2_2': {
            'label': 'B.5.2.2 Initial and Secondary Reviewers',
            'desc': '''It is required that the analyst conduct an initial
                       review of the data including QC checks. It is
                       recommended that a secondary reviewer check a subset
                       of the data. See Appendix E for definitions.'''
        },
        'b5_2_3': {
            'label': 'B.5.2.3 Data Review Definition',
            'desc': '''Describe what data will be reviewed and the frequency
                       of the review(s).'''
        },
        'b5_2_4': {
            'label': 'B.5.2.4 Data Review Process',
            'desc': '''Describe the process for conducting data reviews
                       including the percentage of data reviewed.'''
        },
        'b5_2_5': {
            'label': 'B.5.2.5 Data Review Documentation',
            'desc': '''Describe how the reviews will be documented. Provide
                       examples of any forms or checklists to be used for
                       the reviewing process.'''
        },
        'b5_2_6': {
            'label': 'B.5.2.6 Issue Resolution Procedure',
            'desc': '''Identify issue resolution procedure and responsible
                       individuals.'''
        },
        'b5_2_7': {
            'label': 'B.5.2.7 Data Acceptance Criteria',
            'desc': '''State criteria for accepting, rejecting, or qualifying
                       data. Identify how rejected or qualified data will be
                       annotated. If qualifiers are used, provide definitions
                       of the qualifiers.'''
        },
        'b5_2_8': {
            'label': 'B.5.2.8 Calculations/Algorithms',
            'desc': '''Include project-specific calculations or algorithms.
                       (May be discussed in SOP).'''
        },
    },
    # ############################################
    'b6_1': {
        'heading': 'B.6 DATA ANALYTICS',
        'label': 'B.6.1 Data Analysis Technique(s)',
        'desc': '''Describe how the data will be summarized or analyzed (e.g.,
                   qualitative analysis, descriptive or inferential statistics)
                   to meet the project objective(s) and why the technique(s)
                   were selected.'''
    },
    'b6_2': {
        'label': 'B.6.2 Inputs and Processing Procedure(s)',
        'desc': '''Identify what inputs are needed and what statistical
                   programs will be used. Describe any procedures that will be
                   used to compile or minimize the data prior to data analyses
                   (e.g. exclusion of outliers, handling of qualified data,
                   handling of data reported as qualitative values [i.e. <MRL],
                   range of inclusion).'''
    },
    'b6_3': {
        'label': 'B.6.3 Descriptive Statistics',
        'desc': '''If descriptive statistics are proposed, state what
                   statistics (e.g., mean, median, standard error, minimum and
                   maximum values) will be used to summarize or visualize the
                   data. Identify the criteria used to make decisions
                   (confidence interval, coefficient of determination, test
                   of independence, etc.)'''
    },
    'b6_4': {
        'label': 'B.6.4 Inferential Method',
        'desc': '''If an inferential method is proposed, indicate whether
                   the method will be a hypothesis test, confidence interval,
                   or confidence limit. Describe how the method will be
                   performed and identify any critical thresholds or criteria
                   that will be used to make decisions or draw conclusions.'''
    },
    'b6_5': {
        'label': 'B.6.5 Post Data Analytics Review(s)',
        'desc': '''Describe any reviews to be conducted of post data analytics
                   outputs (i.e. charts, graphs, statistics) including who
                   is responsible, what will be reviewed, and how these reviews
                   will be documented. Provide examples of any forms or
                   checklists to be used for the reviewing process.'''
    },
}

# ########################################################################
# ########################################################################
# ########################################################################

# TODO: Make sure all references to this template are removed:
# MODEL_DEVELOPMENT

# ########################################################################
# ########################################################################
# ########################################################################

MODEL_APPLICATION = {
    'b1_1': {
        'heading': 'B.1 MODEL SPECIFICATION',
        'label': 'B.1.1 Computational Model Description',
        'desc': '''Describes the computational (computer-based) model being
                   developed, applied, and used, including but not limited to,
                   the underlying scientific assumptions of the model, the key
                   processes being simulated/implemented by the model, the
                   critical pathways and processes being implemented in the
                   model, and the environmental and system boundaries of the
                   model.'''
    },
    'b1_2': {
        'label': 'B.1.2 Model Integration',
        'desc': '''Describes how the model/modeling tool fits into a larger
                   research project, and its relationship to other research
                   efforts that may have separate QAPPs (if applicable).
                   Describes how the model (or models) supports the project
                   objectives of the other research projects is related to.
                   Include, by reference, other QAPPs if there is a
                   relationship to related research efforts (e.g., field or
                   lab studies, software/model development, or model
                   application, etc.).'''
    },
    # #####################################
    'b2_1': {
        'heading': 'B.2 MODEL SELECTION',
        'label': 'B.2.1 Model Functionality Requirements',
        'desc': '''Identifies requirements for:
                   • (computer) model functionality, e.g., input formats, types,
                     and applicable values/ranges;
                   • other models/systems that submit inputs into the model,
                   • speed of model operation/processes,
                   • required accuracy of model inputs, output formats, types,
                     and applicable ranges/values,
                   • required accuracy of model outputs,
                   • time required to initiate model operation/run-time,
                   • time required for each model operational cycle and/or time
                     required to stop model operation/run-time,
                   • other models/systems that the model submits its outputs
                     into, etc.
                   Depending on which model or scope of model application,
                   some of the above questions may not apply or you may not
                   yet know.  See section B6 for additional guidance.
                '''
    },
    'b2_2': {
        'label': 'B.2.2 Hardware and OS Requirements',
        'desc': '''Specifies computer hardware and operating system
                   requirements necessary to run the model, (e.g., hard disk
                   size, internal operating system required [e.g., Linux,
                   MacOS, Windows 10, etc.], computer operating system "word"
                   size [e.g., 32-bit, 64-bit, etc.], memory size, internal
                   processor clock speed, etc.).'''
    },
    'b2_3': {
        'label': 'B.2.3 Source Code Compilation',
        'desc': '''If the model is required to convert its source code into
                   virtual machine code, assembly code or other low-level code
                   (i.e., compilers), QAPP describes how this process is
                   implemented and provide an appropriate diagram for the
                   model.
                   If applicable, the QAPP should state where the compiler
                   options influence how the model will be developed, applied
                   and evaluation, the source code will specify (or comment)
                   which compiler settings are used and how this influences
                   the code.'''
    },
    'b2_4': {
        'label': 'B.2.4 Multi-Model Integration',
        'desc': '''If applicable, employs more than one model loosely coupled
                   together (i.e., the output from one or more models serving
                   as input to another model). Provide a written overview of
                   the system design, including a system diagram, and a
                   diagram displaying the transfer of data between models
                   (eg., WRF integration with CMAQ).
                   For projects that involve model integration (e.g.,
                   embedding one model within another or tight coupling of two
                   or more models, and/or sequentially linking models) or use
                   of different model algorithms, provides a written
                   description of the relationships/interactions along with
                   applicable process/system diagrams.'''
    },
    'b2_5': {
        'label': 'B.2.5 Assumptions and Constraints',
        'desc': '''Describes how model assumptions, constraints, and applicable
                   model domain affects the model outputs or results
                   (eg., how are inputs processed).'''
    },
    # #####################################
    'b3_1': {
        'heading': 'B.3 DATA SELECTION AND VALIDATION',
        'label': 'B.3.1 Data/IO Validation',
        'desc': '''For models that require validation of input, output, and/or
                   internal database/data values, QAPP lists, or describes
                   the model input, internal, and/or output parameters
                   required for the analysis. Also, describes any parameter
                   estimation methods (if applicable). QAPP provides
                   information on metadata standards used for data inputs
                   into and data outputs from the model. QAPP provides
                   information on any Software Data Management Plan (SDMP)
                   developed for the model and its associated data. QAPP
                   provides plans or process for making data publicly
                   available (if applicable). '''
    },
    'b3_2': {
        'label': 'B.3.2 Model I/O Parameters',
        'desc': '''Models that require validation, list, or describe the model
                   input or output parameters needed for the analysis.
                   Also, please describe any parameter estimation methods
                   (if applicable).'''
    },
    'b3_3': {
        'label': 'B.3.3 Measured/Observed Data',
        'desc': '''Identifies and specifies potential sources of
                   measured/observed data values for model parameters that are
                   obtained from secondary sources (i.e., sources external to
                   the model) or derived data (eg., output data used as input
                   data).'''
    },
    'b3_4': {
        'label': 'B.3.4 Outliers',
        'desc': '''Describes procedures for identifying input, internal,
                   and/or output data outliers and the process(es) for
                   handling outliers or missing data ([missing] data
                   imputation procedures). Based upon what you defined for
                   Section B2, state how you will ensure you meet this
                   specification, stay within a certain range or limitations?
                   (See “Requirements for Projects Using Existing Data” for
                   additional guidance [provide document designation/number
                   and data or remove this reference].)'''
    },
    'b3_5': {
        'label': 'B.3.5 Parameter Estimates',
        'desc': '''Identifies the process(es) that will be used to estimate
                   the parameter values or model parameters that will be
                   computationally calculated.'''
    },
    'b3_6': {
        'label': 'B.3.6 Estimation Approaches',
        'desc': '''Discusses the rationale (or justification) for using the
                   selected estimation approaches and characterize the range
                   of applicability of these estimation approaches.'''
    },
    'b3_7': {
        'label': 'B.3.7 Data Sources',
        'desc': '''If applicable, identifies the potential sources of data
                   that are used to assess the model output.'''
    },
    'b3_8': {
        'label': 'B.3.8 Measured/Observed Data Sources',
        'desc': '''Identifies measured/observed data sources that will be
                   used to validate the model output. Indicates the criteria
                   that will be used to access whether the output results or
                   the data sets meet the written data quality objectives
                   (DQOs). Describes procedures for identifying and handling
                   data outliers or missing data. State why you decided to
                   use this data/dataset.'''
    },
    'b3_9': {
        'label': 'B.3.9 Validation Procedures',
        'desc': '''Describes the validation procedures to determine if the
                   model output is appropriate (review or post process the
                   output data). Examples include  weighting functions,
                   optimization algorithms, etc.
                   Describes how are the model outputs post-processed to
                   provide data that can be validated and/or analyzed?
                   Example of post-process of model outputs could include be
                   so it can be used for data analysis (i.e., SAS, R, Python,
                   Excel), to fit a certain format or fit into
                   another model.'''
    },
    'b3_10': {
        'label': 'B.3.10 Model Output Acceptance',
        'desc': '''States the statistical "goodness-of-fit" criteria for
                   acceptance of the model output.'''
    },
    # #####################################
    'b4_1': {
        'heading': 'B.4 MODEL PERFORMANCE ASSESSMENT AND VALIDATION',
        'label': 'B.4.1 Results Review and Assessment',
        'desc': '''Describes the procedures that will be used to review and
                   assess the results of the modeling analysis, e.g., through
                   comparisons of the model predictions against observed data
                   collected in field or laboratory studies, output for other
                   models, data from other known datasets, etc.
                   Example: We will derive heat index from the WRF output
                   using XXX algorithm (reference), and we will compare it to
                   heat index derived from observational data taken from
                   /source/ and computed with the same algorithm.'''
    },
    'b4_2': {
        'label': 'B.4.2  Assessment with Expected Results',
        'desc': '''Describes any procedures that will be used to assess whether
                   these model assessment programs are
                   performing as expected.'''
    },
    'b4_3': {
        'label': 'B.4.3 Additional Code/Files',
        'desc': '''Provides a listing(s) of any additional build code, make
                   files, test code, validation code, or scripts that are
                   developed to create the model, its associated model input
                   files, process the model output, or couple multiple models
                   together.'''
    },
    'b4_4': {
        'label': 'B.4.4 Version Control',
        'desc': '''Describes how version control will be implemented for
                   build code, make files, test code, validation code, or
                   scripts, including the file locations and the version
                   control process being used (e.g., Bitbucket, GitHub/Jira,
                   or other management software), and the SOPs that implement
                   the use of these software version control processes.'''
    },
    'b4_5': {
        'label': 'B.4.5 Parameter Sensitivity Analysis',
        'desc': '''Describes and documents the procedures used to accomplish
                   model (output) parameter sensitivity analysis, and/or how
                   the issues of errant values and/or excursions beyond
                   expected range values are addressed in the model output
                   (analysis) runs.'''
    },
    'b4_6': {
        'label': 'B.4.6 Parameter Uncertainty',
        'desc': '''Describes the procedures used to evaluate the impact of
                   model parameter uncertainty on model (output) results
                   and/or what level of uncertainty is acceptable for the
                   model analysis.'''
    },
    'b4_7': {
        'label': 'B.4.7 Tuning Parameters | Spatial/Temporal Discretization',
        'desc': '''Describe the procedures used to assess the impact of
                   adjusting the values of model variables or spatial/temporal
                   discretization on model results.  Example: simulation fails
                   or error alerts.'''
    },
    'b4_8': {
        'label': 'B.4.8 Model Output Evaluation',
        'desc': '''Describe model output evaluation procedures, including
                   but not limited to: comparing measured results, datasets,
                   and other available models, assessment of previous
                   applications of the model, and any validation/verification
                   activities.'''
    },
    # #####################################
    'b5_1': {
        'heading': 'B.5 INTERPRETATION OF MODEL RESULTS',
        'label': 'B.5.1 SOPs',
        'desc': '''Describes any procedures that are used to summarize the
                   model output (e.g., statistical analysis, graphical
                   analysis, etc.)'''
    },
    'b5_2': {
        'label': 'B.5.2 Data Transformations',
        'desc': '''Describes the data transformations that are applied to
                   the model output (e.g., to adjust for scaling, bias,
                   location, time, etc.)'''
    },
    # #####################################
    'b6_1': {
        'heading': 'B.6 DOCUMENTATION',
        'label': 'B.6.1 I/O Requirements',
        'desc': '''Provides location of relevant model files and documents
                   (e.g., model input/output files and databases/datasets;
                   results of model performance assessment; scripts or source
                   code; post-processed model output, design documents,
                   test documents, user/operational manuals, etc. ).'''
    },
    'b6_2': {
        'label': 'B.6.2 SCM',
        'desc': '''Describes how the code repositories used to develop the
                   model (e.g., Bitbucket, GitHub/Jira, etc.) are organized
                   and implemented in the software development environment
                    and the operational software (production) environment.'''
    },
    'b6_3': {
        'label': 'B.6.3 Amendments to QAPP',
        'desc': '''Identifies QAPP elements that may need to be updated,
                   and where information will be documented, as the project
                   evolves and new data or methods are identified. Describes
                   the procedures for QAPP amendment and the QAPP
                   distribution.'''
    }
}

# ########################################################################
# ########################################################################
# ########################################################################

# Social Science/Qualitative Studies
SOC_SCI = {
    'b1_1': {
        'heading': 'B.1 EXPERIMENTAL DESIGN',
        'label': 'B.1.1 Approaches and Perspectives',
        'desc': '''Describe the approaches or perspectives used or
                   assessed in the project including:
                   - interviews (open, semi-structured or structured)
                   - observer or participant observer (overt or covert)
                   - focus groups, enabling/elicitation techniques
                   - self-reports (diaries, surveys)'''
    },
    'b1_2': {
        'label': 'B.1.2 Planned Events',
        'desc': '''Describe any events that will be held to support data
                   collection for the project.'''
    },
    'b1_3': {
        'label': 'B.1.3 Research Objectives',
        'desc': '''Discuss how approaches and events will address research
                   objectives.'''
    },
    'b1_4': {
        'label': 'B.1.4 Sampling Design',
        'desc': '''Describe the sampling design that will be used (i.e.,
                   purposive, quota, snowball etc.) and why it was chosen.'''
    },
    # ###############################
    'b2_1': {
        'heading': 'B.2 DATA COLLECTION',
        'label': 'B.2.1 Data Collection Details',
        'desc': '''Describe the data collection methods in detail: locations,
                   time of year, responsibilities of participants, interview
                   or discussion guides. Be explicit.'''
    },
    'b2_2': {
        'label': 'B.2.2 Types of Observations/Data',
        'desc': '''Describe the types of observations/data that will be
                   collected, and the criteria used for categorical
                   observations.'''
    },
    'b2_3': {
        'label': 'B.2.3 Materials for Participants',
        'desc': '''Describe all materials that will be distributed to
                   participants in the course of the project.'''
    },
    'b2_4': {
        'label': 'B.2.4 Materials Bias Minimization',
        'desc': '''Describe how project materials will be presented (i.e.
                   scripts) and distributed to participants to minimize
                   bias.'''
    },
    'b2_5': {
        'label': 'B.2.5 Data Collection Preparation',
        'desc': '''Describe the preparation for data collection events and
                   how termination of data collection will be decided
                   (saturation, time limit, resources)'''
    },
    'b2_6': {
        'label': 'B.2.6 Confidentiality',
        'desc': '''Describe how confidentiality will be maintained for the
                   chosen data collection method.'''
    },
    'b2_7': {
        'label': 'B.2.7 Information Collection and Documentation',
        'desc': '''Describe the information to be collected in field notes
                   and the medium used for documentation (i.e. data sheets,
                   field notebooks, iPads,).'''
    },
    'b2_8': {
        'label': 'B.2.8 Standard Coding',
        'desc': '''Describe any standard coding that will be used in
                   thematic analysis of responses.'''
    },
    'b2_9': {
        'label': 'B.2.9 Non-direct Measures',
        'desc': '''Describe any non-direct measures (literature searches,
                   databases, etc) that will be utilized including criteria
                   and limitations for use.'''
    },
    'b2_10': {
        'label': 'B.2.10 Functional Criteria for A/V Equipment',
        'desc': '''Provide functional criteria and checks for any audio and/or
                   visual recording equipment used to document activities or
                   otherwise collect data and steps to be taken if audio
                   equipment fails.'''
    },
    # ###############################
    'b3_1': {
        'heading': 'B.3 DATA INTEGRITY',
        'label': 'B.3.1 Electronic Data Documentation and Preservation',
        'desc': '''Describe procedures for documenting and preserving
                   electronic and/or hard copy data gathered at an event.'''
    },
    'b3_2': {
        'label': 'B.3.2 Recordings Integrity',
        'desc': '''Describe steps to ensure the integrity of all recordings.'''
    },
    'b3_3': {
        'label': 'B.3.3 Recording Transcript Accuracy Verification',
        'desc': '''Describe how the accuracy of any recording transcripts
                   will be verified.'''
    },
    'b3_4': {
        'label': 'B.3.4 Traceability',
        'desc': '''Describe steps to be taken to ensure traceability of
                   field notes, video-audio recordings, computer files.'''
    },
    'b3_5': {
        'label': 'B.3.5 Sampling Bias',
        'desc': '''Describe steps to be taken to address the potential
                   for bias in sampling methods.'''
    },
    'b3_6': {
        'label': 'B.3.6 Incomplete Data',
        'desc': '''Describe how incomplete data will be evaluated
                   (i.e participant knows little about topic or incomplete
                   interviews).'''
    },
    # ###############################
    'b4_1': {
        'heading': 'B.4 DATA MANAGEMENT AND ANALYSIS',
        'label': 'B.4.1 Field Note Expanding/Decoding',
        'desc': '''Describe the process and time-frame for expanding/decoding
                   the field notes.'''
    },
    'b4_2': {
        'label': 'B.4.2 Field Note Identification',
        'desc': '''Describe the identification scheme that will be used to
                   link the field notes with the expanded version.'''
    },
    'b4_3': {
        'label': 'B.4.3 Types of Analysis',
        'desc': '''Describe the type of analysis that will be performed
                   (narrative analysis, interpretive phenomenological
                   analysis, thematic analysis, etc.).'''
    },
    'b4_4': {
        'label': 'B.4.4 Outliers, Goodness-of-fit, and Transformations',
        'desc': '''Describe any procedures that will be used to identify
                   outliers, goodness of fit, transformations, etc.'''
    },
    'b4_5': {
        'label': 'B.4.5 Quantitative Treatments',
        'desc': '''Describe any quantitative treatments of data, including
                   the mathematical and statistical procedures.'''
    },
    'b4_6': {
        'label': 'B.4.6 Statistical Software',
        'desc': '''Provide the reference and version on any statistical
                   software that will be used.'''
    },
    'b4_7': {
        'label': 'B.4.7 Data Use Limitations',
        'desc': '''Describe how any limitations on the use of data will be
                   identified and reported.'''
    }
}

# ########################################################################
# ########################################################################
# ########################################################################

SOFTWARE_DEVELOPMENT = {
    'b1_1': {
        'heading': 'B.1 REQUIREMENTS',
        'label': 'B.1.1 Identify Users',
        'desc': '''Identify the users of the software and describe any special
                   user roles or tasks that will be required. Describe the
                   minimum skill-level(s) or qualification(s) that the software
                   user must possess prior to operating/using the software.'''
    },
    'b1_2': {
        'label': 'B.1.2 Define Critical Functionality',
        'desc': '''Provides a list and/or graphical representation(s) of the
                   critical functions that the software system implements.
                   Developer should map the key/critical software design
                   requirements to the important performance/operational
                   areas of the software.'''
    },
    'b1_3': {
        'label': 'B.1.3 System Requirements',
        'desc': '''Explains and describes the system requirements which
                   implement the software functionality, including external
                   interfaces (e.g., Graphical User Interfaces [GUIs], and
                   operational interfaces, which are used by other software
                   programs, to call subroutines from the main software
                   program, as applicable, etc.), performance requirements,
                   and design constraints. System requirements should consider
                   computer (and external) hardware, Graphical User Interfaces
                   [GUIs], operating system software, interfaces with other
                   software/models/databases, minimum and maximum software
                   functionality, operational performance, network
                   communications, computer security, system access, and
                   software and database backup and recovery.  Each requirement
                   should be uniquely identified, and defined, so that its
                   existence and implementation can be objectively verified
                   and validated (e.g., tested).
                   The term 'requirements' encompasses the areas of computer
                   and external hardware Graphical User Interface(s),
                   operating system software, interfaces with other
                   software/models/databases, minimum and maximum software
                   functionality, operational performance, network
                   communications computer security, system access, and
                   software and database back and recovery.'''
    },
    'b1_4': {
        'label': 'Performance and Design Constraints',
        'desc': '''Describe any anticipated performance, and design
                   constraints. Explain the factors (controllable or
                   uncontrollable) that influence the design and operational
                   behavior of the software/model. Describe the mitigation
                   strategies chosen to address these performance and design
                   constraints as applicable.'''
    },
    'b1_5': {
        'label': 'System Hardware and OS Requirements',
        'desc': '''Specify computer hardware (e.g., computer memory storage
                   requirement, computer hard disk/permanent storage
                   requirements, internal system processor clock speed,
                   number of computer nodes or clusters, etc.) and operating
                   system requirements (e.g., Windows 10, MacOS, Linux, Unix,
                   single-threaded or multi-threaded configuration, etc.).'''
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
    # ########################################
    'b2_1': {
        'heading': 'B.2 SYSTEM DESIGN',
        'label': 'B.2.1 System Design',
        'desc': '''Provides an overview of the system design, including block
                   diagrams displaying relationships between major program
                   modules, hardware devices (e.g., computers, storage systems,
                   external computer-controlled systems, etc.), databases,
                   external applications, tools, and models, and data
                   input/output processes, data rates, and data storage
                   requirements.'''
    },
    'b2_2': {
        'label': 'B.2.2 Components and Subcomponents',
        'desc': '''Describes the components and subcomponents of the software
                   design, including databases, tools, interfaces to external
                   hardware and software, and internal interfaces (including
                   GUIs). The description should link the software structure
                   to the functional requirements.'''
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
                   all Functional Requirements (FRs) back to system objectives,
                   to ensure all System Design (SD) elements are included.
                   Changes at this stage should produce an amendment or update
                   to the QAPP. Evaluation of the FRs, and the relationships
                   between requirements, and the checks for correctness,
                   consistency, completeness, accuracy, readability, and
                   testability, should occur after this phase is completed.
                   Developer should assess how well the FRs satisfy the
                   System Design (SD) objectives.'''
    },
    # ########################################
    'b3_1': {
        'heading': 'B.3 SYSTEM DOCUMENTATION',
        'label': 'B.3.1 Documentation Requirements',
        'desc': '''Specifies the requirements for documentation of, the
                   methods, processes, and facilities used to maintain, store,
                   secure, and preserve the document-controlled versions, and
                   related artifacts of, the product software during all
                   phases of the software development life cycle (e.g.,
                   requirements documents, design documents, configuration
                   management plans, test plans,  operations manuals, software
                   source code (for models, tools, database, applications
                   [e.g., Application Programming Interfaces {APIs}], etc.),
                   and user's guides.'''
    },
    'b3_2': {
        'label': 'B.3.2 Software and Hardware Documentation',
        'desc': '''Describes the procedures for controlling, documenting,
                   and archiving all changes to software and hardware.
                   Describes the use of software configuration management,
                   software version control, code repository management,
                   and product release management
                   (e.g., BitBucket, GitHub, etc.).
                   US EPA GitHub for External SW development
                   US EPA Bitbucket for Internal SW development
                   In addition, ORD application (app) inventory is required
                   for ORD developed app'''
    },
    'b3_3': {
        'label': 'B.3.3 Software Configuration Management (SCM)',
        'desc': '''Identifies the software used to archive, control, document,
                   save, and recover changes made to the system software
                   source code. GitHub, Bitbucket, and ORD Application
                   Inventory used to track Open Source Software (OSS).'''
    },
    # ########################################
    'b4_1': {
        'heading': 'B.4 CODING AND IMPLEMENTATION',
        'label': 'B.4.1 Development Process',
        'desc': '''Describes how the operational software system is developed
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
                   tested, verified, and validated (e.g., describes the
                   testing regime for the software [unit test, component
                   test, software integration test, system test, quality
                   assurance/quality control test, user acceptance test
                   {UAT}, etc.]).'''
    },
    'b4_3': {
        'label': 'B.4.3 Software Versioning, Release, and Delivery',
        'desc': '''Describes the software versioning, release, and delivery
                   process and how it is managed, including software versions
                   for alpha and beta testing, user acceptance testing (UAT),
                   and training materials, including user manuals. '''
    },
    'b4_4': {
        'label': 'B.4.4 Software Operational Scenarios',
        'desc': '''Describes how the model will be applied in different
                   operational situations, and details the required model
                   inputs (provide detailed information on the data input
                   format[s] and the external interfaces that feed into the
                   model) and outputs (provide detailed information on the
                   model output format[s] and the external interfaces that the
                   model feeds into). Explains the required operational
                   conditions that must be present to apply the model, and
                   notes that the steps required to achieve the required setup
                   to apply the model will be fully documented in a user
                   manual, test procedure, and/or operations manual for the
                   model/software. Applicable to models, databases, tools,
                   and application programming interfaces (APIs).'''
    },
    # ########################################
    'b5_1': {
        'heading': 'B.5 VERIFICATION AND VALIDATION',
        'label': 'B.5.1 Testing Strategy',
        'desc': '''Describes the testing strategy that will be used, along
                   with the procedures for each planned test. These tests can
                   include routines that assess the operation of the software,
                   including processing of inputs, format of outputs, testing
                   of module/function internal logic/algorithms, etc.,
                   validation, and verification of the software functions.
                   Testing may include, but is not limited to, individual
                   module tests, integration tests, system testing, user
                   acceptance testing, and alpha, and beta testing, etc.
                   Verification: The process of determining whether the
                   products of a given stage of the software development
                   life cycle fulfills the requirements established during
                   the previous stage.
                   Validation: The process of evaluating software at the end
                   of the software development process (acceptance testing
                   activity in the testing stage) to ensure compliance with
                   software requirements.'''
    },
    'b5_2': {
        'label': 'B.5.2 Review Process',
        'desc': '''Describes the review process for the software's Graphical
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
                   within the acceptable range of values, and/or are
                   consistent and applicable, given the subject area
                   (scientific domain) of the model.'''
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
    # ########################################
    'b6_1': {
        'heading': 'MAINTENANCE AND USER SUPPORT',
        'label': 'B.6.1 Post-Release Maintenance',
        'desc': '''Describes the procedures for maintenance and user support
                   when the software or data generated by the project is
                   distributed or deployed outside of the ORD center that
                   initiated the development of the software product.
                   Project Document(s), including the software source code
                   header for each code module, must clearly state that EPA
                   owns the operational software, its source code, object
                   code, databases, and documents, etc., with unlimited rights
                   to its use, transfer, and final disposition.'''
    },
    'b6_2': {
        'label': 'B.6.2 User Access and Training',
        'desc': '''Describes how user will be granted access to the system
                   and any training required.'''
    },
    'b6_3': {
        'label': 'B.6.3 Training Material and User Guides',
        'desc': '''Describe type of training materials/user manuals/system
                   guides that will be developed. Identify who will develop
                   them, and how they will be delivered or made accessible
                   to the users.'''
    }
}

# ########################################################################
# ########################################################################
# ########################################################################

SECTION_B_INFO = {
    "Analytical Methods": ANALYTICAL_METHODS,
    "Animal Cell Studies": ANIMAL_CELL,
    # "Cell Culture Models": CELL_CULTURE_METHODS,
    "Existing Data": EXISTING_DATA,
    "Measurements": MEASUREMENTS_AND_MONITORING,
    # "Model Development": MODEL_DEVELOPMENT,
    "Model Application": MODEL_APPLICATION,
    "Soc Sci": SOC_SCI,
    "Software Development": SOFTWARE_DEVELOPMENT,
}
