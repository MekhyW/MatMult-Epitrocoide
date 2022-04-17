import numpy as np
from scipy.integrate import trapz

# Definindo o vetor tangente
def gama_linha(t):
    x_linha = -6 * np.sin(t) + 9 * np.sin(4.5 * t)
    y_linha = 6 * np.cos(t) - 9 * np.cos(4.5 * t)
    return x_linha, y_linha

# Intervalo dos pontos da curva:
dt = 0.001
interval = np.arange(0, 4 * np.pi, dt)

#Preenchendo os valores da função a ser integrada
Y = []
for t in interval:
    x, y = gama_linha(t)
    val = np.sqrt(x**2 + y**2)
    Y.append(val)

# Biblioteca para aplicar o metodo de trapezio
inte = trapz(Y,x=interval)

print(inte)