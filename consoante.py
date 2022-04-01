palavrasLidas = 0

while True:
	consoantes = 0
	vogais = 0
	palavra = input()
	for letra in palavra:
		if letra == 'a' or letra == 'A' or letra == 'e' or letra == 'E' or letra == 'i' or letra == 'I' or letra == 'o' or letra == 'O' or letra == 'u' or letra == 'U':
			vogais += 1
		else:
			consoantes += 1
	palavrasLidas += 1
	if consoantes > vogais : break

print(palavrasLidas)
