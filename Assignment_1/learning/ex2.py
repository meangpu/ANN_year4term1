import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
rng = np.random

#  จำลองข้อมูล
x = np.random.rand(100)*10
c = rng.randn(100)  # randn is Negative or positive // rand is only positive
y = 2 * x + c

# linear regression model
model = LinearRegression()

x_new = x.reshape(-1, 1)

# train
model.fit(x_new, y)

print(model.score(x_new, y))  # show how good model is -- 0.97 is 97% accurate
print(model.coef_)  # ทำนายค่า m


# test model
xfit = np.linspace(-1, 11, 90)  # 90 value
xfit_new = xfit.reshape(-1, 1)  # reshape into 2d array

yfit = model.predict(xfit_new)

# analysis model


plt.title("Display the graph")
plt.scatter(x, y, label="y=mx+c")
plt.legend(loc="upper left")  # location that show label
plt.plot(xfit, yfit, "-r")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
