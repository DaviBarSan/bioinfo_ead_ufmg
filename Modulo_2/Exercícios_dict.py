'''

1.  O  Protein  Data  Bank  (PDB)  é  uma  base  de  dados  de  estruturas  de  proteínas.  
Cada  entrada  da  base  de dados é identificada de por um id de 4 letras / dígitos como por exemplo “1ABC”. 
Abaixo são apresentados ids de estruturas PDBs, juntamente com a a contagem de aminoácidos presentes nessas estruturas.

'''

pdb = {'1A8M':471, '1TNR':283,'2AZ5':592,'1TNF':471,'2TNF':468,'2TUN':942,'4TSV':150,'5TSW':900,'2E7A':471,'6RMJ':489}

print("Questão 01, a)")
print(f"The id '2TNF' is {pdb['2TNF']}, and '2E7A' is {pdb['2E7A']}")

print("Questão 01, b)")
print(f"The dict pdb lenght is {len(pdb)}")

print("Questão 01, c)")
print(f"The list of keys is: {pdb.keys()}")

print("Questão 01, d)")
print(f"The list of values in dict pdb is: {pdb.values()}.")

print("Questão 01, e)")
print(f"The list of tuples formed by dictionary keys and values is: {pdb.items()}.")