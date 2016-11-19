#calcula de area y perimetro de las fguras geometricas
## Funciones

def figuras():
    print("\t\t  ---------FIGURAS GEOMETRICAS---------")
    print("\t\t\t   (Número de lados)")
    print("\t\tTriangulo(3)\t\t\tOctágono(8)")
    print("\t\tCuadrado(4)\t\t\tEneágono(9)")
    print("\t\tPentágono(5)\t\t\tDecágono(10)")
    print("\t\tHexágono(6)\t\t\tEndecágono(11)")
    print("\t\tHeptágono(7)\t\t\tDodecágono(12)")
    
def triangulo():
     print("\n\t\t-----TRIANGULO-----")
     lado1 = float(input("\nIngrese el valor del lado uno: "))
     lado2 = float(input("Ingrese el valor del lado dos: "))
     base = float(input("Ingrese el valor de la base: "))
     altura = float(input("Ingrese el valor de la altura: "))
     perimetro = lado1 + lado2 + base
     area = (base * altura) / 2
     print("El perimetro del triangulo es: ",perimetro)
     print("El area del triangulo es: ",area)

def cuadrado():
    print("\n\t\t-----CUADRADO-----")
    lado = float(input("\nIngrese el valor del lado: "))
    perimetro = lado + lado + lado + lado
    area = lado * lado
    print("El perimetro del cuadrado es: ",perimetro)
    print("El area del cuadrado es: ",area)
    
def pentagono():
     print("\n\t\t-----PENTÁGONO-----")
     lados = float(input("\nIngrese el valor de la longitud de los lados: "))
     apotema = float(input("Ingrese el valor de la apotema:  "))
     perimetro = (5*lados)
     area = (5*lados*apotema) / 2
     print("El perimetro del pentágono es: ",perimetro)
     print("El area del pentágono es: ",area)

def hexagono():
     print("\n\t\t-----HEXÁGONO-----")
     lados = float(input("\nIngrese el valor de la longitud de los lados: "))
     apotema = float(input("Ingrese el valor de la apotema:  "))
     perimetro = (6*lados)
     area = (3*lados*apotema)
     print("El perimetro del hexágono es: ",perimetro)
     print("El area del hexágono es: ",area)
     
def heptagono():
     print("\n\t\t-----HEPTÁGONO-----")
     lados = float(input("\nIngrese el valor de la longitud de los lados: "))
     apotema = float(input("Ingrese el valor de la apotema:  "))
     perimetro = (7*lados)
     area = (7*lados*apotema)/ 2
     print("El perimetro del heptágono es: ",perimetro)
     print("El area del heptágono es: ",area)

def octagono():
     print("\n\t\t-----OCTÁGONO-----")
     lados = float(input("\nIngrese el valor de la longitud de los lados: "))
     apotema = float(input("Ingrese el valor de la apotema:  "))
     perimetro = (8*lados)
     area = (4*lados*apotema) 
     print("El perimetro del octágono es: ",perimetro)
     print("El area del octágono es: ",area)
     
def enagono():
     print("\n\t\t-----ENEÁGONO-----")
     lados = float(input("\nIngrese el valor de la longitud de los lados: "))
     apotema = float(input("Ingrese el valor de la apotema:  "))
     perimetro = (9*lados)
     area = (perimetro*apotema)/2 
     print("El perimetro del eneágono es: ",perimetro)
     print("El area del eneágono es: ",area)
     
def decagono():
     print(" \n\t\t-----DECEÁGONO-----")
     lados = float(input("\nIngrese el valor de la longitud de los lados: "))
     apotema = float(input("Ingrese el valor de la apotema:  "))
     perimetro = (10*lados)
     area = (perimetro*apotema)/2 
     print("El perimetro del decágono es: ",perimetro)
     print("El area del decágono es: ",area)
     
def endecagono():
     print("\n\t\t-----ENDECÁGONO-----")
     lados = float(input("\nIngrese el valor de la longitud de los lados: "))
     apotema = float(input("Ingrese el valor de la apotema:  "))
     perimetro = (11*lados)
     area = (perimetro*apotema)/2 
     print("El perimetro del endecágono es: ",perimetro)
     print("El area del endecágono es: ",area)
     
def dodecagono():
     print("\n\t\t-----DODECÁGONO-----")
     lados = float(input("\nIngrese el valor de la longitud de los lados: "))
     apotema = float(input("Ingrese el valor de la apotema:  "))
     perimetro = (12*lados)
     area = (perimetro*apotema)/2 
     print("El perimetro del dodecágono es: ",perimetro)
     print("El area del dodecágono es: ",area)

def main():
    print("\t\t\t     Escuela Politécnica Nacional")
    print("\t\t\t  Escuela de Formación de Tecnólogos")
    print("\t\t\t\t  Programación Avanzada")
    print("\t\t\t     Diana Bonilla - Valeria Ochoa")
    print("\tDeterminar el perimetro y area de las siguientes figuras regulares")
    figuras()
    num_lado = int(input("Ingrese el numero de lados de la figura que desea:....."))
    while num_lado != "":
        if num_lado == 3:
            triangulo()
        elif num_lado == 4:
            cuadrado()
        elif num_lado == 5:
            pentagono()
        elif num_lado == 6:
            hexagono()
        elif num_lado == 7:
            heptagono()
        elif num_lado == 8:
            octagono()
        elif num_lado == 9:
            eneagono()
        elif num_lado == 10:
            decagono()
        elif num_lado == 11:
            endecagono()
        elif num_lado == 12:
            dodecagono()     
        else:
            exit()
        print(" ")
        print(" ")
        figuras()
        num_lado = int(input("Ingrese el numero de lados de la figura que desea:....."))

main()
        
