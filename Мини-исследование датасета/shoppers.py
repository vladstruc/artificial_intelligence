
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

students = pd.read_csv("Мини-исследование датасета/online_shoppers_intention.csv")

print(students.shape)
print(students.head())
print(students.info())

print(students.dtypes)

print(students.memory_usage().sum())

print(students.isnull().sum())

print(students.describe())

print(students.isna().any().any())

print(students.corr(numeric_only=True))

st = students.corr(numeric_only=True)
sns.heatmap(st, annot=True,cmap='coolwarm',fmt='.2f')
print(st)
plt.title('Тепловая карта корреляции')
plt.show()

student_num = students.select_dtypes(include=[np.number])
sns.boxplot(data=student_num,width =1000000)
plt.title('Box plot для столбцов')
plt.show()