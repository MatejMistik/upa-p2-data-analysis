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

#data cleansing

df = pd.read_csv('./data/IT Salary Survey EU 2018.csv')
df

#find max value with pandas

print("Salary two years ago is: ",df['Salary two years ago'].idxmax())
print(df['Salary two years ago'].nlargest())

# Using DataFrame.loc[] property.
df2=df.loc[df['Salary two years ago'].idxmax()]
print(df2)

print(df.loc[df['Current Salary'].idxmax()])