from libro import *



def get_list (fichero):
    f = open(fichero, mode="wt", encoding="utf-8")
    data=f.readlines()
    f.close

    palabras = []
    p_1 = []
    p_2 = []
    p_3 = []
    p_4 = []
    p_5 = []
    p_6 = []
    p_7 = []
    p_8 = []
    p_9 = []

    diccionario = {}

    try:
        for renglon in data:
            for palabra in renglon.split(' '):
                palabras.append(palabra)

    except:
        raise ValueError("El fichero esta vacio")
    else:
        for i in range(len(palabras)):
            if(len(palabras[i]) == 1):
                p_1.append(palabras[i])

            if(len(palabras[i]) == 2):
                p_2.append(palabras[i])
        
            if(len(palabras[i]) == 3):
                p_3.append(palabras[i])

            if(len(palabras[i]) == 4):
                p_4.append(palabras[i])
        
            if(len(palabras[i]) == 5):
                p_5.append(palabras[i])

            if(len(palabras[i]) == 6):
                p_6.append(palabras[i])

            if(len(palabras[i]) == 7):
                p_7.append(palabras[i])

            if(len(palabras[i]) == 8):
                p_8.append(palabras[i])

            if(len(palabras[i]) == 9):
                p_9.append(palabras[i])
    
        diccionario[1] = p_1
        diccionario[2] = p_2
        diccionario[3] = p_3
        diccionario[4] = p_4
        diccionario[5] = p_5
        diccionario[6] = p_6
        diccionario[7] = p_7
        diccionario[8] = p_8
        diccionario[9] = p_9

        return diccionario

def mas_antiguos(lista, anyo):

        if anyo < 1900:
            raise ValueError("El año indicado es menos que 1900 o mayor que 2021")
        if anyo > 2021:
            raise ValueError("El año indicado es menos que 1900 o mayor que 2021")

        lista_titulos = []

        for i in range(len(lista)):

            if lista[i].anyo <= anyo:
                lista_titulos.append(lista[i].titulo)

        return lista_titulos
    
'''----MAIN----'''
libro_1 = libro("Cervantes", "Don Quijote", 1950)
libro_2 = libro("Marías, Javier", "Tomás Nevinson", 2020)

libros = [libro_1, libro_2]

#Test
titulos_1 = mas_antiguos(libros, 1960)
print(titulos_1)

titulos_4 = mas_antiguos(libros, 2020)
print(titulos_4)

titulos_2 = mas_antiguos(libros, 1890)
print(titulos_2)

titulos_3 = mas_antiguos(libros, 2022)
print(titulos_3)

