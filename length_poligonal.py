import numpy as np

# Definindo a curva
def curve(t):
    x = 6 * np.cos(t) - 2 * np.cos(4.5 * t)
    y = 6 * np.sin(t) - 2 * np.sin(4.5 * t)
    return x, y

# Aproximando a curva a um poligono 
# A cada intervalo 0.001 do domínio , adiciona-se um ponto

dt = 0.001
interval = np.arange(0, 4 * np.pi, dt)

length = 0
for t in range(1,len(interval)):
    # Calculando a distancia entre o ponto atual e o anterior
    x1, y1 = curve(interval[t-1])
    x2, y2 = curve(interval[t])
    length += np.sqrt((x2-x1)**2 + (y2-y1)**2)
    
print(length)