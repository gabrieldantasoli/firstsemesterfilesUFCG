mapas = []
sim = 0
nao = 0
while True:
	mapas.clear()
	mapa = input()
	if mapa == '###' : break
	for letra in mapa:
		if letra == 'i' or letra == 'c':
			mapas.append(0)
		else:
			mapas.append(1)
	ok = True
	regular = True
	for c in range(len(mapas)-1):	
		if mapas[c] != mapas[c+1] and ok:
			ok = False
		if not ok:
			if mapas[c+1] == 0:
				regular = False
				break
	if regular:
		sim += 1
	else:
		nao += 1

print(f'sim: {sim}')
print(f'não: {nao}')			
