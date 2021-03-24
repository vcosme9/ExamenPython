


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
    