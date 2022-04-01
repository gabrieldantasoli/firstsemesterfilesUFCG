congelado = float(input())
descongelado = float(input())

percentagem = (1 - descongelado / congelado) *100

if percentagem < 5:
    qualidade = 'Produto qualis A.'
elif percentagem < 10:
    qualidade = 'Produto em conformidade.'
else:
    qualidade = 'Produto não conforme.'

print(f'{percentagem:.1f}% do peso do produto é de água congelada.')
print(qualidade)
