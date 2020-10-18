'''
1. Escreva um programa que calcule e escreva a tabela de graus Centígrados em função dos graus Farenheit que variem entre 1 e 150 de 1 em 1 conforme a fórmula a seguir 

C = 5/9(F-32)

'''

def farenh_to_centi(degree_farenh):
    C = (5/9)*(degree_farenh-32)
    return round(C, 3)

for F in range(151):
    print(f"{F}º Farenheit in centigrades is {farenh_to_centi(F)}.")

'''
2. Utilizando as estruturas de repetição, verifique se as seguintes sequências são uma sequência de DNA {A, G, T, C}, RNA {U, C, A, G},
 PROTEÍNA {A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y} ou nenhuma
 delas (nesse caso, imprima as letras que não fazem parte do alfabeto):

'''

sequences_set = ['ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN', 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT', 'ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN']

DNA_seq = {'A', 'G', 'T', 'C'}
RNA_seq = {'U', 'C', 'A', 'G'}
protein_seq = {'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'}


total_aplha = protein_seq.union(DNA_seq, RNA_seq)

print("\nQuestão 02:\n")

for sequences in sequences_set:
    if set(sequences).difference(DNA_seq) == set():
        print(f"This sequence {sequences} is a DNA sequence.")
    elif set(sequences).difference(RNA_seq) == set():
        print(f"This sequence {sequences} is a RNA sequence.")
    elif set(sequences).difference(protein_seq) == set():
        print(f"This sequence {sequences} is an aminoacids sequence.")
    else:
        print(f"This sequence {sequences}  {set(sequences).difference(total_aplha)}.")

print("Questão 03:")

'''
3.  Utilizando  as  estruturas  de  repetição,  gere  e  imprima  a 
sequência  complemento  reverso  da  seguinte sequência de DNA: TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT

'''

sequencia_DNA = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'
complement_DNA = []
for i in sequencia_DNA:
    if i == 'T':
        complement_DNA.append('A')
    elif i == 'A':
        complement_DNA.append('T')
    elif i == 'C':
        complement_DNA.append('G')
    elif i == 'G':
        complement_DNA.append('C')

real_comp = ''.join(complement_DNA)

print(str(real_comp))

'''
4.  Escreva  um  programa  que  calcule  o  fatorial  de  um  número  recebido  como  entrada.  Lembre-se  que  o fatorial de um 
número é igual ao número multiplicado n sucessivamente por n-1, n-2, .. 1. 
Exemplo: fat(6) = 6 x 5 x 4 x 3 x 2 x 1 = 720. 
'''
print("Questão 04")

def fatorial_function(number):
    total = number
    for n in range(1,number):
        total = n*total
    return total
print(fatorial_function(6))


'''
5. Escreva um programa que liste a tabuada (produtos) dos números de 1 a 15.
'''
print("\nQuestão 05:\n")
def tabuada(par1,par2):
    for i in range(par1,(par2)+1):
        for n in range(11):
            print(f"{i} x {n}: {i*n}")
    return 


print(tabuada(1,2))

''' 
6. Considerando a seguinte sequência e tabela de massas (Tabela 1), escreva
um programa em Python que calcule a
massa molar da sequência: 
VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL
'''
aa_weights_dict = {'A':71.03711, 'C':103.00919, 'D':115.02694, 'E':129.04259, 'F': 147.06841, 'G': 57.02146, 'H':137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406, 'M':131.04049, 'N':114.04293, 'P':97.05276, 'Q':128.05858, 'R':156.10111, 'S':87.03203, 'T':101.04768, 'V':99.06841, 'W':186.07931, 'Y':163.06333}
protein_weight_list = []
protein_aa_code = 'VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'
for aa in protein_aa_code:
    protein_weight_list.append(aa_weights_dict.get(aa))

print(sum(protein_weight_list))

print("\nQuestão 07: a)\n")

'''
7. Considerando a Tabela 2 que contem dados de defensinas de plantas, obtenha / calcule e imprima:

A)a menor sequência e seu comprimento 
B)a maior sequência e seu comprimento 
C)a média entre os comprimentos das sequências 
D)a mediana entre os comprimentos das sequências
'''

defensinas_aa_lenght = {'3PSM':47, '2NY9':41, '2NY8':40, '2NZ3':40, '2E3G':40, '2E3F':43, '2E3E':45}

min_lenght_value = min(defensinas_aa_lenght.values())
min_lenght_values = []


max_lenght_value = max(defensinas_aa_lenght.values())
max_lenght_values = []

for prot in defensinas_aa_lenght:
    if min_lenght_value == defensinas_aa_lenght.get(prot):
        min_lenght_values.append(prot)
    elif max_lenght_value == defensinas_aa_lenght.get(prot):
        max_lenght_values.append(prot)


print(f"The id of smallest protein chain(s) is(are) {min_lenght_values}.")
print(f"The id of largest protein chain(s) is(are) {max_lenght_values}.")

defensinas_lenght_mean = (sum(defensinas_aa_lenght.values())/len(defensinas_aa_lenght))
print(f"The mean of defensinas protein chain lenght is {defensinas_lenght_mean}.")



values_list = list(defensinas_aa_lenght.values())
values_list.sort()
n = len(values_list)

if n%2 == 0:
    median_value = (values_list[int(n/2)] + values_list[int((n/2) + ((n+1)/2))])
    print(f"Median of defensinas protein chain lenght is {median_value}")
else:
    median_value = values_list[int((n+1)/2)]
    print(f"Median of defensinas protein chain lenght is {median_value}")

'''
Questão 08
'''

def Tanimoto_Distance(molec1,molec2):
    and_count = 0
    or_count = 0
    for i in range(len(molec1)):
        if molec1[i] and molec2[i] == 1:
            and_count += 1
            or_count += 1
        elif molec1[i] or molec2[i] == 1:
            or_count += 1
        else:
            pass
    return round(and_count/or_count, 4)

print("\nQuestão 08\n")
seq_1 = [0,0,1,0,0,1,1,0,1,1,0,1]
seq_2 = [0,1,0,0,1,1,0,1,1,0,0,0]

print(Tanimoto_Distance(seq_1,seq_2))