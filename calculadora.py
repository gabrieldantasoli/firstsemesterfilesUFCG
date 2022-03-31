adultos = int(input())
criancas = int(input())
preco = float(input())

total = adultos * preco + criancas * (preco/2)

print(f'Total: R$ {total:.2f}')
