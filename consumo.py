watts = float(input())
time = float(input())

consumo = (watts * time) / 60000

print(f'{consumo:.1f} kWh')
