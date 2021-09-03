import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 60, 100)

m = 2
c = 5
y = m * x + c

plt.title("Display the graph")

plt.plot(x, y, "-r", label="y=mx+c")

# plt.scatter(x, y, label="y=mx+c")

plt.legend(loc="upper left")  # location that show label
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
