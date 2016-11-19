#calcula de area y perimetro de las fguras geometricas
## Funciones
def figuras():
    print("\t\t  ---------FIGURAS GEOMETRICAS---------")
    print("\t\t\t   (Número de lados)")
    print("\t\tTriangulo(3)\t\t\tOctágono(8)")
    print("\t\tCuadrado(4)\t\t\tNonágono(9)")
    print("\t\tPentágono(5)\t\t\tDecágono(10)")
    print("\t\tHexágono(6)\t\t\tEndecágono(11)")
    print("\t\tHeptágono(7)\t\t\tDodecágono(12)")
    
def triangulo():
     print("\t\t-----TRIANGULO-----")
     lado1 = float(input("Ingrese el valor del lado uno: "))
     lado2 = float(input("Ingrese el valor del lado dos: "))
     base = float(input("Ingrese el valor de la base: "))
     altura = float(input("Ingrese el valor de la altura: "))
     perimetro = lado1 + lado2 + base
     area = (base * altura) / 2
     print("El perimetro del triangulo es: ",perimetro)
     print("El area del triangulo es: ",area)

def cuadrado():
    print("\t\t-----CUADRADO-----")
    lado = float(input("Ingrese el valor del lado: "))
    perimetro = lado + lado + lado + lado
    area = lado * lado
    print("El perimetro del cuadrado es: ",perimetro)
    print("El area del cuadrado es: ",area)

def main():
    print("\t\t\t     Escuela Politécnica Nacional")
    print("\t\t\t  Escuela de Formación de Tecnólogos")
    print("\t\t\t\t  Programación Avanzada")
    print("\t\t\t     Diana Bonilla - Valeria Ochoa")
    print("\tDeterminar el perimetro y area de las siguientes figuras")
    figuras()
    num_lado = int(input("Ingrese el numero de lados de la figura que desea:....."))
    while num_lado != "":
        if num_lado == 3:
            triangulo()
        elif num_lado == 4:
            cuadrado()
        else:
            exit()
        print(" ")
        print(" ")
        figuras()
        num_lado = int(input("Ingrese el numero de lados de la figura que desea:....."))

main()
        
