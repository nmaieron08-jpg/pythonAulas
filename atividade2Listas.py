from random import randint
itens_vilao = ['grimório de zoltraak' , 'cajado' , 'espada' , 'fern' , 'cama']
itens_coletados = []
pontos_itens = [2 , 5 , 7 , 67 , 100000]
pontos = 0
print(" você e a fern entraram numa dangeon de monstros  e goblins  vocês derrotaram o boss (naverdade so você porque ele comeu a fern)")
print (" voce tem mque escolher os itens do  monstro para levar para sua base")
for index in range(5):
    escolha = input(f"você quer pegar {itens_vilao[index]}? (sim ou não) ")
    if escolha == "sim" :
        resultado = randint(0,100)
        if resultado <50:
            pontos -= pontos_itens[index]
            itens_coletados.append(itens_vilao[index]+ " amaldiçoado")
            print (f"teu {itens_vilao[index]} foi amaldiçoado")
        else:
            pontos += pontos_itens[index]
            itens_coletados.append(itens_vilao[index]+ " encantado")
            print (f"teu {itens_vilao[index]} foi encantado")
            
print (f"itens coletados:{itens_coletados}+{pontos}")
