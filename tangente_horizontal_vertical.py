from cmath import cos, sin
import math

t = 0
dt = 0.0001
t_upper_limit = 4*math.pi
casos_horizontal = []
casos_vertical = []
while t < t_upper_limit:
    a = (-6)*sin(t)
    b = 9*sin(9*t/2)
    c = 6*cos(t)
    d = -9*cos(9*t/2)
    if abs(a+b) > dt and abs(c+d) < dt:
        casos_horizontal.append(t)
    if abs(a+b) < dt and abs(c+d) > dt:
        casos_vertical.append(t)
    t += dt
print("Casos de tangente horizontal: ", casos_horizontal)
print("Casos de tangente vertical: ", casos_vertical)