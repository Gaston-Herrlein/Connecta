from list_utils import replace_all_in_matrix


def explode_string(string):
    """
    Este metodo trandforma un string en una lista de caracteres
    """
    return list(string)


def explode_list_of_strings(l):
    """
    Dada una lista de string, lo transforma en una lista de listas (separando los string en caracter por caracter)
    """
    result = []
    for string in l:
        result.append(explode_string(string))
    return result


def explode_string_to_matrix(string, sep="|"):
    """
    Dado un string compruebo si contiene el separador. Si lo contiene lo transformo en una lista de string.
    Luego le aplico la funcion 'explode_list_of_strings()' para obtener la matriz
    """
    m = []
    if sep in string:
        m = explode_list_of_strings(string.split(sep))
    else:
        m = explode_list_of_strings(string)
    return replace_all_in_matrix(m)
