import math
ecuaciones = []
variables = []
valores_iniciales = []
cifras_sig = 0
maximo_iter = 0
n_incognitas = 0
error = 1

lambda_value = 1

print("Numero de incognitas:")
try:
    n_incognitas = int(input())
except:
    print("> ERROR: Entrada invalida")
    exit(1)

for ecuacion_index in range(n_incognitas):
    for variable in range(n_incognitas+1):
        try:
            if variable == n_incognitas:
                print("Varaiable A de la ecuacion numero"+str(ecuacion_index+1)+":")
                variables.append(float(input()))
                break
            print("Varaiable X"+str(variable+1)+" de la ecuacion numero"+str(ecuacion_index+1)+":")
            variables.append(float(input()))
        except:
            print("> ERROR: Entrada invalida")
            exit(1)
    ecuaciones.append(variables)
    variables = []

for iniciales in range(n_incognitas):
    try:
        print("Valor inicial para X"+str(iniciales+1)+":")
        valores_iniciales.append(float(input()))
    except:
        print("> ERROR: Entrada invalida")
        exit(1)

try:
    print("Cifras significativas:")
    cifras_sig = int(input())
    print("Maximo iteraciones:")
    maximo_iter = int(input())
    print("Lambda de relajacion:")
    lambda_value = float(input())

except:
    print("> ERROR: Entrada invalida")
    exit(1)

cifras_sig = 0.5*(10**(-cifras_sig))
iteraciones = 0

while error > cifras_sig:
    if iteraciones > maximo_iter:
        print("> ERROR: Se llegó al maximo de iteraciones!")
        exit(1)
    
    nueva_fila = []
    for x in range(n_incognitas):
        nueva_fila.append(valores_iniciales[x])

    for variables_index in range(n_incognitas):
        temp = 0
        for demas_variables in range(n_incognitas):
            if demas_variables == variables_index:
                continue
            else:
                temp += (-1*(ecuaciones[ variables_index][demas_variables]*nueva_fila[demas_variables]))

        nueva_fila[variables_index] = ( ecuaciones[variables_index][n_incognitas] + temp) / ecuaciones[variables_index][variables_index]

        # RELAJACION
        nueva_fila[variables_index] = lambda_value * nueva_fila[variables_index] + (1 - lambda_value )* valores_iniciales[variables_index]
    
    # ERROR RELATIVO NORMA MAXIMO---------------------------------------
    error_list_diff=[]
    for i in range(n_incognitas):
        error_list_diff.append(abs(nueva_fila[i]-valores_iniciales[i]))
    error = max(error_list_diff) / max(map(abs,nueva_fila))
    # ------------------------------------------------------------------
    
    # ERROR RELATIVO
    """
    sumatoria = 0
    for i in range(n_incognitas):
        sumatoria += (nueva_fila[i]-valores_iniciales[i])**2
        error_list_diff.append(abs(nueva_fila[i]-valores_iniciales[i]))
    sumatoriaX = 0
    for i in range(n_incognitas):
        sumatoriaX += nueva_fila[i]**2
    error = math.sqrt(sumatoria) / math.sqrt(sumatoriaX)
    """

    valores_iniciales = nueva_fila
    iteraciones +=1
    #print("Valores de Xn: ", valores_iniciales)
    #print("Iteracion numero: ",iteraciones)
    #print("Error relativo:",error)

print("\n> Iteracion numero:",iteraciones)
print("> Valores de Xn: ")
for x in range(n_incognitas):
    print("X"+str(x+1)+" =",valores_iniciales[x])

print("> Toleracia: +-",error)