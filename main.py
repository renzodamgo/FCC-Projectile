import math
from matplotlib import pyplot
# import sympy

C_d = 0.5
p = 1.200
radio = 0.10
A = math.pi * pow(radio, 2)
y_max = 0
v0 = 50
theta = (45*math.pi) / 180
m = 0.1
X = []
Y = []
X_r = []
Y_r = []


class ball:
    def __init__(self, v_o, angulo, masa, C_d, p, A):
        self.v_o = v_o
        self.v = v_o
        self.angulo = angulo
        self.v_x = v_o*math.cos(angulo)
        self.v_y = v_o*math.sin(angulo)
        self.m = masa
        self.dt = 0.0001
        self.t = 0
        self.g = -9.81
        self.F = self.m*self.g
        self.x = 0
        self.y = 0
        self.k = 0.5*C_d*p*A
        self.c = v_o-((self.m*-self.g)/self.k)

    def move(self):
        self.v_x = self.v_x
        # self.v_y = self.v_y+self.g*self.dt
        self.v_y = self.v_y+self.g*self.dt
        self.x = self.x + self.v_x*self.dt
        self.y = self.y + self.v_y*self.dt
        self.t = self.t + self.dt
        return self.x, self.y

    def move_r(self):

        self.v = (self.m*-self.g)/self.k + self.c * \
            pow(math.e, (-self.k/self.m)*self.t)
        print(self.v)
        self.v_x = self.v*math.cos(self.angulo)
        self.v_y = self.v*math.sin(self.angulo)
        self.x = self.x + self.v_x*self.dt
        self.y = self.y + self.v_y*self.dt
        self.t = self.t + self.dt
        return self.x, self.y


ball_o = ball(v0, theta, m, C_d, p, A)

ball_r = ball(v0, theta, m, C_d, p, A)


def max_H(v, angle):
    a = (v**2)*(math.sin(angle)**2)
    b = 2*9.81
    H = a/b
    return H


while True:
    x, y = ball_o.move()

    if y < 0:
        break
    if y >= y_max:
        y_max = y
    X.append(x)
    Y.append(y)


for _ in range(10):
    x, y = ball_r.move_r()

    # if y < 0:
    #     break

    X_r.append(x)
    Y_r.append(y)

print(max_H(v0, theta))
print(y_max)

pyplot.plot(X_r, Y_r)
# pyplot.axis('square')
pyplot.savefig("img/parabolico_img.png")
pyplot.show()
