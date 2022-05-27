import string
import random
from random_word import RandomWords


def main():
    file = open("ni.in", "w")

    tamanio = 10
    cadena = procesarCadena("papaya")
    file.write(cadena + "\n")

    r = RandomWords()
    cadena = procesarCadena(r.get_random_word(hasDictionaryDef="true"))
    file.write(cadena + "\n")

    for i in range(10):
        tamanio = random.randint(1, 10**4)
        cadena = generar_caso(tamanio)
        file.write(cadena + "\n")

    file.close()

def generar_caso(tamanio: int):
    letras = string.ascii_lowercase
    cadena = ''.join(random.choice(letras) for i in range(tamanio))
    resul = procesarCadena(cadena)
    return resul

def procesarCadena(cadena: str):
    cadenaCopy = cadena
    while len(cadenaCopy) > 0:
        index = random.randint(0, len(cadenaCopy) - 1)
        letter = cadenaCopy[index]
        cadenaCopy = cadenaCopy.replace(letter, "")
        cadena += cadenaCopy
    return cadena


main()
