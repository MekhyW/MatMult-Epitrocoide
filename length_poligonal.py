import numpy as np

# Definindo a curva
def curva(t):
    x = 6 * np.cos(t) - 2 * np.cos(4.5 * t)
    y = 6 * np.sin(t) - 2 * np.sin(4.5 * t)
    return (x, y)

# Aproximando a curva a um poligono 
# A cada intervalo 0.001 do domínio , adiciona-se um ponto

dt = 0.001
intervalo = np.arange(0, 4 * np.pi, dt)

comprimento = 0
for indice in range(1, len(intervalo)):
    # Calculando a distancia entre o ponto atual e o anterior
    x1, y1 = curva(intervalo[indice-1])
    x2, y2 = curva(intervalo[indice])
    comprimento_diff = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    comprimento += comprimento_diff
    
print("O comprimento da curva é: {}".format(comprimento))