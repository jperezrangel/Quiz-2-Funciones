def area(base,altura):
    return base*altura

def area_prisma(base,altura,profundidad):
    return area(base,altura)*2+area(altura,profundidad)*2+area(base,profundidad)*2

def main():
    #escribe tu código abajo de esta línea
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    p = float(input("Dame la profundidad: "))

    r = area_prisma(b,a,p)

    print("El área total del prisma es:",r)

if __name__=='__main__':
    main()
