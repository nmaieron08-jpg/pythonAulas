import random
progresso = []
pedras = ["Agarrão", "Romba", "Pinça", "Buraco" , "Chaminé"]
movimentos = ["Esticar braços", "Descanso", "Movimento fluido" , "Apressar a passagem"]
while len(progresso) <6 :
    print (f"seu progresso: {progresso}")
    pedra = pedras[random.randint(0,4)]
    movimento = input(f"a proxima pedra é {pedra}, qual movimento voce vai fazer? {movimentos}: ")
    if pedra == "Agarrão":
        if movimento == "Esticar braços":
            progresso.append(pedra) 
            print (f"voce subiu {pedra} ")
        elif movimento == "Apressar a passagem":
            progresso.clear() 
            print  ("voce caiu")
        else:
            print  ("seu movimento o sustenta mas não progride e  deve tentar uma pedra ao lado")
    
    elif pedra == "Romba":
        if movimento == "Movimento fluido":
            progresso.append(pedra) 
            print (f"voce subiu {pedra} ")
        elif movimento == "Esticar braços":
            progresso.clear() 
            print  ("voce caiu")
        else:
             print  ("seu movimento o sustenta mas não progride e  deve tentar uma pedra ao lado")

    elif pedra == "Pinça":
        if movimento == "Movimento fluido":
            progresso.append(pedra) 
            print (f"voce subiu {pedra} ")
        elif movimento == "Esticar braços":
            progresso.clear() 
            print  ("voce caiu")
        else:
            print  ("seu movimento o sustenta mas não progride e  deve tentar uma pedra ao lado")

    elif pedra == "Buraco":
        if movimento == "Apressar passagem":
            progresso.append(pedra) 
            print (f"voce subiu {pedra} ")
        elif movimento == "Movimento fluido":
            progresso.clear() 
            print  ("voce caiu")
        else:
            print   ("seu movimento o sustenta mas não progride e  deve tentar uma pedra ao lado") 

    elif pedra == "Chaminé":
        if movimento == "Esticar braços":
            progresso.append(pedra) 
            print (f"voce subiu {pedra} ")
        elif movimento == "Apressar passagem":
            progresso.clear() 
            print  ("voce caiu")
        else:
             print  ("seu movimento o sustenta mas não progride e  deve tentar uma pedra ao lado")  
print ("parabéns alpinista! você chegou ao topo da montanha, você é um dos poucos que subiram aqui.")
print (F"esse foi o seu caminho!!! : {progresso}")                        
        
