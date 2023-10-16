from settings import *


def find_streak(list, needle, n=VICTORY_STRICK):
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
    return list (map (lambda element: element[n] if len (element) > 0 else None, matrix))

def transpose (matrix):
    
    if len(matrix) > 0:
        transpose_matrix = []
        for index in range(len(matrix[0])):
            transpose_matrix.append (nth_elements(matrix, index))
        return  transpose_matrix
    else:
        return []

def one_displace (l):
    """
    Este metodo desplaza 1 posicion hacia la derecha
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
    Este metodo solamente deslpaza la lista hacia la derecha

    if nth == 0 or len(l) <= 1:
        return l
    l_copy = list (map(lambda lista: lista, l))
    for i in range (nth):
        l_copy = one_displace(l_copy)
    return l_copy
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
    disp = []
    for i in range(len(matrix)):
        disp.append(displace(matrix[i], (i-1)))
    return disp

def reverse_list (l):
    return list(reversed(l))

def reverse_matrix (m):
    rm = []

    for col in m:
        rm.append (reverse_list(col))
    
    return rm