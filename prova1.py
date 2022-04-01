# UNIVERSIDADE FEDERAL DE CAMPINA GRANDE - UFCG
# GABRIEL DANTAS DE OLIVEIRA - 121110669
# 14/02/2022 
# Programação 1 - prova = questão Letras Distintas

palavra = input()
comparacao = input()

distintas = []

for p in palavra:
	for c in comparacao:
		if p == c: break
	else:
		distintas.append(p)
		 
print(len(distintas))		
