lista = [1,681,81,5,101,56,15,0,21,8,1,10,68,186,5,4,87,484,8,494,51,53,1,544,8,45,4,5,8,4,1,3,21,5,4185,4,87,5,45,1,1,5,4,84,878,76,21322,5,6,45,8,46,14]
maior = lista[0]
menor = lista[0]
def maior_Menor_1(lista):
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
        elif lista [i] < menor:
            menor = lista[i]
    print(maior, menor)