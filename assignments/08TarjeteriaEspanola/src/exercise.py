def tarjetas(pliegos,plumones):
    
    tarjetasPliegos = pliegos*12
    tarjetasPlumones = plumones*35

    if tarjetasPliegos<=tarjetasPlumones:
        return tarjetasPliegos
    else:
        return tarjetasPlumones

def main():
    #escribe tu código abajo de esta línea
    pli = int(input("Dame la cantidad de pliegos de papel albanene: "))
    plu = int(input("Dame la cantidad de plumones: "))

    r = tarjetas(pli,plu)

    print("El número máximo de tarjetas que se pueden hacer es:",r)

if __name__=='__main__':
    main()
