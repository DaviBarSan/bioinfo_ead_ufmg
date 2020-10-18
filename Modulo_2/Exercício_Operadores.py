import math

''''
Nit = (108.304, 100.827, 67.992)
CA = (108.477, 100.389, 69.362)
C = (109.907, 100.555, 69.817)
O = (110.821, 100.799, 69.027)

atomic_distance_1 = (Nit, CA, C, O)
'''
#In these tuples coordinates are x,y,z respectively
'''
Nit_2 = (107.670, 101.359, 70.074)
CA_2 = (108.477, 100.389, 69.362)
C_2 = (109.513, 101.011, 68.450)
O_2 = (110.667, 100.572, 68.425)
'''

Nit1_2 = (abs(108.304-107.670), abs(100.827-101.359), abs(67.992 - 70.074))
CA1_2 = (108.477 - 108.477, 100.389 - 100.389, 69.362 - 69.362)
C1_2 = (109.907 - 109.513, abs(100.555 - 101.011), abs(69.817 - 68.450))
O1_2 = (110.821 - 110.667, 100.799 - 100.572, 69.027 - 68.425)

atomic_distance_1_2 = (Nit1_2, CA1_2, C1_2, O1_2)

RMSD_sum = []

for x, y, z in atomic_distance_1_2:    
    RMSD = ((x)**2+(y)**2+(z)**2)
    RMSD_sum.append(RMSD)  


print(f"Questão 01: The RMSD for the glicines is {round(math.sqrt((sum(RMSD_sum)/4.0)), 4)}.")


#Questão 02

seq_A = 'ATGATCTCGTAATTAACCGGAATTTTGGGCC'
seq_B = 'GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA'

def GC_content(sequence):
    return round(((100*((sequence.count('C')) + (sequence.count('G')))/len(sequence))), 4)



print(f"The GC content in the sequence A and B are respectively {GC_content(seq_A)} and {GC_content(seq_B)}.")

