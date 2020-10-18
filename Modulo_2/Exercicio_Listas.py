''' 
1.  O  GenBank  é  um  banco  de  dados  de  sequências  biológicas  disponíveis  publicamente  e  é  produzido  e mantido pelo 
National Center for Biotechnology Information (NCBI). 
As sequências podem ser acessadas por identificadores, no caso das sequências proteicas, o formato dos números de acesso é composto
por 3 letras + 5 numerais ou 3 letras + 7 numerais. 
Realize as seguintes tarefas em Python com base nos identificadores abaixo

''' 

seq_id = ["AAY66821.1", "AAY66759.1", "AAY66711.1", "AAY66706.1", "AAY66703.1", "AAY66697.1", "AAY66696.1", "AAY66682.1", "AAY66647.1", "AAY66625.1", "AAY66623.1", "AAY66620.1", "AAY66619.1", "AAY66616.1", "AAY66609.1", "AAY66607.1", "AAY66586.1", "AAY66564.1", "AAY66562.1", "AAY66561.1", "AAY66558.1", "AAY66544.1", "AAY66542.1", "AAY66539.1", "AAY66538.1", "AAY66537.1", "AAY66536.1", "AAY66512.1", "AAY66496.1", "AAM93627.1", "AAM93626.1", "AAY66506.1", "AAM93587.1", "AAY66811.1", "AAY66620.1", "AAY66555.1","AAY66707.1", "AAM93653.1", "AAY66608.1", "AAY66700.1", "AAY66646.1", "AAY66809.1", "AAK97814.1", "AAK97810.1", "AAY66594.1", "AAY66685.1", "AAY66571.1", "AAY66865.1"]
print("Questão 1, a)\n")
print("seq_id lenght is {}".format(len(seq_id)))

print("\nQuestão 01, b)\n")
check_list = ["AAY66682.1",  "AAY66504.1", "AAY66640.1", "AAY66562.1", "AAY66816.1"]
for i in check_list:
    if i in seq_id:
        print("{} IS in seq_id list!\n".format(i))
    else:
        print("{} is NOT in seq_id list!\n".format(i))
print("\nQuestão 01, c)\n")
print("The tenth element in seq_id list is {}".format(seq_id[9]))

print("Questão 01, d)\n")

seq_id.insert(11, "AAY66967.1")
seq_id.insert(21, "AAY66880.1")
seq_id.insert(16, "AAY6687.1")

print("\nQuestão 01, e)\n")
print("The eight element in seq_id list is {}".format(seq_id[8]))
seq_id.pop(8)
print("Now, the eight element in seq_id list is {}".format(seq_id[8]))


#------ Questão 02 ------

docking_energy = ["-695.9", "-884.3", "-658.2", "-917.9", "-799.8", "-842.1", "-618.6", "-726.6", "-652.6", "-594.8", "-536.1,", ''"-788.2", "-772.1", "-676.9", "-600.2", "-575", "-575.3","-603.4", "-659.6", "-715.3", "-643.8", "-703", "-763.1", "-712.1", "-719", "-574.2", "-594.1", "-700.3", "-742.1", "-621.9","-649.7", "-663.3", "-825.3", "-849.3", "-616.5", "-675.1", "-572.8","-624.2", "-608", "-615.3", "-572.8", "-665.3", "-644.6","-788.9", "-631.8", "-707.4", "-715.2", "-728.2", "-729", "-642.1", "-567.8", "-596.5", "-551.5", "-735",  "-805.5", "-696.7", "-617.9", "-606.5", "-658.8", "-667.8", "-689.5", "-728.4", "-564", "-725.8", "-623.2", "-637", "-570.9", "-646.6", "-703.2", "-722.3", "-624.1", "-655.4"]
print("Questão 02, a)\n")
print(docking_energy)
print("Questão 02, b)\n")
print("\nThe docking_protein list lenght is {}\n".format(len(docking_energy)))
print("Questão 02, c)\n")

docking_energy.sort()
print("The best model, wich has the lower energy, in dockingh_energy list is {}".format(docking_energy[-1]))
print("\nQuestão 02, e)\n")
print("The worst model, wich has the higher energy, in docking_energy list is {}".format(docking_energy[0]))
#Questão 02, e)
docking_energy.remove("-575")
#Questão 02, f)
docking_energy.sort(reverse=True)
#Questão 02, g)
print("\nQuestão 02, g)\n ")
print(docking_energy)
