comprimento  = float(input())
largura = float(input())
profundidade = float(input())

volume = comprimento * largura * profundidade 
litros = volume * 1000

print(f'A piscina comporta {litros:.2f} litros de água.')
