#a=4 pi r2
#v=4 pi r3 /3
import math

raio = float(input())

area = 4 * math.pi * raio**2
volume = (4 * math.pi * raio **3)/3

print(f'{area:.2f}')
print(f'{volume:.2f}')
