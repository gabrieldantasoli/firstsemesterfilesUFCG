lado1 = float(input())
lado2 = float(input())
areaCasas = float(input())

areaTerreno = lado1 * lado2
qtdCasas = areaTerreno // areaCasas

print(f'{qtdCasas:.0f} casa(s) pode(m) ser construída(s) no terreno.') 
