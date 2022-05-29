from sys import stdin
from time import process_time as timer


def lectura():
    start = timer()
    nCasos = int(stdin.readline())
    # print(nCasos)
    while nCasos != 0:
        linea = stdin.readline().replace('\n', '')
        # print("lista", lista)
        procesar(linea)
        nCasos -= 1

    elapsed_time = timer() - start
    print("Time: %.10f" % elapsed_time)


def procesar(entrada):
    letras_repeticiones = {}

    for n in range(1, len(entrada)+1, 1):
        actual = entrada[-n]
        if actual in letras_repeticiones:
            letras_repeticiones[actual] += 1
        else:
            letras_repeticiones[actual] = 1

    letras = list(letras_repeticiones.keys())

    letras_cantidad = {}
    orden_eliminacion = ""

    for n in range(1, len(letras)+1, 1):
        letra = letras[-n]
        veces = letras_repeticiones[letra]//n
        letras_cantidad[letra] = veces
        orden_eliminacion += " " + letra

    cantidad_palabra = sum(list(letras_cantidad.values()))
    palabra_original = entrada[0:cantidad_palabra]

    salida = palabra_original + orden_eliminacion
    print(salida)


lectura()
