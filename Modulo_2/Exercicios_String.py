#1. O TNF alfa é uma citocina pró inflamatória capaz de provocar a apoptose (morte) de células tumorais.\
#  Dada a sua sequência de aminoácidos: 

TNF_seq = "VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"

#Questão 01: a) Retorne o tamanho da sequência.
def seq_len(seq):
    return print(len(seq))
print("Quetão 01, a:\n")
seq_len(TNF_seq)
#Questão 01: b) Realize a contagem da ocorrência de um sequência de leucinas (LL). 
print("\nQuestão 01, b:\n")
print(TNF_seq.count("LL"))
#Questão 01: c) Encontre na sequência as posições ocupadas por duas glicinas (GG) e duas argininas (RR).    
print("\nQuestão 01, c:\n")
print("GG index is {}, and RR index is {}\n".format(TNF_seq.find("GG"), TNF_seq.find("RR")))
#Questão 01: d) Retorne os 100 primeiros aminoácidos da sequência. 
print("Questão 01, d\n")
print(TNF_seq[:100])
#Questão 01 : e) Substitua o trecho da sequência com a ocorrência de 3 serinas e 1 arginina  (SSSR) por alaninas.
print("\nQuestão 01, e:\n")
print(TNF_seq.replace("SSSR", "AAAA"))
#Questão 01 : f) f) Quebre a sequência no local onde a substituição foi realizada.
print("\nQuestão 01, f\n")
new_TNF = TNF_seq.replace("SSSR", "AAAA")
print(new_TNF.split("AAAA"))

''' 
2. Utilizando o texto abaixo:
"As  proteínas  são  cadeias  polipeptídicas  formadas  pela  ligação  peptídica  entre  resíduos  de  aminoácidos. 
Existem  20  tipos  de  aminoácidos  comumente  encontrados  nos  seres  vivos. 
A  esses  aminoácidos,  foram atribuídas  abreviações  de  3  letras  e  símbolos  de  1  letra.  
As  abreviações  de  3  letras  são  bastante  evidentes consistindo nas três primeiras letras do se nome." 

Realiza as seguintes tarefas: 
a) Passe todo o texto para letras maiúsculas. 
b) Passe todo o texto para letras minúsculas.  
c) Passe cada primeira letra de palavra em maiúsculo. 
d) Transforme as letras maiúsculas em minúsculas e vice-versa.

'''
string_model ="As  proteínas  são  cadeias  polipeptídicas  formadas  pela  ligação  peptídica  entre  resíduos  de  aminoácidos. Existem  20  tipos  de  aminoácidos  comumente  encontrados  nos  seres  vivos. A  esses  aminoácidos,  foram atribuídas  abreviações  de  3  letras  e  símbolos  de  1  letra. As  abreviações  de  3  letras  são  bastante  evidentes consistindo nas três primeiras letras do se nome." 
#Questão 02:
print("Questão 02, a:\n")
print(string_model.upper())
print("\nQuestão 02, b:\n")
print(string_model.lower())
print("\nQuestão 02, c:\n")
print(string_model.title())
print("\nQuestão 02, d:\n")
print(string_model.swapcase())

#Questão 03:

insulin_signal = "MALWMRLLPLLALLALWGPDPAAA"

'''
a) Retorne o tamanho da sequência apresentada.  
b) Quebre a sequência no trecho “LLALLALWG". 
c) Concatene as sequências resultantes obtendo a seguinte sequência final MALWMRLLPPDPAAA. 
d) Substitua o trecho "DPAAA" por “LLALL”.

'''
print("\nQuestão 03, a\n")
print("Inslin signal aa code lenght is {}".format(len(insulin_signal)))

print("\nQuestão 03, b\n")
print(insulin_signal.split("LLALLALWG"))

print("\nQuestão 03, c\n")
new_ins_signal = insulin_signal.split("LLALLALWG")
print("".join(new_ins_signal))

print("\nQuestão 03, d\n")
print(insulin_signal.replace("DPAAA", "LLALL"))

'''
4.  Com  base  na  sequência  de  DNA  GATGGAACTTGACGTAAACCTATATT  retorne  a  sequência  de  
RNA correspondente sendo a mesma GAUGGAACUUGACGUAAACCUAUAUU.

'''
DNA_seq = "GATGGAACTTGACGTAAACCTATATT"
RNA_seq = DNA_seq.replace("T", "U")
print("\nQuestão 04:\n")
print(RNA_seq)
