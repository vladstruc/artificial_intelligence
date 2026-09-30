
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

students = pd.read_csv("Мини-исследование датасета/online_shoppers_intention.csv")
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 12400)
print(students.shape)
print(students.info())
print(students.isnull().any())
print(students.isnull().any().any())
print(students.describe())
desc = students['OperatingSystems'].describe()
Q1 = students['OperatingSystems'].quantile(0.25)
Q3 = students['OperatingSystems'].quantile(0.75)
print(Q1)
print(Q3)

IQR = Q3 - Q1
print(IQR)
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR
print(lower)
print(upper)
stds = students[(students['OperatingSystems']<lower) | (students['OperatingSystems'] > upper) ]
print(stds) 
