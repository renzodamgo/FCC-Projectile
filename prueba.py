import matplotlib.pyplot as pl
import numpy as np
import math

X0 = 0.00  # Posición inicial en X (m)
Y0 = 0.00  # Posición inicial en Y (m)
V0 = 65.0  # Rapidez inicial (m/s)
RADIO = 10.0  # Radio del proyectil (cm)
RADIO = RADIO * 10**(-2)  # Radio convertido de cm a m
CD = 0.500  # Coeficiente de resistencia
MASA = 0.140  # Masa del proyectil (kg)
ALPHA = 45  # Ángulo de lanzamiento (Grado sexagesimal)
ALPHA = math.radians(ALPHA)  # Ángulo convertido de grado sexagesimal a radian
RHO = 1.20  # Densidad del aire (kg/m^3)

G = 9.81  # Acelaración de la gravedad (m/s^2)
DELTA_T = 0.01  # Intervalo de tiempo (s)


def xposNoAir(t):
    return (X0 + v0x*t)


def yposNoAir(t):
    return (Y0 + v0y*t - 0.5*G*t**2)


v0x, v0y = V0*(math.cos(ALPHA)), V0*(math.sin(ALPHA))


def GraficaNoAir():
    arrX, arrY = [], []
    t = 0
    while True:
        auxX = xposNoAir(t)
        auxY = yposNoAir(t)
        if auxY < 0:
            break
        arrX.append(auxX)
        arrY.append(auxY)
        t += DELTA_T
    pl.plot(arrX, arrY, 'b', label='Sin resistencia del aire')


GraficaNoAir()
pl.show()
