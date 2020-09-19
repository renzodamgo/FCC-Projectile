import math
from matplotlib import pyplot


class ball:
    def __init__(self, v_o, angulo, masa):
        self.v_x = v_o*math.cos(angulo)
        self.v_y = v_o*math.sin(angulo)
        self.m = masa
        self.dt = 0.0001
        self.t = 0
        self.g = -9.81
        self.F = self.m*self.g
        self.x = 0
        self.y = 0

    def move(self):
        self.v_x = self.v_x
        self.v_y = self.v_y+(self.F/self.m)*self.dt
        self.x = self.x + self.v_x*self.dt
        self.y = self.y + self.v_y * self.dt
        self.t = self.t + self.dt
        return self.x, self.y


y_max = 0
v0 = 8
theta = (45*math.pi) / 180
m = 0.5
X = []
Y = []
ball = ball(v0, theta, m)


def max_H(v, angle):
    a = (v**2)*(math.sin(angle)**2)
    b = 2*9.81
    H = a/b
    return H


while True:
    x, y = ball.move()

    if y < 0:
        break
    if y >= y_max:
        y_max = y
    X.append(x)
    Y.append(y)

print(max_H(v0, theta))
print(y_max)

pyplot.plot(X, Y)
pyplot.axis('square')
pyplot.show()
