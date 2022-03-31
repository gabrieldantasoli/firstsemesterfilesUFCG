numeros = []

soma = 0
soma1 = 0
count = 0

while True:
    if soma1 < 100:
        num = int(input())
        soma1 += num
    if soma1 >= 100 or num < 0: break
    numeros.append(num)
    count += 1
    soma += num

media = soma / count

for num in range(len(numeros)):
    if numeros[num] > media:
        print(f'{numeros[num]} > {media:.3f}')
    if numeros[num] < media:
        print(f'{numeros[num]} < {media:.3f}')
