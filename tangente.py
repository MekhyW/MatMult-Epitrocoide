import numpy as np
from cmath import cos, sin

# Passo a ser utilizado para iterar os valores de gama(t)
dt = 0.001

t_verticais = []
t_horizontais = []

for t in np.arange(0,4*np.pi,dt):
    # Armazenando o valor de x' e y' a cada instante
    x_linha = -6 * np.sin(t) + 9 * np.sin(4.5 * t)
    y_linha = 6 * np.cos(t) - 9 * np.cos(4.5 * t)

    # Se valor de X for aproximadamente 0, o ponto é vertical
    if abs(x_linha) < 0.005:
        t_verticais.append(t)

    # Se o valor de Y for aproximadamente 0, o ponto é horizontal
    if abs(y_linha) < 0.005:
        t_horizontais.append(t)


print(f'Pontos verticais: {t_verticais}')
print(f'Pontos horizontais: {t_horizontais}')
