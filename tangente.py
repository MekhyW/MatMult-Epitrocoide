import numpy as np
from cmath import cos, sin

# Passo a ser utilizado para iterar os valores de x(t)
dt = 0.001

t_verticais = []
t_horizontais = []

for t in np.arange(0,4*np.pi,dt):
    # Armazenando o valor de x e y a cada instante
    x = 6 * cos(t) - 2 * cos(4.5 * t)
    y = 6 * sin(t) - 2 * sin(4.5 * t)

    # Se valor de X for aproximadamente 0, o ponto é vertical
    if abs(x) < 0.005:
        t_verticais.append(t)

    # Se o valor de Y for aproximadamente 0, o ponto é horizontal
    if abs(y) < 0.005:
        t_horizontais.append(t)


print(f'Pontos verticais: {t_verticais}')
print(f'Pontos horizontais: {t_horizontais}')
