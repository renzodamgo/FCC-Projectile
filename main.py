import math
from matplotlib import pyplot


class ball:
    def __init__(self, v_o, angulo, masa):
        self.v_x = v_o*math.cos(angulo)
        self.v_y = v_o*math.sin(angulo)
        self.m = masa
        self.dt = 0.01
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


v0 = 8
theta = (30*math.pi) / 180
m = 0.5
X = []
Y = []
ball = ball(v0, theta, m)
for _ in range(100):
    x, y = ball.move()
    X.append(x)
    Y.append(y)


pyplot.plot(X, Y)

pyplot.show()
