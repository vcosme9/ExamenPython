import Libro

#datos de libros inventados
libro_1 = Libro("Cervantes", "Don Quijote", 1950)


def get_list (fichero):
    with fichero open as f

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
        for lineas in f:
        palabras.extend(lineas.split())

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
    except:
        print("ValueError: el fichero esta vacio")

def mas_antiguos(lista, anyo):
    