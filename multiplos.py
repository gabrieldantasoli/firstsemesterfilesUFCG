limite = int(input())

numAtual = 5
while True:
    if limite > numAtual and numAtual % 2 == 0:
        print(numAtual)
    numAtual += 5
    if limite <= numAtual: break
