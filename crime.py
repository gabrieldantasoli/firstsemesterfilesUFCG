mensal = float(input())
maioreslimite = []

while True:
    sequencia = input()
    if sequencia == 'fim': break
    valores = sequencia.split()
    soma = 0
    for c in valores:
        soma += int(c)
    media = soma / len(valores)
    if media > mensal: maioreslimite.append(sequencia)
    if media < mensal/2: break

for c in maioreslimite:
    print(c)
