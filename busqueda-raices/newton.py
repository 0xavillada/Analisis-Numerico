import math

cont = 0
error = 0
xi = 0
xn = 0
tol = 0
iter = 0

def main():
    newton(1.5, 0.00001, 4)

def newton(xi, tol, iter):
    #control de entrada:
    fxi = funcion(xi)
    cont = 1
    error = tol + 1
    #procedimiento
    while error > tol and fxi != 0 and cont < iter:

        xn = funcionG(xi)
        fxi = funcion(xn)
        error = abs((xn - xi)/xn)
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

def derivadaFuncion(x):
    #f'(x) = -2 e^(1 - x^2) x - sin(2 x + 3) - 2 x cos(2 x + 3) - 4
    Fx = -2 * math.exp(1 - (pow(x,2))) * x - math.sin( 2*x+3 ) - 2*x*math.cos( 2*x+3 ) - 4
    return Fx

def funcionG(x):
    #g(x) = x - ( f(x)/f'(x) )
    fx = funcion(x)
    Fx = derivadaFuncion(x)
    gx = x - (fx/Fx)
    return gx

main()
