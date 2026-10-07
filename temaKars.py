mestre = input("quem será seu  treinador? (lisa lisa ou ceasar) :   ")
exercicios = int(input("quantos exercicios eu vou fazer? "))
total_repeticoes = 0
for i in range(1,exercicios +1) :
    nome = input("qual o nome do exercicio? ")
    repeticoes = int(input("quantas repeticoes eu vou ter que sofrer? "))
    total_repeticoes += repeticoes
    if repeticoes >100 or "hamon" in nome:
        print ("man nois vai se lascar, o esforço vai ser extremo")
    elif repeticoes >50:
        print (" um pouco mais dificil")
    elif repeticoes >10:
        print ("molezinha")
    else:
        print ("faço de olho fechado")
impar = total_repeticoes %2
print (f"resumo final:\n treinador:{mestre}\n exercicios:{exercicios}\n media de repeticoes:{total_repeticoes / exercicios } ")
if total_repeticoes >500:
    print ("agora é so matar o kars")
else:
    print (f"faltam {500- total_repeticoes} repeticoes pra matar o kars")
