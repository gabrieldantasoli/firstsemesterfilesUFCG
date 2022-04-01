# Universidade Federal de Campina Grande
# aluno : Gabriel Dantas De Oliveira
# matrícula : 121110669
# questão : Soma simétricos - soma elementos "opostos" em posição de uma lista

index = 1
total = 0
invalidas = 0

while True:
    pares = 0
    impares = 0
    linha = input()
    linha2 = linha.split()

    if linha == 'fim': break
    
    for num in linha2:
        if int(num) % 2 == 0:
            pares += 1
        else:
            impares += 1

    if impares >= pares:
        invalidas += 1
        print(f'linha {index} inválida: {linha}')
    total += 1

    index += 1

print(f'sequências lidas: {total} (inválidas: {invalidas})')
