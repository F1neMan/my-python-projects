import numpy as np
import pandas as pd

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

# Генерация выборки
# features - пространство объектов, output - пространство ответов, coef - коэфы которые использовала модель

features, output, coef = make_regression(
    n_samples=15000,  # кол-во элементов
    n_features=9,  # кол-во признаков
    n_informative=5,  # кол-во информативных признаков
    n_targets=1,  # кол-во целевых признаков
    noise=1,  # шум
    coef=True
)
'''
# pd.DataFrame - представление в памяти листа Excel с помощью языка программирования Python
X = pd.DataFrame(features, columns=['Фактор_1', 'Фактор_2', 'Фактор_3', 'Фактор_4', 'Фактор_5'])
y = pd.DataFrame(output, columns=['Результат'])

df = pd.concat([X, y], axis=1)  # axis=1 приклеивает справа
df.describe() #статистика датафрейма
df.info()
'''

model = LinearRegression()  # инициализируем модель линейной регрессии
model.fit(features, output)  # обучаем модель линейной регрессии

for i in range(len(model.coef_)):
    print(model.coef_[i])

'''print(model.coef_[0])
print(model.coef_[1])
print(model.coef_[2])
print(model.coef_[3])
print(model.coef_[4])
print(model.coef_[5])
print(model.coef_[6])
print(model.coef_[7])
print(model.coef_[8])'''

# print(coef) если нужно сравнить используемые с полученными

print(model.predict([[0, 0, 0, 0, 0, 0, 0, 0, 0]]))
