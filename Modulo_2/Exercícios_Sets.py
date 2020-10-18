ferramenta_1 = {1.9, 1.8, 5.7, 1.6, 5.8, 1.7, 9.6, 5.9, 9.5, 6.5, 6.2, 1.1, 4.4, 3.5, 2.9, 4.7, 4.6, 5.2, 5.3}
ferramenta_2 = {4.7, 3.6, 6.2, 7.1, 7, 5.6, 5.7, 3.4, 3.3, 2.1, 3.8, 3.9, 5, 5.1, 1.9, 9.5, 1.0, 1.3, 5.4}
ferrementa_3 = {2.2, 3.3, 5.1, 3, 3.7, 9.1, 8.8, 8.5, 2, 4.1, 6.1, 4.9, 1.1, 0.5, 0.8, 3.2, 6.9, 9.3, 9.5}

print("Questão 01, a):")
print(f"The difference between the sets (1,2), (1,3) and (2,3) are respectively:\n{ferramenta_1.difference(ferramenta_2)};\n{ferramenta_1.difference(ferrementa_3)} and\n{ferramenta_2.difference(ferrementa_3)}.")
print("\nQuestão 01, b):")
print(f"The intersections between the sets (1,2) are {ferramenta_1.intersection(ferramenta_2)};\n\
between sets (1,3) are {ferramenta_1.intersection(ferramenta_2)}\n\
and in sets (2,3) are {ferramenta_2.intersection(ferrementa_3)}")

print("Questão 01, c):")
print(len(ferramenta_1))
ferramenta_1.update(ferramenta_2)
ferramenta_1.update(ferrementa_3)
print("Questão 01, d):")
print(len(ferramenta_1))

#Questão 02

A = {3, 6, 9, 12, 15, 18, 21, 24, 28, 27}
B = {2, 6, 8, 10, 14, 16, 18, 20, 22, 24}
C = {2, 6, 10, 18, 20}
D = {1, 30, 5, 11, 17, 16, 22, 26}

print("Questão 02, a):")
print(f"The intersection between the sets A and B is {A.intersection(B)}, althought the difference between them are {A.difference(B)}.")
print("\nQuestão 02, b)")
print(f"The set A is disjoint from D: {A.isdisjoint(D)}")
print(f"The set B is disjoint from D: {B.isdisjoint(D)}")
print("\nQuestão 02, c):")
print(f"The set C is subset of A union B: {C.issubset(A.union(B))}")
print("\nQuestão 02, d):")
print(len(D))
D.update([18, 23, 25, 63])
print(len(D))