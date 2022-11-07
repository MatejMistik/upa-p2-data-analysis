# Path: upa_analyzation_tests.py
import warnings
warnings.filterwarnings("ignore")

import os
for dirname, _, filenames in os.walk('./data/'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('./data/IT Salary Survey EU  2020.csv')
df

#find max value with pandas


#series tests


ser = df["Annual bonus+stocks one year ago. Only answer if staying in same country"].astype(float)
print(ser.max())

