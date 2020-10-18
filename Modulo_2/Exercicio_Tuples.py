'''

Construa um tupla contendo os seguintes aminoácidos: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y 

Realize as seguintes tarefas através de códigos em Python: 

a) Conte e imprima o número de elementos contidos na tupla criada.  
b) Verifique e imprima se o aminoácido Serina (S) pertence à tupla. 
c) Crie uma segunda tupla contendo os elementos Prolina (P), Glicina (G), Asparagina (N), Tirosina (Y), Valina (V) e Triptofano (W).  
d) Some as tuplas construídas e imprima o resultado. 
e) Conte a ocorrência dos elementos Glicina (G), Asparagina (N) e Cisteína (C). 
f) Retorne a posição do primeiro elemento Asparagina (N). 
g) Retorne os 5 últimos elementos da tupla.

'''
aa_tuple = ('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y')

print("Questão a)\n")
print("aa_tuple lenght is {}".format(len(aa_tuple)))

print("\nQuestão b)\n")
if "S" in aa_tuple:
    print("S aa is in tuple")

sec_aa_tuple = ('P','G','N','Y','V','W')

print("\nQuestão d)\n")
print(aa_tuple + sec_aa_tuple)

print("\nQuestão e)\n")
new_tuple = aa_tuple + sec_aa_tuple
print("G occurence is {}, N occurence is {}, C ocurrence is {}".format(new_tuple.count('G'),new_tuple.count('N'),new_tuple.count('C')))

print("\nQuestão f)\n")
print("N index in new_tuple is {}".format(new_tuple.index('N')))

print("\nQuestão g)\n")
print("The last five elements in new_tuple is {}".format(new_tuple[-5:]))