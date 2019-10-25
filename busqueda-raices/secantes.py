import math

cont = 0
error = 0
xi = 0
xn = 0
tol = 0
iter = 0

xant = 0

def main():
    secantes(2, 1, 0.00001, 7)

def secantes(xant, xi, tol, iter):
    #control de entrada:
    xant = xant
    fxi = funcion(xi)
    cont = 2
    error = tol + 1

    #procedimiento
    while error > tol and fxi != 0 and cont < iter:
        xn = funcionG(xant, xi)
        fxi = funcion(xn)
        error = abs(xn - xi)
        xant = xi
        xi = xn
        cont = cont + 1

    if fxi == 0:
        print(str(xi) + " Es presuntamente una raíz.")
    elif error < tol:
        print(str(xi) + " Es una aproximación a una raíz con tolerancia = " + str(tol))
    else:
        print("Fracaso en " + str(iter))

def funcion(x):
    #f(x) = e^(-(x^2)+1) - xsen(2x+3) - 4x + 4
    fx = math.exp( -pow(x,2)+1 ) - x*math.sin( 2*x+3 ) - 4*x + 4
    return fx

def funcionG(xant,x):
    #g(x) = xn − f(xn)*(xn − xn−1) / f(xn) − f(xn−1)

    gx = x - ( ( funcion(x)*( x - xant ) ) / ( funcion(x) - funcion(xant) ) )
    return gx

main()
