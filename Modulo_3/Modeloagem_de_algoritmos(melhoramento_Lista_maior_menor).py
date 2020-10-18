'''
1. Vamos comparar os elementos aos pares, separando-os sempre em dois subconjuntos: o dos que foram
maiores e o dos que foram menores na comparação de que participaram. Note que isso nos renderia no
máximo n/2 comparações (considerando um número par de elementos na lista).
2. Obteremos então o maior elemento na metade do vetor que tem os elementos que venceram as
comparações como um custo ótimo de no máximo n/2-1 comparações (usando o algoritmo “maior” já
apresentado anteriormente que é ótimo)
3. Obteremos o menor elemento de forma semelhante à obtenção do maior elemento a um custo também
de no máximo n/2-1.

'''
lista = [
    1, 681, 81, 5, 101, 56, 15, 0, 21, 8, 1, 10, 68, 186, 5, 4, 87, 484, 8,
    494, 51, 53, 1, 544, 8, 45, 4, 5, 8, 4, 1, 3, 21, 5, 4185, 4, 87, 5, 45, 1,
    1, 5, 4, 84, 878, 76, 21322, 5, 6, 45, 8, 46, 14
]


def maior_Menor_1_1(lista):
    if (len(lista) % 2 == 1):
        lista.append(lista[0])
    #apenas definindo maior e menor
    if (lista[0] > lista[1]):
        maior = lista[0]
        menor = lista[1]
    else:
        maior = lista[1]
        menor = lista[0]
    #iterando em lista a pares sobre indices
    i = 2
    while (i < len(lista)):
        if (lista[i] > lista[i + 1]):
            if lista[i] > maior:
                maior = lista[i]
            if lista[i + 1] < menor:
                menor = lista[i + 1]
        else:
            if lista[i] < menor:
                menor = lista[i]
            if lista[i + 1] > maior:
                maior = lista[i + 1]
        i += 2
    tupla = (maior,menor)
    return tupla


print(maior_Menor_1_1(lista))