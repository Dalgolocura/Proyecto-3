import string
import random
from time import process_time as timer


def main():
    ncasos = 1000000
    naleatorios = int(ncasos * 0.25)
    nincorrectos = int(ncasos * 0.25)
    ncorrectos = ncasos - naleatorios - nincorrectos - 4
    print(ncasos, ncorrectos, naleatorios, nincorrectos)

    filepalabras = open("generar/lemario.txt", "r")
    linea = filepalabras.readline()
    palabras = linea.strip().split()
    filepalabras.close()

    file = open(str(ncasos) + ".in", "w")
    filepalabras = open("s" + str(ncasos) + ".out", "w")

    file.write(str(ncasos) + "\n")

    cadena = procesarCadena("Borris", filepalabras)
    file.write(cadena + "\n")
    cadena = procesarCadena("Juliana", filepalabras)
    file.write(cadena + "\n")
    cadena = procesarCadena("Daniel", filepalabras)
    file.write(cadena + "\n")
    cadena = procesarCadena("William", filepalabras)
    file.write(cadena + "\n")

    start = timer()
    for i in range(ncorrectos):
        palabra = None
        while palabra is None:
            palabra = random.choice(palabras)

        palabra = palabra.replace("-", "").replace(" ", "").replace("'", "")
        cadena = procesarCadena(palabra, filepalabras)
        file.write(cadena + "\n")

        if i % int(ncorrectos * 0.05) == 0:
            print(int(round(i / ncorrectos,2)*100), "% de palabras normales")
    elapsed_time = timer() - start
    print("Time: %.10f" % elapsed_time)

    start = timer()
    for i in range(naleatorios):
        tamanio = random.randint(1, 10**4)
        cadena = generar_caso(tamanio, filepalabras)
        file.write(cadena + "\n")

        if i % int(naleatorios * 0.05) == 0:
            print(int(round(i / naleatorios,2)*100), "% de palabras aleatorias")
    elapsed_time = timer() - start
    print("Time: %.10f" % elapsed_time)

    start = timer()
    for i in range(nincorrectos):
        cadena = ''.join(random.choice(string.ascii_lowercase)
                         for i in range(random.randint(1, 10**4)))
        file.write(cadena + "\n")
        filepalabras.write("NO EXISTE\n")

        if i % int(nincorrectos * 0.05) == 0:
            print(int(round(i / nincorrectos,2)*100), "% de palabras incorrectas")
    elapsed_time = timer() - start
    print("Time: %.10f" % elapsed_time)

    file.close()
    filepalabras.close()


def generar_caso(tamanio: int, filePalabras):
    letras = string.ascii_lowercase
    cadena = ''.join(random.choice(letras) for i in range(tamanio))
    resul = procesarCadena(cadena, filePalabras)
    return resul


def procesarCadena(cadena: str, filePalabras):
    try:
        cadenaCopy = cadena
        filePalabras.write(cadena)
        while len(cadenaCopy) > 0:
            index = random.randint(0, len(cadenaCopy) - 1)
            letter = cadenaCopy[index]
            filePalabras.write(" " + letter)
            cadenaCopy = cadenaCopy.replace(letter, "")
            cadena += cadenaCopy
        filePalabras.write("\n")
    except Exception as e:
        print(cadena)
        print(e)
    return cadena


main()
