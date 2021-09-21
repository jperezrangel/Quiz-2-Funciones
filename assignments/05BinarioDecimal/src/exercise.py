# Funcion binario a decimal
# Convierte un numero binario a uno decimal
# regresa -1 si parametro nulo o numero no binario
def binario_decimal(datoBinario):
    if len(datoBinario)==0:
        return -1
    for numero in datoBinario:
        if numero != "0" and numero != "1":
            return -1
    decimal = 0
    posicion = 0
    for numero in datoBinario:
        decimal += int(2) ** posicion
        posicion += 1
    return decimal

def main():
    numero = input()
    print(binario_decimal(numero))

if __name__=='__main__':
    main()
