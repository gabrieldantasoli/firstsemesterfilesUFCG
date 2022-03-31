nadador = str(input())
idade = int(input())

if idade < 5:
    categoria = 'Não pode competir'
elif idade < 8:
    categoria = 'Infantil A'
elif idade < 11:
    categoria = 'Infantil B'
elif idade < 14:
    categoria = 'Juvenil A'
elif idade < 18:
    categoria = 'Juvenil B'
else:
    categoria = 'Senior'

print(f'{nadador}, {idade} anos, {categoria}.')
