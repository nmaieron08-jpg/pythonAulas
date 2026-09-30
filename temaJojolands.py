alvos = ["drone" , "paco" , "policial"]
alcance = [4 , 10 , 20]
for index in range(3):
    print(f"Alvo {index+1}: {alvos[index]} | Distância: {alcance[index]}m")
    if alcance[index] < 5:
        print ("gg gurizada, o november rain deixou esse chinelão onde deveria! ele levou gotas pesadas")
    elif alcance[index] <= 15:
        print ("bah tche! o november rain não esmagou esse chinelão porque ta tomando chima longe de nois, mas pelomenos ele desacelerou.  ")
    else:
        print ("esse egoísta quer tomar mate sem dividir com a gente, bah mais que nojentão esse cagão aí, chega mais pertoo ai o november rain nao consegue te dale um supapo no pé da oreia!!!")
    print("-" * 50)
