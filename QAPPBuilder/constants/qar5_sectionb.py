# qar5_sectionb.py (constants)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301

"""Constants for the QAR5 QAPP_Builder module."""

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

EXISTING_DATA = {
    'b1_1': {
        'heading': 'B.1	DATA ACQUISITION AND COLLECTION',
        'label': 'B.1.1 Existing Data',
        'desc': 'Identify the Existing Data and Information needed to ' +
        'meet the research objective(s).'
    },
    'b1_2': {
        'label': 'B.1.2 Data Use',
        'desc': 'Describe how the existing data/ information will be ' +
        'used in the research effort (e.g., augment or replace ' +
        'existing data/ information, verify or validate ' +
        'existing data/ information.'
    },
    'b1_3': {
        'label': 'B.1.3 Data Requirements',
        'desc': 'Specify requirements relating to the type of data, ' +
        'the age of data, geographical representation, temporal ' +
        'representation, and technological representation, as applicable.'
    },
    'b1_4': {
        'label': 'B.1.4 Databases, Maps, Literature',
        'desc': 'Identify databases, maps and literature, and list ' +
        'as applicable to the research effort:\r\n(1) Information and ' +
        'data used to site or time sampling events (meteorology, ' +
        'geology, etc.);\r\n(2) Anecdotal or other information ' +
        'triggering the study;\r\n(3) Toxicity, exposure, and ' +
        'environmental fate data;\r\n(4) Models and their ' +
        'output;\r\n(5) Census data;\r\n(6) GIS data.'
    },
    'b1_5': {
        'label': 'B.1.5 Non-Quality Constraints',
        'desc': 'Identify any non-quality constraints on the ' +
                'Existing Data and Information that affect its use in ' +
                'the research ' +
                'effort (e.g., legal, programmatic, privacy/ ' +
                'confidentiality (i.e., is it proprietary or CBI)).\r\nIf ' +
                'supporting an office, region or program check on ' +
                'applicability of the project/decision, examples may ' +
                'include: CAA Credible Evidence Revisions (FR 62:36, ' +
                'Feb. 24, 1997) or Federal Rule of Evidence 702.).'
    },
    'b2_1': {
        'heading': 'B.2	DATA COLLECTION AND EVALUATION',
        'label': 'B.2.1 Existing Data Sources',
        'desc': 'Identify the source(s) for the Existing Data and ' +
                'Information.  ' +
                'Describe the planning process for data gathering and ' +
                'how the project ensures that data or information collected ' +
                'are of sufficient quality to satisfy the ' +
                'needs of the research effort.'
    },
    'b2_2': {
        'label': 'B.2.2 Criteria for Acceptance or Rejection',
        'desc': 'Describe the process for acceptance/ rejection and ' +
                'inclusion/ exclusion of Existing Data and Information' +
                'to support research ' +
                'objectives (e.g., to exclude potential bias).'
    },
    'b2_3': {
        'label': 'B.2.3 Rational Selection of Existing Data',
        'desc': 'Discuss the rationale for selecting the source(s) ' +
                'identified.  If a hierarchy of sources exists for the ' +
                'gathering of Existing Data and Information, specify ' +
                'that hierarchy.'
    },
    'b2_4': {
        'label': 'B.2.4 SOPs Determine Quality of Data',
        'desc': 'Describe the procedures for determining the quality of ' +
                'the Existing Data and Information. Identify criteria for ' +
                'evaluating data ' +
                'or information quality (e.g., using EPA’s five General ' +
                'Assessment Factors or using measurement data criteria such ' +
                'as accuracy, precision, representativeness, completeness, ' +
                'and comparability).\r\nNote: Existing published data from ' +
                'sources such as governmental databases which have ' +
                'well-documented QA/QC procedures may not require ' +
                'additional evaluation for quality.'
    },
    'b2_5': {
        'label': 'B.2.5 Disclaimer Existing Data',
        'desc': 'If the quality of the Existing Data and Information ' +
                'will not be evaluated by EPA, state this in the QAPP and ' +
                'require one of the following disclaimer statements to be ' +
                'added to any research product requiring clearance:\r\nEPA ' +
                'is distributing this information solely as a public ' +
                'service. [Insert name of information source] is ' +
                'responsible for the quality of this information. EPA\'s ' +
                'distribution of this information does not represent or ' +
                'imply endorsement by EPA.\r\nor;\r\nThe research presented ' +
                'was not performed or funded by EPA and was not subject to ' +
                'EPA\'s quality system requirements. The views expressed in ' +
                'this [article/presentation/poster] are those of the ' +
                'author(s) and do not necessarily represent the views or ' +
                'the policies of the U.S. Environmental Protection Agency.'
    },
    'b3_1': {
        'heading': 'B.3	DATA MANAGEMENT AND DOCUMENTATION',
        'label': 'B.3.1 Data Tracking and Storage',
        'desc': 'Describe the process for documenting and tracking ' +
                'sources used and the information that will be recorded for ' +
                'the Existing Data and Information collected (e.g., data ' +
                'source, originating organization, report title, type of ' +
                'information, date).'
    }
}

