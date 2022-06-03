from sys import stdin
from time import process_time as timer
# import threading


def lectura():
    start = timer()
    nCasos = int(stdin.readline())
    while nCasos != 0:
        linea = stdin.readline().replace('\n', '')
        procesar(linea)
        nCasos -= 1

    elapsed_time = timer() - start
    print("Time: %.10f" % elapsed_time)


def lecturaConArchivo():
    start = timer()
    file = open("jijijija.in", "r")
    # file = open("500000.in", "r")
    nCasos = int(file.readline())
    while nCasos != 0:
        linea = file.readline().replace('\n', '')
        procesar(linea)
        # procesarCifrando(linea)
        nCasos -= 1
    elapsed_time = timer() - start
    print("Time: %.10f" % elapsed_time)


def procesar(entrada):
    letras_repeticiones = {}

    for n in range(1, len(entrada)+1):
        actual = entrada[-n]
        if actual in letras_repeticiones:
            letras_repeticiones[actual] += 1
        else:
            letras_repeticiones[actual] = 1

    letras_cantidad = {}
    orden_eliminacion = ""
    cantidad_palabra = 0

    tamanio = len(letras_repeticiones)
    for letra in letras_repeticiones:
        veces = letras_repeticiones[letra]//(tamanio)
        tamanio -= 1
        letras_cantidad[letra] = veces
        cantidad_palabra += veces
        orden_eliminacion = letra + orden_eliminacion

    palabra_original = entrada[0:cantidad_palabra]
    funciona = True

    for i in range(cantidad_palabra):
        letra = palabra_original[i]
        if letras_cantidad[letra] > 0:
            letras_cantidad[letra] -= 1
        else:
            print("NO EXISTE")
            funciona = False
            break

    cifrada = cifrarCadena(palabra_original, list(orden_eliminacion))

    if funciona and cifrada == entrada:
        salida = palabra_original + " " + orden_eliminacion
        print(salida)
    else:
        print("NO EXISTE")


def procesarCifrando(entrada):

    letras_repeticiones = {}
    orden = []

    for n in range(1, len(entrada)+1):
        actual = entrada[-n]
        if letras_repeticiones.get(actual) is not None:
            letras_repeticiones[actual] += 1
        else:
            letras_repeticiones[actual] = 1
            orden.append(actual)

    # print(orden)

    for i in range(len(orden), len(entrada)):
        palabra = entrada[:i]

        # print("palabra", palabra)

        cifrada = cifrarCadena(palabra, orden)
        # print("cifrada", cifrada)
        if cifrada == entrada:
            print(cifrada, ''.join(orden[::-1]))
            break
        elif i == len(entrada)-1:
            print("NO EXISTE")



def cifrarCadena(cadena: str, letras: list):
    cadenaCopy = cadena
    index = 0
    # print("tamaño copia", len(cadenaCopy))
    while len(cadenaCopy) > 0:
        # print(index)
        letter = letras[index]
        cadenaCopy = cadenaCopy.replace(letter, "")
        index += 1
        cadena += cadenaCopy
    return cadena

# lectura()
lecturaConArchivo()

