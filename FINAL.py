print('== Estágio 1 ==')
peso1 = float(input('Peso? '))
nota1 = float(input('Nota? '))
print('== Estágio 2 ==')
peso2 = float(input('Peso? '))
nota2 = float(input('Nota? '))
print('== Estágio 3 ==')
peso3 = float(input('Peso? '))
nota3 = float(input('Nota? '))

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3)

print('== Resultados ==')

media5 = (5 - media * 0.6) / 0.4
media7 = (7 - media * 0.6) / 0.4

print(f'Média parcial: {media:.1f}')
print(f'Nota na final, pra média 5.0 = {media5:.1f}')
print(f'Nota na final, pra média 7.0 = {media7:.1f}')
