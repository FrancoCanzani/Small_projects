
print("""Bienvenido a la calculadora, estas son las acciones que puede llevar a cabo:

1. suma
2. resta
3. multiplicacion
4. division\n""")

num_1 = 0
num_2 = 0

accion = input("Ingrese el número correspondiente a la acción que desea llevar a cabo: ")


if accion in ('1', '2', '3', '4'):
    try:
        num_1 = int(input("Ingrese el primer número: "))
        num_2 = int(input("ingrese el segundo número: "))

    except:
        print("No ingresó ningún número.")


def suma(num_1, num_2):
    return num_1 + num_2


def resta(num_1, num_2):
    return num_1 - num_2


def multiplicacion(num_1, num_2):
    return num_1 * num_2


def division(num_1, num_2):
    return num_1 / num_2


constant = "El resultado es "

if accion == '1':
    print(constant + str(suma(num_1, num_2)))
if accion == '2':
    print(constant + str(resta(num_1, num_2)))
if accion == '3':
    print(constant + str(multiplicacion(num_1, num_2)))
if accion == '4':
    print(constant + str(division(num_1, num_2)))