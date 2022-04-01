dobradas = []
naodobradas = []

quantidadesPalavras = int(input())

for c in range(quantidadesPalavras):
    palavra = input()
    letraanterior = palavra[0]
    adicionado = False
    for letra in range(1,len(palavra)):
        letraAtual = palavra[letra]
        if letraAtual == letraanterior and adicionado == False:
            dobradas.append(palavra)
            adicionado = True
        letraanterior = letraAtual
    if adicionado == False:
        naodobradas.append(palavra)

print(f'{len(dobradas)} palavra(s) com letras dobradas:') 
for palavra in dobradas:
    print(palavra)
print('---')
print(f'{len(naodobradas)} palavra(s) sem letras dobradas:')
for palavra in naodobradas:
    print(palavra)
