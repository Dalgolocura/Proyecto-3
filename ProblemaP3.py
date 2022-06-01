from sys import stdin
from time import process_time as timer
# import threading


def lectura():
    start = timer()
    nCasos = int(stdin.readline())
    # threads = []
    # print(nCasos)
    while nCasos != 0:
        linea = stdin.readline().replace('\n', '')
        # print("lista", lista)

        # thread = threading.Thread(target=procesar, args=(linea,))
        # threads.append(thread)
        # thread.start()
        procesar(linea)

        nCasos -= 1

    # for thread in threads:
    #     thread.join()

    elapsed_time = timer() - start
    print("Time: %.10f" % elapsed_time)

def lecturaConArchivo():
    start = timer()
    file = open("in.in.txt", "r")
    # file = open("500000.in", "r")
    nCasos = int(file.readline())
    while nCasos != 0:
        linea = file.readline().replace('\n', '')
        procesar(linea)
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

    # letras = list(letras_repeticiones.keys())

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

    # cantidad_palabra = sum(list(letras_cantidad.values()))
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
    if funciona:
        salida = palabra_original + " " + orden_eliminacion
        print(salida)


lectura()
# lecturaConArchivo()

