'''
1.Imprima apenas as sequências com 80 ou mais aminoácidos. 
2.Imprima apenas as sequências cujo tamanho seja maior que a média de tamanho das sequências. 
3.Imprima apenas as sequências que possuam pelo menos uma histidina (H) e nenhuma prolina (P). 
4.Identifique e imprima a maior dentre as três sequências a seguir. 
5.Imprima as três sequências em ordem crescente de tamanho. 
'''

aa_seq_A =  'LRSSSQNSSDKPVAHVVANHQVEEQLEWLSQRANALLANGMDLKDNQLVVPADGLYLVYSQVLFKGQGCPDYVLLTHTVSLRSSSDK'
aa_seq_B = 'KPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSS'
aa_seq_C = 'CPQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCR'

#Questão 01
seq_list = [aa_seq_A, aa_seq_B, aa_seq_C]
print('Questão 1:')
for sequence in seq_list:
    if len(sequence) >= 80:
        print(f"Sequence '{sequence}' lenght is {len(sequence)}.")

print("Questão 02:")

mean = round(sum([len(i) for i in seq_list])/len(seq_list), 4)

for sequence in seq_list:
    if len(sequence) >=  mean:
        print(f"The sequence {sequence} lenght is bigger than seq_list mean ({mean})")

print("Questão 03:")
for sequence in seq_list:
    if 'H' in sequence and 'P' not in sequence:
        print(f"This sequence contain Histidine and doesn't contain Proline: \n{sequence}.")
    else:
        print("No one sequence in seq_list contain 'H' and doesn't contain 'P' simutaneously")

print("Questão 04:")
print(f"The largest element in seq_list is {max(seq_list, key=len)}")

print("Questão 05:")
seq_list.sort(key=len)
print(f"The seq_list sorted by lenght becomes {seq_list}")




'''
print(max(seq_list))

'''