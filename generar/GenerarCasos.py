import string
import random
from random_word import RandomWords


def main():
    ncasos = 500000
    ncorrectos = int(ncasos * 0.25) - 4
    naleatorios = ncasos - int(ncasos * 0.5)
    nincorrectos = int(ncasos * 0.25)
    print(ncasos, ncorrectos, naleatorios, nincorrectos)

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

    r = RandomWords()
    for i in range(ncorrectos):
        palabra = None
        while palabra is None:
            palabra = r.get_random_word(hasDictionaryDef="true")

        palabra = palabra.replace("-", "").replace(" ", "").replace("'", "")
        cadena = procesarCadena(palabra, filepalabras)
        print(i, palabra)
        file.write(cadena + "\n")

    for i in range(naleatorios):
        tamanio = random.randint(1, 10**4)
        cadena = generar_caso(tamanio, filepalabras)
        print(i)
        file.write(cadena + "\n")

    for i in range(nincorrectos):
        cadena = ''.join(random.choice(string.ascii_lowercase)
                         for i in range(random.randint(1, 10**4)))
        print(i)
        file.write(cadena + "\n")
        filepalabras.write("NO EXISTE\n")

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
