import matplotlib.pyplot as plt

def isConatin(x, y):
    return ((y <= -(1/8) * (x+9)**2 + 8) and ((y >= 7*((x+8)**2) + 1 and -9 <= x <= -8) or (-8 < x < -1)) and (y >= (x+1)**2/49)) or \
           ((y <= -(1/8) * (x-9)**2 + 8) and ((y >= 7*((x-8)**2) + 1 and 8 <= x <= 9) or (1 < x < 8)) and (y >= (x-1)**2/49)) or \
           (y >= 4*x**2 - 6 and y <= -4*x**2 + 2) or \
           (-2 <= x <= 0 and y == (-3/2) * x + 2) or \
           (0 <= x <= 2 and y == (3/2) * x + 2) or \
           (((-8 <= x < -2) and (y >= (1/3)*(x+5)**2-7) and (y <= (-1/16)*x**2)) or ((-2 <= x <= -1) and (y <= (-1/16)*x**2) and (y >= -2*(x+1)**2-2))) or \
           (((2 <= x < 8) and (y >= (1/3)*(x-5)**2-7) and (y <= (-1/16)*x**2)) or ((1 <= x <= 2) and (y <= (-1/16)*x**2) and (y >= -2*(x-1)**2-2)))

X = []
Y = []
for x in range(-20*25, 20*25):
    for y in range(-20*25, 20*25):
        if (isConatin(x/20, y/20)):
            X.append(x/20)
            Y.append(y/20)

plt.scatter(X, Y)
plt.show()