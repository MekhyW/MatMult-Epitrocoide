import numpy as np

# Método da biseção
def bisection(f, a, b, tol=1e-5, maxiter=100):
    """
    Encontra a raiz de uma função f(x) em um intervalo [a, b]
    Inputs:
        f: função
        a: parte inferior do intervalo
        b: parte superior do intervalo
        tol: tolerancia
        maxiter: número máximo de iterações
    Outputs:
        x: ráiz da função
        e: erro
        n: número de iterações
    """
    n = 0
    x = (a + b) / 2
    e = np.inf
    while e > tol and n < maxiter:
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        x = (a + b) / 2
        e = abs(x - (a + b) / 2)
        n += 1
    return x, e, n

# Funções a serem encontradas as raizes

#k = -1

def k1(b):
    val = 6 * np.cos((7*np.pi)/8) * np.sin(b/2) - 2 * np.cos((63*np.pi)/16) * np.sin(2.25 * b)
    return val

# k = -2

def k2(b):
    val = 6 * np.cos((7*np.pi)/4) * np.sin(b/2) - 2 * np.cos((63*np.pi)/8) * np.sin(2.25 * b)
    return val

print(bisection(k1, 0, 4 * np.pi,maxiter=1000)[0])
print(bisection(k2, 0, 4 * np.pi,maxiter=1000)[0])