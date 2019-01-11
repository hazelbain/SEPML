# SEPML
Solar Energetic Particle (SEP) forecasting with machine learning framework

Current physics based models of SEPs are unable to execute sufficiently fast in order to provide actionable information towards forecasting such disturbances, which can impact Earth within tens of minutes of the onset of an eruptive event. This is compounded by the intrinsic latency of certain key observations, which are used to define the initial conditions of these models. Instead, there is a reliance on statistical models to provide forecast probabilities of Earth-bound SEPs using real-time data. Since the largest, most impactful events occur infrequently, some regions of the feature space are sparse and simple discrete binning procedures have limitations. The goal of this project is to improve upon the empirical SEP proton prediction forecast model (PROTONS) currently in operational use at SWPC, through the application of modern machine learning techniques.

# Notebooks

#### sep_master.ipynb
This notebook deals ONLY with the original Balch features - Soft X-ray ingrated flux, soxft X-ray peak flux, typeII and typeIV features for logistic regression, decision trees and SVM.

#### sep_master_new_features.ipynb	
Main Notebook for dealing with all new features beyond Balch - Wind Waves 1 MHz fluence, GOES temp and emission measure, and soon to be RSTN integrated flux. 

#### SEP.ipynb - ***DEPRECATED***

#### sep_master_T_EM.ipynb - ***DEPRECATED***
Analysis rolled into sep_master_new_features

#### sep_LogisticRegression.ipynb - ***DEPRECATED***
Breakout notebook to look at logisitic regression only 

#### sep_DecisionTree.ipynb - ***DEPRECATED***
Breakout notebook to look at decision trees only

#### GOES_temp_em_scratch.ipynb
Notebook to cross reference GOES Temp and Emission Measure files for the original Balch event list (1986 - 2004) with Doug's student's event list which contains T and EM values. This Notebook generates the data file: AllEvtsShuffled_1986_2004_t_em.csv

#### SEP.ipynb
Main Juptyer Python notebook 

# Data Files

#### SPEall.v7p.xls
SEP event list from the Balch 2008 paper

#### ctrlevents.v8p.xls
Event list from Balch 2008 paper containing all SEP and control events.

#### ControlEvents_student.xls
Doug's student's event list. Based on Balch event list but expanded to include new features.

#### AllEvtsShuffled_1986_2004_cme.csv
Shuffled version of ControlEvents_student.xls

#### AllEvtsShuffled_1986_2004_t_em.csv - ***USE THIS ONE***
Original Balch event list with GOES Temp and Emission Measure values added from Doug's Student's event list

#### AllEvtsShuffled.csv	(???)
#### AllEvtsShuffled_1986_2004.csv	(???)
#### AllEvtsShuffled_1986_2004_cme.csv	(???)


#### sep_events_2004_2017.xls  - ***DEPRECATED (I think)***
SEP event list for events from 2004 to 2017

#### sep_events_2004_2017.csv - ***DEPRECATED (I think)***
replcae sep_events_2004_2017.xls with the csv version


Type	Name	Latest commit message	Commit time

