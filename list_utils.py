from settings import VICTORY_STRICK


def find_streak(list, needle, n=VICTORY_STRICK):
    """
    Recibe una lista y retorna True/False segun encuentre una seguidilla de 'n' 'needle'
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


def nth_elements(matrix, n=0):
    """
    Devuele el enecimo elemento de cada lista de una matriz. En caso que la lista sea demasiado corta, devuelve None
    """
    return list(map(lambda element: element[n] if len(element) > n else None, matrix))


def transpose(matrix):
    """
    Metodo que recive una matriz y devuelve la transpuesta de la misma
    En caso de recibir una matriz vacia devuelve una lista vacia
    """
    if len(matrix) > 0:
        transpose_matrix = []
        for index in range(len(matrix[0])):
            transpose_matrix.append(nth_elements(matrix, index))
        return transpose_matrix
    else:
        return []


def one_displace(l):
    """
    Recibe una lista y desplaza 1 posicion hacia la derecha cada elementos
    """
    # Creamos una copia de la lista para no alterar la original
    l_copy = list(map(lambda lista: lista, l))
    aux = l_copy[0]
    next = l_copy[1]
    for i in range(len(l_copy)):
        l_copy[i + 1] = aux
        aux = next
        if (i + 2) < len(l_copy):
            next = l_copy[i + 2]
        else:
            l_copy[0] = next
            break
    return l_copy


def displace(l, nth=0, filler=None):
    """
    Desplaza 'n' lugares los elementos de una lista
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
        res = res[abs(nth) :]
        return res


def displace_matrix(matrix):
    """
    Desplaza 'n' lugares los elementos de una matriz
    """
    disp = []
    for i in range(len(matrix)):
        disp.append(displace(matrix[i], (i - 1)))
    return disp


def reverse_list(l):
    """
    Devuelve el reverso de una lista
    """
    return list(reversed(l))


def reverse_matrix(m):
    """
    Devuelve el reverso de una matriz
    """
    rm = []

    for col in m:
        rm.append(reverse_list(col))

    return rm


def all_same(l):
    """
    Dada una lista, devuelve True si todos sus elementos son iguales.
    En caso de una lista vacia devuelve True
    """
    flag = True
    if len(l) != 0:
        reference = l[0]
        for i in l:
            if reference != i:
                flag = False
                break
    return flag


def collapse_list(l):
    """
    Metodo que conbierte una lista a string, reemplazando los None por "."
    """
    return "".join(map(lambda x: str(x) if x != None else ".", l))


def collapse_matrix(m):
    """
    Metodo que reutiliza collapse_list para convertir matrices en cadena de caracteres. Separadas por "|"
    """
    collapse_matrix = ""
    for l in m:
        collapse_matrix += collapse_list(l) + "|"

    return collapse_matrix[:-1]


def replace_all_in_list(original, old=".", new=None):
    """
    Cambia todas las ocurrencias 'old' por 'new'
    """
    return list(map(lambda x: new if x == old else x, original))


def replace_all_in_matrix(original, old=".", new=None):
    """
    Aplica replace_all_in_list a todas las listas
    """
    return list(map(lambda x: replace_all_in_list(x, old, new), original))