SOFTWARE_DEVELOPMENT = {
    'b1_1': {
        'heading': 'B.1	FUNCTIONAL REQUIREMENTS',
        'label': 'B.1.1 Functional Requirements',
        'desc': 'Provide a list of the most important functions ' +
                'that the software system must address.'
    },
    'b1_2': {
        'label': 'B.1.2 Requirements Design',
        'desc': 'Identify requirements for functionality, external ' +
                'interfaces (includes graphical user interfaces and ' +
                'interfaces which are needed for other programs to call ' +
                'subroutines from the software, as applicable), ' +
                'performance, and design constraints. Each requirement ' +
                'should be uniquely identified and defined such that its ' +
                'achievement is capable of being objectively ' +
                'verified and validated.'
    },
    'b1_3': {
        'label': 'B.1.3 Hardware Minimum Requirements',
        'desc': 'Specify computer hardware and operating system ' +
                'requirements as required in the ORD APP inventory.'
    },
    'b2_1': {
        'heading': 'B.2	SYSTEM DESIGN',
        'label': 'B.2.1 System Design',
        'desc': 'Provide an overview of the system design, e.g., block ' +
                'diagrams showing relationships between major program ' +
                'modules, hardware devices, and data input/output.'
    },
    'b2_2': {
        'label': 'B.2.2 Components and Subcomponents',
        'desc': 'Describe the components and subcomponents of the ' +
                'software design, including databases and internal ' +
                'interfaces. The description should link the software ' +
                'structure to the functional requirements.'
    },
    'b2_3': {
        'label': 'B.2.3 Rationale of Hardware/Software',
        'desc': 'Provide the rationale for selecting the proposed ' +
                'hardware and software tools as addressed in the ' +
                'application governance process.'
    },
    'b3_1': {
        'heading': 'B.3	IMPLEMENTATION',
        'label': 'B.3.1 Design Specifications',
        'desc': 'Describe how a working software system is developed ' +
                'from the design specifications. Agile software ' +
                'development is recommended.'
    },
    'b3_2': {
        'label': 'B.3.2 Requirements for Functionality',
        'desc': 'Describe how the requirements for functionality, ' +
                'external interfaces, performance, and design ' +
                'constraints will be verified and validated.'
    },
    'b3_3': {
        'label': 'B.3.3 Software Implementation',
        'desc': 'Describe how release and delivery of the product is ' +
        'managed, including versions for alpha and beta testing, ' +
        'user acceptance testing (UAT), and training materials for users.'
    },
    'b3_4': {
        'label': 'B.3.4 Software Configuration Management (SCM)',
        'desc': 'Describe the procedures for controlling, documenting, ' +
                'and archiving all significant changes to software and ' +
                'hardware. Recommend the use of bitbucket or GitHub ' +
                'depending on scenario.'
    },
    'b3_5': {
        'label': 'B.3.5 Software Maintenance',
        'desc': 'Identify the archiving software used for controlling, ' +
                'documenting, saving, and recovering changes made ' +
                'to the source code.'
    },
    'b4_1': {
        'heading': 'B.4	VALIDATION, VERIFICATION, AND TESTING',
        'label': 'B.4.1 V&V and IV&V',
        'desc': 'Describe the testing strategy that will be used along ' +
                'with the procedures for each planned test. These tests ' +
                'can include routines that assess validation and ' +
                'verification of the software functions. Testing may ' +
                'include individual module tests, integration tests, system ' +
                'testing, acceptance testing, and alpha and beta testing.'
    },
    'b4_2': {
        'label': 'B.4.2 GUI',
        'desc': 'Describe the review process for the software’s ' +
                'graphical user interface and output reports.  Ensure ' +
                'that summary or synthesis statements accurately represent ' +
                'the underlying data and limitations.  Check for correct ' +
                'interpretation of results, clarity of discussion, proper ' +
                'citations and references, and spelling and grammar.'
    },
    'b4_3': {
        'label': 'B.4.3 I/O Testing',
        'desc': 'Describe the procedure for checking the correctness of ' +
                'outputs and validity of model inputs, e.g., checks that ' +
                'input parameters are realistic and/or do not violate ' +
                'the applicability domain of the model.'
    },
    'b4_4': {
        'label': 'B.4.4 User/Agency Expectations',
        'desc': 'Describe how it will be determined if the developed ' +
                'software product conforms to customer and Agency ' +
                'requirements, and whether the software product fulfills ' +
                'the intended use and user expectations. This includes ' +
                'analysis, evaluation, review, inspection, assessment' +
                ', and testing of the software product and the ' +
                'processes that produced the product.'
    },
    'b5_1': {
        'heading': 'B.5	DOCUMENTATION, MAINTENANCE, AND USER SUPPORT',
        'label': 'B.5.1 Documentation',
        'desc': 'Specify the requirements for documentation, methods and ' +
                'facilities used to maintain, store, secure, and ' +
                'document-controlled versions and related artifacts of ' +
                'the identified software during all phases of the software ' +
                'life cycle (e.g., requirements and design documents, ' +
                'configuration maintenance plan, operations manual, ' +
                'source code, user’s guide, and application ' +
                'programming interface).'
    },
    'b5_2': {
        'label': 'B.5.2 Support',
        'desc': 'Describe the procedures for maintenance and user ' +
        'support when software or data generated by the project will ' +
        'be distributed or deployed outside of the ORD laboratory ' +
        'that initiated the development of the software product.'
    }
}

