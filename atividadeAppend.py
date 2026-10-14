itens_vilao = ['grimório de zoltraak' , 'cajado' , 'espada' , 'fern' , 'cama']
itens_coletados = []
print(" você e a fern entraram numa dangeon de monstros  e goblins  vocês derrotaram o boss (naverdade so você porque ele comeu a fern)")
print (" voce tem mque escolher os itens do  monstro para levar para sua base")
for item in itens_vilao:
    escolha = input(f"você quer pegar {item}? (sim ou não) ")
    if escolha == "sim" :
        itens_coletados.append(item)
print (f"itens coletados:{itens_coletados}")
