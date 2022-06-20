from math import *

t1 = [4*pi*(0 + (39/2573)), 4*pi*(0 - (39/2573)), 4*pi*(1 + (39/2573)), 4*pi*(1 - (39/2573)), 
4*pi*(0 + (137/1546)), 4*pi*(0 - (137/1546)), 4*pi*(1 + (137/1546)), 4*pi*(1 - (137/1546)), 
4*pi*(0 - (555/3928)), 4*pi*(1 - (555/3928))]

t2 = [0, 4*pi, 4*pi*(0 + (202/4155)), 4*pi*(0 - (202/4155)), 4*pi*(1 + (202/4155)), 4*pi*(1 - (202/4155)), 
4*pi*(0 + (456/3677)), 4*pi*(0 - (456/3677)), 4*pi*(1 + (456/3677)), 4*pi*(1 - (456/3677))]

for valor in t1:
    ponto = [(-6 * sin(valor)) + (9 * sin(4.5*valor)), 0]
    print("Ponto de tangencia horizontal: {}".format(ponto))

for valor in t2:
    ponto = [0, (6 * cos(valor)) - (9 * cos(4.5*valor))]
    print("Ponto de tangencia vertical: {}".format(ponto))