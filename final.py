# =======================================================================================================
# Table of Contents START
# =======================================================================================================

'''
1. Orientation
2. Imports
3. visual1
4. visual2
5. visual3
6. visual4
7. visual5
8. visual6
9. stat1
10. stat2
11. stat3
12. models
13. models_best
14. acquire
15. prepare
16. wrangle
'''

# =======================================================================================================
# Table of Contents END
# Table of Contents TO Orientation
# Orientation START
# =======================================================================================================

'''
The purpose of this file is to create functions in order to expedite and maintain cleanliness
of the final_report.ipynb
'''

# =======================================================================================================
# Orientation END
# Orientation TO Imports
# Imports START
# =======================================================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, recall_score
import wrangle as w
import explore as e

# =======================================================================================================
# Imports END
# Imports TO visual1
# visual1 START
# =======================================================================================================



# =======================================================================================================
# visual1 END
# visual1 TO visual2
# visual2 START
# =======================================================================================================



# =======================================================================================================
# visual2 END
# visual2 TO visual3
# visual3 START
# =======================================================================================================



# =======================================================================================================
# visual3 END
# visual3 TO visual4
# visual4 START
# =======================================================================================================



# =======================================================================================================
# visual4 END
# visual4 TO visual5
# visual5 START
# =======================================================================================================



# =======================================================================================================
# visual5 END
# visual5 TO visual6
# visual6 START
# =======================================================================================================



# =======================================================================================================
# visual6 END
# visual6 TO stat1
# stat1 START
# =======================================================================================================



# =======================================================================================================
# stat1 END
# stat1 TO stat2
# stat2 START
# =======================================================================================================



# =======================================================================================================
# stat2 END
# stat2 TO stat3
# stat3 START
# =======================================================================================================



# =======================================================================================================
# stat3 END
# stat3 TO models
# models START
# =======================================================================================================



# =======================================================================================================
# models END
# models TO models_best
# models_best START
# =======================================================================================================



# =======================================================================================================
# models_best END
# models_best TO acquire
# acquire START
# =======================================================================================================

def acquire():
    '''
    Obtains the vanilla mass_shooters dataframe from the 'wrangle.py' file

    INPUT:
    NONE

    OUTPUT:
    mass_shooters = pandas dataframe
    '''
    mass_shooters = w.acquire_mass_shooters()
    return mass_shooters

# =======================================================================================================
# acquire END
# acquire TO prepare
# prepare START
# =======================================================================================================

def prepare():
    '''
    Obtains the prepared mass_shooters dataframe from the 'wrangle.py' file

    INPUT:
    NONE

    OUTPUT:
    prepped_mass_shooters = pandas dataframe
    '''
    prepped_mass_shooters = w.prepare_mass_shooters()
    return prepped_mass_shooters

# =======================================================================================================
# prepare END
# prepare TO wrangle
# wrangle START
# =======================================================================================================

def wrangle():
    '''
    Obtains the splitted mass_shooters dataframe from the 'wrangle.py' file

    INPUT:
    NONE

    OUTPUT:
    train = pandas dataframe with 70% of prepared mass_shooters dataframe
    validate = pandas dataframe with 20% of prepared mass_shooters dataframe
    test = pandas dataframe with 10% of prepared mass_shooters dataframe
    '''
    train, validate, test = w.wrangle_mass_shooters()
    return train, validate, test

# =======================================================================================================
# wrangle END
# =======================================================================================================