
import pandas as pd

import pandas as pd
import numpy as np
import sys

from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.metrics import roc_auc_score, f1_score
shoppers = pd.read_csv("Мини-исследование датасета/online_shoppers_intention.csv")
pd.set_option('display.max_columns', None)
print("Анализ датасета на нулевые значения и типы колонок")
print(shoppers.info())
print(shoppers.isnull().any())
print(shoppers.isnull().any().any())
signs = shoppers.drop('Revenue',axis=1)
target = shoppers['Revenue']
signs_train, signs_test, target_train, target_test = train_test_split(signs, target,test_size=0.3, random_state=42, stratify=target)
print(f"Число положительных значенийв в обучающей выбороке: {np.count_nonzero(target_train==True)}")
print(f"Число отрицательных значений в обучающей выборкеЖ {np.count_nonzero(target_train==False)}")
if((np.count_nonzero(target_train==True) > np.count_nonzero(target_train==False)) or((np.count_nonzero(target_train==True) < np.count_nonzero(target_train==False)))):
   print("Имеется дисбаланс классов в тестовой выбороке")
le = LabelEncoder()
signs_train['Month'] = le.fit_transform(signs_train['Month'])
print(signs_train['Month'].dtypes)
signs_train['VisitorType'] = le.fit_transform(signs_train['VisitorType'])
print(signs_train['VisitorType'].dtypes)
signs_test['Month'] = le.fit_transform(signs_test['Month'])
print(signs_test['Month'].dtypes)
signs_test['VisitorType'] = le.fit_transform(signs_test['VisitorType'])
print(signs_test['VisitorType'].dtypes)
scaler = StandardScaler()
signs_train = scaler.fit_transform(signs_train)
signs_test = scaler.transform(signs_test)
model_logistic_regression = LogisticRegression()
model_logistic_regression.fit(signs_train, target_train)
target_predict_logistic_regression_train = model_logistic_regression.predict(signs_train)

target_predict_logistic_regression_test = model_logistic_regression.predict(signs_test)
np.set_printoptions(threshold=sys.maxsize)
print("Результаты обучения модели LogisticRegression")
print(f"Значение метрики ROC для тестовой выборки:{roc_auc_score(target_test, target_predict_logistic_regression_test)}")
print(f"Значение метрики f1 для тестовой выборки:{f1_score(target_test, target_predict_logistic_regression_test)}")
print(f"Значение метрики f1 для обучающей выборки:{f1_score(target_train, target_predict_logistic_regression_train)}")
if (f1_score(target_train, target_predict_logistic_regression_train)-f1_score(target_test, target_predict_logistic_regression_test)> 0.1):
    print("Заметный разрыв - есть проблема переобучения модели")
baseline_model = DummyClassifier(strategy='most_frequent')
baseline_model.fit(signs_train, target_train)
target_predict_baseline_train = baseline_model.predict(signs_train)
target_predict_baseline_test = baseline_model.predict(signs_test)
print("Результаты обучения модели Baseline")
print(f"Значение метрики ROC для тестовой выборки:{roc_auc_score(target_test, target_predict_baseline_test)}")
print(f"Значение метрики f1 для тестовой выборки:{f1_score(target_test, target_predict_baseline_test)}")
print(f"Значение метрики f1 для обучающей выборки::{f1_score(target_train, target_predict_baseline_train)}")
if (f1_score(target_train, target_predict_baseline_train)-f1_score(target_test, target_predict_baseline_test)> 0.1):
    print("Заметный разрыв - есть проблема переобучения модели")

decision_tree_model = DecisionTreeClassifier(max_depth=6)
decision_tree_model.fit(signs_train, target_train)
target_predict_dec_tree_train = decision_tree_model.predict(signs_train)
target_predict_dec_tree_test = decision_tree_model.predict(signs_test)
print("Результаты обучения модели DecisionTree")
print(f"Значение метрики ROC для тестовой выборки: {roc_auc_score(target_test, target_predict_dec_tree_test)}")
print(f"Значение метрики f1 для тестовой выборки:  {f1_score(target_test, target_predict_dec_tree_test)}")
print(f"Значение метрики f1 для обучающей выборки: {f1_score(target_train, target_predict_dec_tree_train)}")
if(f1_score(target_train, target_predict_dec_tree_train)-f1_score(target_test, target_predict_dec_tree_test)>0.1):
        print("Заметный разрыв - есть проблема переобучения модели")

random_forest_model = RandomForestClassifier(max_depth=6)
random_forest_model.fit(signs_train, target_train)
target_random_forest_test = random_forest_model.predict(signs_test)
target_random_forest_train = random_forest_model.predict(signs_train)

print("Результаты обучения модели RandomForest")
print(f"Значение метрики ROC для тестовой выборки: {roc_auc_score(target_test, target_random_forest_test)}")
print(f"Значение метрики f1 для тестовой выборки:{f1_score(target_test, target_random_forest_test)}")
print(f"Значение метрики f1 для обучающей выборки:{f1_score(target_train, target_random_forest_train)}")
if(f1_score(target_train, target_random_forest_train)-f1_score(target_test, target_random_forest_test)>0.1):
        print("Заметный разрыв - есть проблема переобучения модели")