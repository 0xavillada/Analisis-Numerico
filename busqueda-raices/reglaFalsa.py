import math

xm=0
aux=0
cont = 0
error = 0
xi = 0
xs = 0
xm = 0
tol = 0
iter = 0

def main():
    reglaFalsa(2,3,0.0005,35)

def reglaFalsa(xi, xs, tol, iter):
    #control de entrada:
    fxi = funcion(xi)
    fxs = funcion(xs)
    if fxi == 0:
        print(str(xi) + "Es una raíz.")
    elif fxs == 0:
        print(str(xs) + "Es una raíz.")
    elif fxi * fxs < 0:
        #control de proceso
        xm = xi - ((fxi*(xs-xi)/(fxs-fxi)))
        fxm = (funcion(xm))
        cont = 1
        error = tol + 1
        while error > tol and fxm != 0 and cont < iter:
            if fxi * fxm < 0:
                xs = xm
                fxs = fxm
            else:
                xi = xm
                fxi = fxm
            
            aux = xm
            xm = ((xi + xs)/2)
            fxm = (funcion(xm))
            error = abs(xm - aux)
            cont = cont + 1
        
        if fxm == 0:
            print(str(xm) + "Es raíz.")
        elif error < tol:
            print(str(xm) + "Es una aproximación a una raíz con tolerancia = " + str(tol))
        else:
            print("Fracaso en " + str(iter))
    else:
        print("El intervalo es inadecuado.")


def funcion(x):
    """# f(x) = x^2 - 3
    fx = pow(x, 2) - 3
    """
    #f(x) = e^(3x-12) + xcos(3x) -x^2 + 4
    fx = math.exp((3*x) - 12) + (x*math.cos(3*x)) - (pow(x, 2)) + 4
    return fx


main()




