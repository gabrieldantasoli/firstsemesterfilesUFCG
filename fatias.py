convidados = int(input())

op1 = 32 // convidados 
op1resto = 32 % convidados
op2 = 32 / convidados

print(f'Opção 1: {op1} fatias cada, {op1resto} de resto')
print(f'Opção 2: {op2:.2f} fatias cada')
