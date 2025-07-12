from itertools import product
import os
os.system("cls")

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
}


def ver_marcas():
    marcas = set()
    for producto in productos.values():
        marcas.add(producto[0])

    print(" MARCAS : ")
    for marca in sorted(marcas):

        print(f"{marcas}")
        

def stock_marca():
    stock = 0
    for modelo,datos in stock_marca.items():
        if datos[0].lower()== modelo.lower():
            stock += [modelo][0]
        
        print(f"stock total para la marca{modelo} {stock}")

def busqueda_por_precio(p_min,p_max):
    resultados =[]
    if p_min <= stock <=p_max and stock:
        marca = productos[p_min][0]
        resultados.append(f"{marca}")


def actualizar_precio():
    p_min = int(input("ingrese precio minimo: "))
    p_max = int(input("ingrese precio maximo: "))
    return





def menu():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1.STOCK MARCA")
        print("2.BUSQUEDA POR PRECIO ")
        print("3.ACTUALIZAR PRECIO")
        print("4.SALIR")

        opcion = int(input("ingrese una opcion: "))


        if opcion < 1 or opcion > 4:
            try:
                ("opcion fuera de rango")
            except:
                return opcion
        elif opcion ==1:
            ver_marcas()
            input()


        elif opcion == 2:
            stock_marca()
            input()


        elif opcion == 3:
            actualizar_precio()

           
            input()

        elif opcion == 4:
            os.system("cls")
            input("PROGRAMA FINALIZADO")

        else:
            break


menu()
