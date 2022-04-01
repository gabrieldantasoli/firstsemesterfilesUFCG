nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

pond1 = float(input())
pond2 = float(input())
pond3 = 100 - (pond1+pond2)

ponderada = (nota1 * pond1 + nota2 * pond2 + nota3 * pond3) / 100

print(f'Média Final: {ponderada:.1f}')
