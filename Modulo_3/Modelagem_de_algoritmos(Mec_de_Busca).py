lista = [1,2,3,4,5,6,7,8,9]



def pesquisaBinaria(reg, lista):
    if len(lista) == 0:
        return -1
    esq = 0
    dir = len(lista)-1
    i = int((esq+dir)/2)
    while esq <= dir and reg != lista[i]:
        if reg < lista[i]:
            dir = i - 1
        else:
            esq = i + 1
        i = int((esq+dir)/2)
    if lista[i] == reg:
        return i
    
