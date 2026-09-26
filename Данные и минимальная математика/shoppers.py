
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

students = pd.read_csv("Данные и минимальная математика/online_shoppers_intention.csv")



month_order = ['Feb','Mar','May','June','Jul','Aug','Sep','Oct','Nov','Dec']
students['Month'] = pd.Categorical(students['Month'],categories=month_order, ordered=True)

plt.figure()
monthly_mean = students.groupby(["Month"])["BounceRates"].mean()
monthly_mean_graph = monthly_mean.plot(marker ='o' , linestyle='-', figsize=(12,6), color = 'blue')
monthly_mean_graph.set_xlabel('Месяц',fontsize=14)
monthly_mean_graph.set_ylabel('Математическое ожидание', fontsize=14)
monthly_mean_graph.set_title('Среднее число отказов по месяцам', fontsize=14)
monthly_mean_graph.grid(axis='both', alpha=0.6)
plt.figure()
monthly_var = students.groupby(["Month"])["BounceRates"].var()
print(monthly_var)
monthly_var_graph = monthly_var.plot(marker ='o' ,linestyle='-', figsize=(12,6), color = 'red')
monthly_var_graph.set_xlabel('Месяц',fontsize=14)
monthly_var_graph.set_ylabel('Дисперсия', fontsize=14)
monthly_var_graph.set_title('Дисперсия числа отказов по месяцам', fontsize=14)
monthly_var_graph.grid(axis='both', alpha=0.6)
plt.figure()
monthly_var = students.groupby(["Month"])["BounceRates"].median()
print(monthly_var)
monthly_var_graph = monthly_var.plot(marker ='o' ,linestyle='-', figsize=(12,6), color = 'green')
monthly_var_graph.set_xlabel('Месяц',fontsize=14)
monthly_var_graph.set_ylabel('Медиана', fontsize=14)
monthly_var_graph.set_title('Медиана числа отказов по месяцам', fontsize=14)
monthly_var_graph.grid(axis='both', alpha=0.6)
students['ExitRates_new'] = students['ExitRates']*100 

monthly_corr = students.groupby(["Month"])[["BounceRates","ExitRates","PageValues"]].corr()
sns.heatmap(monthly_corr, annot=True,cmap='coolwarm',fmt='.2f')
print(monthly_corr)
plt.title('Тепловая карта корреляции')
plt.show()