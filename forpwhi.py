fator = int(input())

tabu = 0
while True:
    produto = tabu * fator
    print(f"{fator}  x {tabu:2}  = {produto:3}")
    tabu += 1
    if tabu > 10: break
