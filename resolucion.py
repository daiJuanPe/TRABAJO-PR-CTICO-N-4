import random

# 1)
"""
for x in range (0, 101):  # el 0 indica el inicio y el 101 el fin, sin incluir el 101
    print(x)

# 2)
cantidadDeDigitos = 0
numero = int(input("Ingrese un número entero para saber la cantidad de dígitos que contiene:"))

numero = abs(numero) # si el usuario ingresa un numero negativo, con abs() lo paso a positivo

if numero == 0:
    cantidadDeDigitos = 1
else:
    while numero > 0:
        numero //= 10   # es mas corto que usar mod. // es división entera, divide i descarta los decimales, redondeando hacia abajo.
                        # en este caso esta dividiendo por 10 y guardando solo la parte entera del resultado. elimina el ultimo digito de un n° entero
        cantidadDeDigitos += 1

print(f"La cantidad de dígitos que contiene el número ingresado es {cantidadDeDigitos}")

# 3)

sumatoria = 0
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

for x in range(valor1, valor2 + 1):
    sumatoria += x

print(f"La suma entre los números ingresados es: {sumatoria}")

# 4)
numero = 1
sumatoria = 0
while numero != 0 :
    numero = int(input("Ingrese un número. Para terminar ingrese 0"))
    sumatoria += numero

print(f"La suma de los números ingresados es: {sumatoria}")

# 5)
num = 10
aleatorio = 0

while num != aleatorio:
    num = int(input("Ingrese un número entre 0 y 9"))
    aleatorio = random.randint(0,9)
    print(f"Numero aleatorio: {aleatorio} , número del usuario: {num}")

print("GANASTE!! El número ingresado es igual al aleatorio!")


# 6)

# Opción 1: Rango con paso -2 (solo pares, eficiente)
#for x in range(100, -1, -2):  # Desde 100 hasta 0, restando 2
#    print(x)

# Opción 2: Filtrado con if (para entender el proceso)
for x in range(100, -1, -1):  # Desde 100 hasta 0, restando 1
    if x % 2 == 0:             # Si es par
        print(f"Número par: {x}")

# 7)
sumatoria = 0
num = int(input("Ingrese un número entero positivo"))

while num <= 0: 
    num = int(input("ERROR! Ingrese un número entero positivo"))

for x in range(0, num+1):
    sumatoria += x

print(f"La suma de los números es: {sumatoria}")

# 8)
esPar=0
esImpar=0
negativo=0
positivo=0

for i in range(0, 101):
    num = int(input("Ingrese un número entero: "))

    if num % 2 == 0:
        esPar += 1
    else:
        esImpar += 1

    if num < 0:
        negativo += 1
    elif num > 0:
        positivo += 1

print(f"Cantidad de números pares: {esPar}")
print(f"Cantidad de números impares: {esImpar}")
print(f"Cantidad de números positivos: {positivo}")
print(f"Cantidad de números negativos: {negativo}")



# 9)
sumatoria = 0

for x in range(0, 101):
    num = int(input("Ingrese un número entero:"))
    sumatoria += num

media = sumatoria / 100

print(f"La media de los números ingresados es: {media}")



# 10)

numero = int(input("Ingrese un número entero: "))

# Invertir los dígitos
numeroInvertido = 0
while numero > 0:
    # Obtener el último dígito
    digito = numero % 10
    # Agregar el dígito al número invertido
    numeroInvertido = numeroInvertido * 10 + digito
    # Quitar el último dígito del número original
    numero = numero // 10

print("El número invertido es:", numeroInvertido)

"""
