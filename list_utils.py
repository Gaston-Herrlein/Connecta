from settings import VICTORY_STRICK


def find_streak(list, needle, n=VICTORY_STRICK):
    """
    Metodo que analisa una lista dada como argumento y retorna True/False segun encuentre una seguidilla de 'n' 'needle'
    """
    if n >= 0:
        index = 0
        count = 0
        streak = False

        while count < n and index < len(list):
            if needle == list[index]:
                streak = True
                count += 1
            else:
                streak = False
                count = 0
            
            index += 1
        return count >= n and streak
    else:
        return False

def nth_elements (matrix, n=0):
    """
    Devuele el enecimo elemento de una cada lista de una matriz. En caso que la lista sea demasiado corta, devuelve None
    """
    return list (map (lambda element: element[n] if len (element) > n else None, matrix))

def transpose (matrix):
    """
    Metodo que recive una matriz y devuelve la transpuesta de la misma
    En caso de recibir una matriz vacia devuelve una lista vacia
    """
    if len(matrix) > 0:
        transpose_matrix = []
        for index in range(len(matrix[0])):
            transpose_matrix.append (nth_elements(matrix, index))
        return  transpose_matrix
    else:
        return []

def one_displace (l):
    """
    Este metodo recibe una lista y desplaza 1 posicion hacia la derecha sus elementos
    """
    #Creamos una copia de la lista para no alterar la original
    l_copy = list (map(lambda lista: lista, l))
    aux = l_copy[0]
    next = l_copy[1]
    for i in range (len(l_copy)):
        l_copy[i+1] = aux
        aux = next
        if (i+2) < len(l_copy):
            next = l_copy[i+2]
        else:
            l_copy[0] = next
            break     
    return l_copy
    
def displace (l, nth=0, filler=None):
    """
    Metodo que haciendo uso de 'one_displace()' desplaza 'n' lugares los elementos de una lista
    Completa los espacion con filler ('None' por defecto) 
    """
    if nth == 0:
        return l
    elif nth > 0:
        filling = [filler] * nth
        res = filling + l
        res = res[:-nth]
        return res
    else:
        filling = [filler] * abs(nth)
        res = l + filling
        res = res[abs(nth):]
        return res

def displace_matrix(matrix):
    """
    Metodo que haciendo uso de 'displace()' desplaza 'n' lugares los elementos de una matriz
    Este metodo se utiliza con el fin de detectar una una victoria en diagonal (ascendente o descendente)
    """
    disp = []
    for i in range(len(matrix)):
        disp.append(displace(matrix[i], (i-1)))
    return disp

def reverse_list (l):
    """
    Devuelve el reverso de una lista
    """
    return list(reversed(l))

def reverse_matrix (m):
    """
    Devuelve el reverso de una matriz
    """
    rm = []

    for col in m:
        rm.append (reverse_list(col))
    
    return rm