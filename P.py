def datecheck(date):

    newdate = date.split("/")

    error = 0
    noerrores = 0
    diagonal = 0

    for i in range(len(newdate)):
        if date[i] in "/":
            diagonal += 1
            noerrores += 1
    if diagonal > 0:

        if len(date) == 8:

            if int(newdate[0]) == 0 or int(newdate[1] == 0):
                error += 1
            else:
                noerrores += 1

            if int(newdate[2]) != 18:
                error += 1
            else:
                noerrores += 1

            if (int(newdate[1]) < 1 or int(newdate[1]) > 12):
                error += 1

            if int(newdate[1]) == 1 or int(newdate[1]) == 5 or int(newdate[1]) == 7 or int(newdate[1]) == 8 or int(newdate[1]) == 10 or int(newdate[1]) == 12:
                if int(newdate[0]) < 1 or int(newdate[0]) > 31:
                    error += 1
                else:
                    noerrores += 1

            if int(newdate[1]) == 3 or int(newdate[1]) == 4 or int(newdate[1]) == 6 or int(newdate[1]) == 9 or int(newdate[1]) == 11:
                if int(newdate[0]) < 1 or int(newdate[0]) > 30:
                    error += 1
                else:
                    noerrores += 1

            if int(newdate[1]) == 2:
                if int(newdate[0]) < 1 or int(newdate[0]) > 28:
                    error += 1
        else:
            error += 1

    if error > 0 or (error == 0 and noerrores == 0):
        return False

    if noerrores > 0 and error == 0:
        return True

def convert(s):
    new = ""
    for x in s:
        new += x
    return new

def guardar(moneda, cantidad, fecha):
    archivo = open("Guardar.txt", "a")
    archivo.write(moneda + " " + fecha + "\n" + cantidad)
    archivo.close()

def revisar():
    archivo = open("Guardar.txt", "r")
    if archivo.readline().strip() == "Consulta de tipo de cambio":
        archivo.close()
        return True
    else:
        archivo.close()
        return False


print("----------------------------------------------------------------------------------------------------------")
print("|Bienvenido al servicio de tipo de cambio, puede consultar la venta y compra de una moneda en particular.|")
print("|Puede escoger entre 3 tipos de cambio: Dolar, Euro y Libra                                              |")
print("|Para ingresar la fecha utilice el formato (dd/mm/aa)                                                    |")
print("|Para salir del programa, escribe 'listo'.                                                               |")
print("|Para borrar el historial, escribe 'eliminar'.                                                           |")
print("|¿Desea borrar los archivos? Ingrese 'eliminar'. Si no, escriba 'no':                                    |")
print("----------------------------------------------------------------------------------------------------------")

salir = input()

if salir.upper() == "ELIMINAR":
    archivo = open("Guardar.txt", "w")
    archivo.close()

moneda = input("Ingrese el tipo de cambio que desee consultar: ")
while not moneda == "listo":
    if not (moneda.upper() == "DOLAR" or moneda.upper() == "LIBRA" or moneda.upper() == "EURO" or moneda.upper() == "ELIMINAR"):
        print("Lo sentimos, la entrada no es correcta o no manejamos ese tipo de moneda")
        moneda = input("Ingresa una opción valida: ")

    if moneda.upper() == "DOLAR":
        fecha = input("Ingrese una fecha para consultar el cambio del dolar: ")
        while datecheck(fecha) == False:
            print("Fecha incorrecta, no se encuentra en nuestros archivos")
            fecha = input("Ingrese una fecha para consultar el cambio del dolar: ")
        dolarnuevo = []
        searchdolar = open("DOLAR.txt", "r")
        for line in searchdolar:
            if fecha in line:
                dolarnuevo += line
        searchdolar.close()

        print("")
        print("El tipo de cambio de esa fecha es: ")
        print(convert(dolarnuevo)[11:])
        guardar(moneda,convert(dolarnuevo[11:]), fecha)


    if moneda.upper() == "EURO":
        fecha = input("Ingrese una fecha para consultar el cambio del euro: ")
        while datecheck(fecha) == False:
            print("Fecha incorrecta, no se encuentra en nuestros archivos")
            fecha = input("Ingrese una fecha para consultar el cambio del euro: ")
        euronuevo = []
        searcheuro = open("EURO.txt", "r")
        for line in searcheuro:
            if fecha in line:
                euronuevo += line
        searcheuro.close()

        print("")
        print("El tipo de cambio de esa fecha es: ")
        print(convert(euronuevo)[11:])
        guardar(moneda, convert(euronuevo)[11:], fecha)

    if moneda.upper() == "LIBRA":
        fecha = input("Ingrese una fecha para consultar el cambio de la libra: ")
        while datecheck(fecha) == False:
            print("Fecha incorrecta, no se encuentra en nuestros archivos")
            fecha = input("Ingrese una fecha para consultar el cambio de la libra: ")
        libranuevo = []
        searchlibra = open("LIBRA.txt", "r")
        for line in searchlibra:
            if fecha in line:
                libranuevo += line
        searchlibra.close()

        print("")
        print("El tipo de cambio de la libra de esa fecha es: ")
        print(convert(libranuevo)[11:])
        guardar(moneda, convert(libranuevo)[11:], fecha)
    moneda = input("Ingrese el tipo de cambio que desee consultar: ")
else:
    exit()

