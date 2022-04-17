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

# Calculando a área do poligono ao somar as areas de cada triangulo
area = 0
for t in range(1,len(interval)):
    # Selecionando os pontos atuais e anteriores
    x1, y1 = curve(interval[t-1])
    x2, y2 = curve(interval[t])
    x_0, y_0 = [0,0] # Origem do sistema de coordenadas
    #Lados do triangulo
    l12 = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    l02 = np.sqrt((x2-x_0)**2 + (y2-y_0)**2)
    l01 = np.sqrt((x1-x_0)**2 + (y1-y_0)**2)
    # semiperimetro
    s = (l12 + l02 + l01)/2
    # Area do triangulo
    area += np.sqrt(s*(s-l12)*(s-l02)*(s-l01))

print(area)