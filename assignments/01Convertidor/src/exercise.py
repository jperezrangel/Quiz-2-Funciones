def pies():
    centimetros = cantidad * 30.48
    print(centimetros)


def pulgadas():
    centimetros = cantidad * 2.54
    print(centimetros)


def yardas():
    centimetros = cantidad * 91.44
    print(centimetros)


def main():
    global cantidad
    print("1. pies a cm, 2. pulgadas a cm, 3. yardas a cm")
    opcion = int(input("Introduce una opcion: "))
    cantidad = int(input("Introduce la cantidad: "))

    if opcion == 1:
        pies()
    if opcion == 2:
        pulgadas()
    if opcion == 3:
        yardas()
    if opcion != 3 | 2 | 1:
        print("Error")
    elif opcion <= 0:
        print("Error")


if __name__ == '__main__':
    main()
