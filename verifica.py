def calcula_digitos_verificacao(numeros):
    cpf = []
    for c in range(len(numeros)-1,-1,-1):
        cpf.append(numeros[c])
    soma = 0
    for num in range(10,1,-1):
        soma += int(cpf[num-2]) * num
    soma = (soma * 10) % 11  
    digito1 = soma
    cpf = []
    numeros += f'{digito1}'
    for c in range(len(numeros)-1,-1,-1):
            cpf.append(numeros[c])
    soma = 0
    for num in range(11,1,-1):
        soma += int(cpf[num-2]) * num
    soma = (soma * 10) % 11
    digito2 = soma
    verificador = f'{digito1}{digito2}'
    return verificador

assert calcula_digitos_verificacao('153245875') == '40'
