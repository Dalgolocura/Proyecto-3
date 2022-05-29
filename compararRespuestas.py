file1 = open("ou.out", "r")
# file2 = open("10.out", "r")
file2 = open("15.out", "r")
# file2 = open("20.out", "r")
# file2 = open("100.out", "r")
# file2 = open("500000.out", "r")
# file2 = open("1000000.out", "r")
fileSalida = open("compararResultados.txt", "w")


linea1 = file1.readline().replace("\n", "")
linea2 = file2.readline().replace("\n", "")
fileSalida.write("Casos mal:\n")

diferentes = 0
caso = 1
while linea1 != "" or linea2 != "":
    if linea1 != linea2:
        diferentes += 1
        lineaSalida = "Caso " + str(caso) + ": Nuestro " + linea1 + " Profe " + linea2
        try:
            lineaSalida += " Diferencia: " + str(int(linea1) - int(linea2))
        except:
            pass
        lineaSalida += "\n"
        fileSalida.write(lineaSalida)
    linea1 = file1.readline().replace("\n", "")
    linea2 = file2.readline().replace("\n", "")
    caso += 1

fileSalida.write("Casos diferentes:" + str(diferentes) + "\n")
file1.close()
file2.close()
fileSalida.close()