MODEL_DEVELOPMENT = {
    'b1_1': {
        'heading': 'B.1	MODEL DESIGN',
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
        'heading': 'B.2	MODEL DEREVATION',
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
        'heading': 'B.3	VALIDATION, VERIFICATION, AND TESTING',
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
        'heading': 'B.4	DOCUMENTATION',
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

MODEL_APPLICATION = {
    'b1_1': {
        'heading': 'B.1	MODEL SPECIFICATION',
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
        'heading': 'B.2	MODEL SELECTION',
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
        'heading': 'B.3	MODEL PARAMETERIZATION AND CALIBRATION',
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
        'heading': 'B.4	MODEL PERFORMANCE ASSESSMENT',
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
        'heading': 'B.5	INTERPRETATION OF MODEL RESULTS',
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
        'heading': 'B.6	DOCUMENTATION',
        'label': 'B.6.1 I/O Requirements',
        'desc': 'Specify the requirements for project documentation ' +
                '(e.g., model input/output files; results of model ' +
                'performance assessment; scripts or source code; ' +
                'post-processed model output).'
    },
    'b6_2': {
        'label': 'B.6.2 Ammendments to QAPP',
        'desc': 'Identify QAPP elements that may need to be ' +
                'updated as the project moves forward and describe the ' +
                'procedures for QAPP amendment and distribution.'
    }
}

MEASUREMENTS_AND_MONITORING = {
    'b1_1': {
        'heading': 'B.1	EXPERIMENTAL DESIGN',
        'label': 'B.1.1	Analyte(s) of Interest & Matrix/Matrices’',
        'desc': 'Identify the specific analyte(s) of interest and the ' +
                'matrix/matrices. Classify each measurement parameter ' +
                'as either critical or needed for information only.'
    },
    'b1_2': {
        'label': 'B.1.2	Sampling and/or Experimental Design',
        'desc': 'Describe sampling and/or experimental design to ' +
                'generate the data needed to evaluate the research ' +
                'objectives. A description of the design should ' +
                'include the rationale for the design and types ' +
                'and number of samples required, including any ' +
                'field or experimental QC samples.'
    },
    'b1_3': {
        'label': 'B.1.3	Sampling Locations & Frequency',
        'desc': 'Identify sampling locations and frequency of sampling.'
    },
    'b2_1': {
        'heading': 'B.2	SAMPLING PROCEDURES',
        'label': 'B.2.1	Non-Synthetic (real-world sample) Samples',
        'desc': 'If non-synthetic (i.e., real-world sample) ' +
                'samples are used describe the sampling design that ' +
                'will be used, and the steps taken to assure that ' +
                'representative samples are collected.'
    },
    'b2_2': {
        'label': 'B.2.2	Synthetic (lab-prepared) Samples',
        'desc': 'If synthetic (i.e., laboratory-prepared) ' +
                'samples are used, describe the preparation of these samples.'
    },
    'b2_3': {
        'label': 'B.2.3	Decontamination Procedures',
        'desc': 'Describe the decontamination procedures for any ' +
                'sampling equipment that will be reused to ' +
                'prevent cross contamination.'
    },
    'b2_4': {
        'label': 'B.2.4	Sample Containers & Quantities',
        'desc': 'Provide a list of sample containers, sample quantities ' +
                'to be collected, and the sample amount required for ' +
                'each analysis, including QC sample analysis.'
    },
    'b2_5': {
        'label': 'B.2.5	Labeling',
        'desc': 'Describe labeling (information to be included) ' +
                'and uniquely numbering each sample.'
    },
    'b2_6': {
        'label': 'B.2.6	Sample Preservation',
        'desc': 'Specify sample preservation requirements ' +
                '(e.g., refrigeration, acidification, etc.) ' +
                'and sample hold times.'
    },
    'b2_7': {
        'label': 'B.2.7	Calibration Procedures',
        'desc': 'If non-synthetic (i.e., real-world sample) samples ' +
                'are used describe procedures for packing and shipping ' +
                'samples, and provisions for maintaining ' +
                'chain-of-custody, as applicable.'
    },
    'b3_1': {
        'heading': 'B.3	MEASUREMENT PROCEDURES',
        'label': 'B.3.1	Field Analyses',
        'desc': 'For field analyses (including in-line measurements), ' +
                'describe in detail or reference each field sample ' +
                'analysis method and instrumentation to be used. ' +
                'Include steps for instrument calibration, ' +
                'measurement, quality control, and documentation of results.'
    },
    'b3_2': {
        'label': 'B.3.2	Lab Analyses',
        'desc': 'For laboratory analyses, describe in detail or ' +
                'reference each sample preparation method (e.g., ' +
                'sample extractions) and analytical methods, equipment ' +
                'and instrumentation to be used. Include steps for ' +
                'preparation, calibration, measurement, quality ' +
                'control, and reporting.'
    },
    'b3_3': {
        'label': 'B.3.3	Specific Calibration Procedures',
        'desc': 'Include specific calibration procedures, including ' +
                'linearity checks and initial and continuing calibration ' +
                'checks, and detection limits.'
    },
    'b4_1': {
        'heading': 'B.4	METHOD PERFORMANCE METRICS',
        'label': 'B.4.1	Method QC check',
        'desc': 'For each analysis method QC check (e.g., blanks, ' +
                'control samples, duplicates, matrix spikes, surrogates) ' +
                'specify the frequencies for performing these checks, ' +
                'associated acceptance criteria, and corrective actions ' +
                'to be performed if acceptance criteria are not met.'
    },
}

ANALYTICAL_METHODS = {
    'b1_1': {
        'heading': 'B.1	EXPERIMENTAL DESIGN',
        'label': 'B.1.1 Analyte(s) of Interest',
        'desc': 'Identify the specific analyte(s) of interest ' +
        'and the matrix/matrices or limitations to the ' +
        'range of detection under study.'
    },
    'b1_2': {
        'label': 'B.1.2 Analytical Approach',
        'desc': 'Identify the analytical approach that will be used ' +
        'and how it will be optimized for this study. Also ' +
        'describe any tests of interference and analyte stability.'
    },
    'b1_3': {
        'label': 'B.1.3 Performance Metrics',
        'desc': 'Identify the method performance metrics (QA/QC checks) ' +
        'that will be used to evaluate the method, including the ' +
        'procedures used. These metrics could include (but are not ' +
        'limited to) positive and negative controls, sensitivity, ' +
        'precision, accuracy, recovery, linearity, specificity, ' +
        'robustness, and range. '
    },
    'b2_1': {
        'heading': 'B.2	SAMPLING PROCEDURES',
        'label': 'B.2.1 Requirements for Samples',
        'desc': 'Provide the requirements for samples including those ' +
        'field collected or made in the laboratory, that will be ' +
        'used to test the method, including matrix and ' +
        'presence/concentration of analytes). '
    },
    'b2_2': {
        'label': 'B.2.2 Requirements for Synthetic Samples',
        'desc': 'If synthetic (i.e., laboratory-prepared) samples are ' +
        'used, describe the preparation of these samples.'
    },
    'b2_3': {
        'label': 'B.2.3 Requirements for Non-Synthetic Samples',
        'desc': 'If non-synthetic (i.e., real-world sample) samples are ' +
        'used describe the sampling design that will be used and the ' +
        'steps taken to assure that representative samples are collected.'
    },
    'b2_4': {
        'label': 'B.2.4 Non-Synthetic Sampling SOPs',
        'desc': 'If non-synthetic (i.e., real-world sample) samples are ' +
        'used discuss or reference each sampling procedure.'
    },
    'b2_5': {
        'label': 'B.2.5 Synthetic Sampling SOPs',
        'desc': 'If non-synthetic (i.e., real-world sample) samples are ' +
        'used If non-synthetic (i.e., real-world sample) samples are used.'
    },
    'b2_6': {
        'label': 'B.2.6 Non-Synthetic Package/Shipping',
        'desc': 'If non-synthetic (i.e., real-world sample) samples are ' +
        'used describe procedures for packing and shipping samples, ' +
        'and provisions for maintaining chain-of-custody, as applicable.'
    },
    'b2_7': {
        'label': 'B.2.7 Sample Preservation',
        'desc': 'Specify sample preservation requirements (e.g., ' +
        'refrigeration, acidification, etc.) and holding times.  ' +
        'If a holding time study will be conducted, ' +
        'describe the parameters of this study.'
    },
    'b2_8': {
        'label': 'B.2.8 Numbering',
        'desc': 'Describe the method for uniquely numbering each sample. '
    },
    'b3_1': {
        'heading': 'B.3	MEASUREMENT PROCEDURES',
        'label': 'B.3.1 Calibration QA/QC',
        'desc': 'Describe in detail or reference each preparation ' +
        'or analytical procedure, equipment and instrumentation ' +
        'to be used, if known. Include steps for preparation, ' +
        'calibration, measurement, quality control, and reporting.'
    },
    'b3_2': {
        'label': 'B.3.2 Detection Limits',
        'desc': 'Include specific calibration procedures, including ' +
        'linearity checks and initial and continuing ' +
        'calibration checks, and detection limits. '
    },
    'b4_1': {
        'heading': 'B.4	METHOD PERFORMANCE METRICS',
        'label': 'B.4.1 QA/QC Checks',
        'desc': 'For each method performance metric (QA/QC check) ' +
        'specify the frequencies for performing these checks, ' +
        'associated acceptance criteria, and corrective actions to ' +
        'be performed if acceptance criteria are not met. '
    }
}

CELL_CULTURE_METHODS = {
    'b1_1': {
        'heading': 'B.1	EXPERIMENTAL DESIGN',
        'label': 'B.1.1 Culture Model',
        'desc': 'Discuss the culture model to be used in ' +
        'addressing the study objectives.'
    },
    'b1_2': {
        'label': 'B.1.2 Stressors Tested',
        'desc': 'Discuss the choice of chemicals, materials, or ' +
        'other stressors to be tested in addressing the study objectives.'
    },
    'b1_3': {
        'label': 'B.1.3 Independent Variables',
        'desc': 'Discuss independent variables to be manipulated. '
    },
    'b1_4': {
        'label': 'B.1.4 Dependent Variables',
        'desc': 'Discuss dependent variables to be measured.'
    },
    'b2_1': {
        'heading': 'B.2	METHODS AND EXPERIMENTAL DETAIL',
        'label': 'B.2.1 Treatment Group Exposures',
        'desc': 'Describe the method for determining treatment group ' +
        'exposures and number of replicates (dose limits; ' +
        'power calculations).'
    },
    'b2_2': {
        'label': 'B.2.2 Study Controls',
        'desc': 'Describe study controls (blinding; standard ' +
        'curves; positive/negative controls; etc.).'
    },
    'b2_3': {
        'label': 'B.2.3 Sample Collection',
        'desc': 'Provide details of sample collection, ' +
        'identification, storage, analysis etc.'
    },
    'b2_4': {
        'label': 'B.2.4 Project Personnel/Collaborators',
        'desc': 'List project personnel/collaborators and their roles.'
    },
    'b2_5': {
        'label': 'B.2.5 SOPs Protocols',
        'desc': 'List and attach all operating procedures or protocols ' +
        'and ensure that they include adequate quality control.'
    },
    'b2_6': {
        'label': 'B.2.6 Procedures not Covered',
        'desc': 'Describe the procedures to be used for any activities ' +
        'that are not covered by existing operating procedures or ' +
        'protocols.  Ensure that appropriate quality control is included.'
    },
    'b3_1': {
        'heading': 'B.3	EQUIPMENT AND SUPPLIES',
        'label': 'B.3.1 Equipment',
        'desc': 'List major equipment (make, model).'
    },
    'b3_2': {
        'label': 'B.3.2 Supplies',
        'desc': 'List critical supplies (name, source, amount, ' +
        'expiration dates if any).'
    },
    'b4_1': {
        'heading': 'B.4	DATA COLLECTION AND ANALYSIS',
        'label': 'B.4.1 Datasets Collected',
        'desc': 'List and describe (analog, electronic, etc.) ' +
        'datasets to be collected.'
    },
    'b4_2': {
        'label': 'B.4.2 Data Verification',
        'desc': 'Describe data verification procedures used ' +
        'to ensure reporting of accurate data.'
    },
    'b4_3': {
        'label': 'B.4.3 Statistical Analysis',
        'desc': 'Describe planned statistical analysis following ' +
        'guidance of: https://intranet.ord.epa.gov/nheerl/' +
        'cop-statistics-study-design-experimental'
    }
}

ANIMAL_SUBJECTS = {
    'b1_1': {
        'heading': 'B.1	EXPERIMENTAL DESIGN',
        'label': 'B.1.1 Animal Subjects Tested',
        'desc': 'Discuss the choice of animal subjects to be tested, ' +
        'including ACUP/LAPR references, if applicable in addressing ' +
        'the study objectives. (ACUP = Animal Care and Use Protocol, ' +
        'previously known as the LAPR = Laboratory Animal Protocol ' +
        'Report. These documents address the regulatory animal ' +
        'care and use ethics requirements.)'
    },
    'b1_2': {
        'label': 'B.1.2 Chemicals, Materials, Stressors',
        'desc': 'Discuss the choice of chemicals, materials, or other ' +
        'stressors to be tested in addressing the study objectives.'
    },
    'b1_3': {
        'label': 'B.1.3 Independent Variables',
        'desc': 'Discuss independent variables to be manipulated. '
    },
    'b1_4': {
        'label': 'B.1.4 Dependent Variables',
        'desc': 'Discuss dependent variables to be measured.'
    },
    'b2_1': {
        'heading': 'B.2	METHODS AND EXPERIMENTAL DETAIL',
        'label': 'B.2.1 Determining Test Group',
        'desc': 'Describe the method for determining test group ' +
        'treatment, number, and size (dose limits; power calculations).'
    },
    'b2_2': {
        'label': 'B.2.2 Method for Test Group',
        'desc': 'Describe the method for test group assignment and ' +
        'identification for individual animal subjects ' +
        '(randomization; tagging, group housing).'
    },
    'b2_3': {
        'label': 'B.2.3 Study Controls',
        'desc': 'Describe study controls (blinding; standard curves; ' +
        'positive/negative controls; control, sentinel, ' +
        'and sham animals, etc.).'
    },
    'b2_4': {
        'label': 'B.2.4 Sample Collection',
        'desc': 'Provide details of sample collection, ' +
        'identification, storage, analysis etc.'
    },
    'b2_5': {
        'label': 'B.2.5 SOPs',
        'desc': 'List and attach all operating procedures or protocols ' +
        'and ensure that they include adequate quality control.'
    },
    'b2_6': {
        'label': 'B.2.6 Other SOPs',
        'desc': 'Describe the procedures to be used for any activities ' +
        'that are not covered by existing operating procedures or ' +
        'protocols.  Ensure that appropriate quality control is included.'
    },
    'b3_1': {
        'heading': 'B.3	EQUIPMENT AND SUPPLIES',
        'label': 'B.3.1 Equipment',
        'desc': 'List major equipment (make, model).'
    },
    'b3_2': {
        'label': 'B.3.2 Supplies',
        'desc': 'List critical supplies (name, source, ' +
        'amount, expiration dates if any).'
    },
    'b4_1': {
        'heading': 'B.4	DATA COLLECTION AND ANALYSIS',
        'label': 'B.4.1 Datasets',
        'desc': 'List and describe (analog, electronic, ' +
        'etc.) datasets to be collected .'
    },
    'b4_2': {
        'label': 'B.4.2 V&V',
        'desc': 'Describe data verification procedures used to ' +
        'ensure reporting of accurate data'
    },
    'b4_3': {
        'label': 'B.4.3 Statistical Analysis',
        'desc': 'Describe planned statistical analysis following ' +
        ' +guidance of: https://intranet.ord.epa.gov/' +
        'nheerl/cop-statistics-study-design-experimental'
    }
}

SECTION_B_INFO = {
    "Existing Data": EXISTING_DATA,
    "Software Development": SOFTWARE_DEVELOPMENT,
    "Model Development": MODEL_DEVELOPMENT,
    "Model Application": MODEL_APPLICATION,
    "Measurements": MEASUREMENTS_AND_MONITORING,
    "Analytical Methods": ANALYTICAL_METHODS,
    "Cell Culture Models": CELL_CULTURE_METHODS,
    "Animal Subjects": ANIMAL_SUBJECTS
}
