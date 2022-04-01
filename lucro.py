meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
lucro = []

for num in range(12):
	valores = input()
	valores = valores.split()
	valores = float(valores[0])-float(valores[1])
	lucro.append(valores)

for num in range(12):
	print(f'{meses[num]} {lucro[num]:>4.1f}')
