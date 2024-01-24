import matplotlib.pyplot as plt
from scipy.stats import linregress

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = linregress(x, y)

def myfunc(x):
    return slope * x + intercept

myModel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, myModel, label='Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r**2)
