day1 = int(input())
day2 = int(input())
day3 = int(input())
day4 = int(input())
day5 = int(input())

minutosSemana = 7200
soma = day1 + day2 + day3 + day4 + day5
media = soma / 5
episodios = soma // 50
porcentagem = f'{(soma / minutosSemana) * 100:.2f}' 

print(f'Você perdeu {soma} min na semana (média de {media:.1f} min por dia).')
print(f'Isso significa {porcentagem}% da sua semana produtiva.')
print(f'Daria para assistir {episodios} episódio(s) de House.')
