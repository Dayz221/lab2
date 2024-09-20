import matplotlib.pyplot as plt

def isConatin(x, y):
    return ((-3 <= x < 0) and (y <= (9-x**2)**0.5+3) and (y >= x**2-6) and (y >= x)) or \
           ((0 <= x <= 3) and (y <= (9-x**2)**0.5+3) and (y >= x**2-6) and (y >= -x))

X = []
Y = []
for x in range(-80, 80):
    for y in range(-120, 120):
        if (isConatin(x/20, y/20)):
            X.append(x/20)
            Y.append(y/20)

plt.scatter(X, Y)
plt.show()