import matplotlib.pyplot as plt

def f(x):
    if x < -2: return -(x+5)**2+9
    elif -2 <= x < 0: return (1-(x+1)**2)**0.5
    elif 0 <= x < 5: return x
    elif x >= 5: return -(x-5)**0.5 + 5

X = [i/100 for i in range(-400, 700)]
Y = [f(x) for x in X]

plt.plot(X, Y)
plt.show()