def oraciones(cadena):
    # solución sin ciclos return cadena.count(".")

    cont = 0
    for c in cadena:
        if c==".":
            cont = cont+1

    return cont

def main():
    #escribe tu código abajo de esta línea
    parrafo = input("Dame un párrafo: ")

    r = oraciones(parrafo)

    print("Número de oraciones terminadas por un punto:",r)

if __name__=='__main__':
    main()
