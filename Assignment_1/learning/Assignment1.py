"""
Assignment1
Student name: Nattapong Tangsatheanrapap
613040128-7
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# data from  https://www.kaggle.com/akpmpr/updated-netflix-stock-price-all-time
dataset = pd.read_csv("https://raw.githubusercontent.com/meangpu/ANN_year4term1/main/Assignment_1/mainData/netflix.csv")
TEST_SIZE = 0.2


# Using linear regression model
x = dataset['Low'].values.reshape(-1, 1)
y = dataset['High'].values.reshape(-1, 1)

# train 80% test 20%
model = LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=TEST_SIZE, random_state=0)


# train data
model.fit(x_train, y_train)


# test model
y_predict = model.predict(x_test)

# analysis model
# plt.scatter(x_test, y_test)
# plt.plot(x_test, y_predict, color="red", linewidth=2, label="the model")
# plt.legend(loc="upper left")  # location that show label
# plt.grid()
# plt.show()
#
# print(model.coef_)


# compare true data with predict data
dataFrame = pd.DataFrame({"Real": y_test.flatten(), "Predict": y_predict.flatten()})
print(f"MAE = {metrics.mean_absolute_error(y_test, y_predict)}")
print(f"MSE = {metrics.mean_squared_error(y_test, y_predict)}")
print(f"RMSE = {np.sqrt(metrics.mean_squared_error(y_test, y_predict))}")
print(f"Score(accuracy%) = {metrics.r2_score(y_test, y_predict) * 100}%")

# graph data error
print(dataFrame.head())
dataFrame1 = dataFrame.head(40)  # first 10 data
dataFrame1.plot(kind="bar", figsize=(16, 10))
plt.grid()
plt.show()


def describe_data_set():
    print(dataset.shape)
    print(dataset.describe())
    dataset.plot(x='Low', y='High', style=".")
    plt.title("high/low graph of netflix stock price")
    plt.xlabel('x - Low')
    plt.ylabel('y - High')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    describe_data_set()
    pass
