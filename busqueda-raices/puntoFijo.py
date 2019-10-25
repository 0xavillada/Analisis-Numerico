import math

xm=0
aux=0
cont = 0
error = 0
xi = 0
xn = 0
tol = 0
iter = 0

def main():
    puntoFijo(-1, 0.00001, 9)

def puntoFijo(xi, tol, iter):
    #control de entrada:
    fxi = funcion(xi)
    cont = 1
    error = tol + 1
    #procedimiento
    while error > tol and fxi != 0 and cont < iter:
        xn = funcionG(xi)
        fxi = funcion(xn)
        error = abs(xn - xi)
        xi = xn
        cont = cont + 1

    if fxi == 0:
        print(str(xi) + "Es raíz.")
    elif error < tol:
        print(str(xi) + "Es una aproximación a una raíz con tolerancia = " + str(tol))
    else:
        print("Fracaso en " + str(iter))


def funcion(x):
    #f(x) = e^(-2x-5) - x^2 + 2x
    fx = math.exp((-(3)*x) - 5)  - (pow(x, 2)) + 2*x
    return fx

def funcionG(x):
    #g(x) = (-e^(-2x-5) - x^2)/2
    gx = (-math.exp((-(3)*x) - 5)  - (pow(x, 2)))/2
    return gx


main()
