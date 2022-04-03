import math

raio = float(input())

areaCirculo = math.pi * raio**2

ladoQuadrado = raio/math.sqrt(2) * 2

areaQuadrado = ladoQuadrado**2

areaNaoComun = areaCirculo - areaQuadrado

print(f'Área não comum: {areaNaoComun:.5f}')
