vida_do_monstro = 10
vida_do_héroi = 10
cura = 1
raio = 1
print ("esse rpg tem 4 rodadadas, você e seu inimigo começam com 10 de vida, você tem opções de cura ou de ataque especial ou espada.")
for rodada in range(1,5):
    print (f"sua vida: {vida_do_héroi} e vida do teu oponente: {vida_do_monstro}")
    print (f"quantidade de cura: {cura} e quantidade de ataque especial: {raio}")
    escolha = int(input("digite oque tu quer fazer:  (1: ataque básico / 2: curar / 3:ataque especial): "))
    if escolha == 1:
        vida_do_monstro -=3
    elif escolha == 2:
        if cura ==1:
            vida_do_héroi += 6
            cura = 0
        else:
            print (" sem cura mais abestado")
    elif escolha == 3:
        
        if raio ==1:
            vida_do_monstro -= 6
            raio = 0
        else:
            print (" sem raio mais abestado")
    else:
        print ("escreveu errado burrão, seu personagens ratiou.")
    if vida_do_monstro >=1:
        vida_do_héroi -= 5
    if vida_do_monstro <1 or vida_do_héroi <1:
        break
print (f"vida do herói: {vida_do_héroi} e vida do monstro: {vida_do_monstro}")
if vida_do_monstro <1:
    print ("herói venceu")    
elif vida_do_héroi <1:
    print ("monstro venceu")
else:
    print ("draw") 
