import random
import itertools
import time

def password_generator():
    letras_minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letras_mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    simbolos = ['.', '-', '/', '_', ',']

    try:
        minus = int(input("Introduzca la cantidad de minusculas que debe llevar su contraseña: "))
        mayus = int(input("Introduzca la cantidad de mayusculas que debe llevar su contraseña: "))
        num = int(input("Introduzca la cantidad de numeros que debe llevar su contraseña: "))
        simb = int(input("Introduzca la cantidad de simbolos que debe llevar su contraseña: "))

        minusculas = random.choices(letras_minusculas, weights=None, cum_weights=None, k=minus)
        mayusculas = random.choices(letras_mayusculas, weights=None, cum_weights=None, k=mayus)
        numeros_2 = random.choices(numeros, weights=None, cum_weights=None, k=num)
        simbolos_2 = random.choices(simbolos, weights=None, cum_weights=None, k=simb)

        cadena = list(itertools.chain(minusculas, mayusculas, numeros_2, simbolos_2))
        password = ''.join(map(str, cadena))
        print(f'Su contraseña es: {password}')

    except:
        print('Error. Intentelo nuevamente ingresando otros valores.')