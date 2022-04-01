# UNIVERSIDADE FEDERAL DE CAMPINA GRANDE - UFCG
# GABRIEL DANTAS DE OLIVEIRA - 121110669
# 14/03/2022 
# Programação 1 - questão 2 - Somando os Ultimos Números

numeros = []

quantidadeNumeros= int(input())

soma = 0
count = 0
for num in range(quantidadeNumeros):
	numero = int(input())
	numeros.append(numero)
	soma += numero
	count += 1

media = soma / count

soma = 0
for num in range(len(numeros)):
	soma += numeros[len(numeros)-1-num]
	if numeros[len(numeros)-1-num] >= media: break

print(soma)
