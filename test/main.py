import numpy as np
import matplotlib.pyplot as plt

# Stałe fizyczne
G = 6.67430e-11  # Stała grawitacji
m_earth = 5.972e24  # Masa Ziemi
r_earth = 6.371e6  # Promień Ziemi
q = 0.5  # Współczynnik oporu ośrodka
dt = 1.0  # Czas kroku

# Warunki początkowe
n = 1000  # Liczba punktów
x0 = np.zeros(n)
y0 = np.zeros(n)
vx0 = np.zeros(n)
vy0 = np.zeros(n)

for i in range(n):
    theta = np.random.uniform(0, 2*np.pi)
    r = np.random.uniform(0, r_earth*2)
    x0[i] = r * np.cos(theta)
    y0[i] = r * np.sin(theta)
    v0 = np.sqrt(G*m_earth/r)
    vx0[i] = -v0 * np.sin(theta)
    vy0[i] = v0 * np.cos(theta)

# Funkcja obliczająca wypadkową siłę
def force(x, y, vx, vy):
    r = np.sqrt(x**2 + y**2)
    F_gravity = -G * m_earth / r**2
    Fx = F_gravity * x / r
    Fy = F_gravity * y / r
    Fx -= q * vx / m_earth
    Fy -= q * vy / m_earth
    return Fx, Fy

# Symulacja ruchu
x = np.zeros((n, 1))
y = np.zeros((n, 1))
vx = np.zeros((n, 1))
vy = np.zeros((n, 1))

x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0

for i in range(1, 10000):
    Fx, Fy = force(x[i-1], y[i-1], vx[i-1], vy[i-1])
    vx[i] = vx[i-1] + dt * Fx / m_earth
    x[i] = x[i-1] + dt * vx[i]
    vy[i] = vy[i-1] + dt * Fy / m_earth
    y[i] = y[i-1] + dt * vy[i]

# Wykres trajektorii
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trajektoria ruchu punktów z oporem ośrodka i siłą grawitacji')
plt.show()