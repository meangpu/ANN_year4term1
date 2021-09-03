import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
rng = np.random

#  จำลองข้อมูล
x = np.random.rand(10)*10
c = rng.randn(10)  # randn is Negative or positive // rand is only positive
y = 2 * x + c

# linear regression model
model = LinearRegression()

print(x)
x_new = x.reshape(-1, 1)
print(x_new)
