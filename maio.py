def maioridade_penal(nomes,idades):
    nome = nomes.split()
    idade = idades.split()
    retorno = ''
    for c in range(len(nome)):
        if int(idade[c]) >= 18:
            retorno += nome[c]
        if c < len(nome)-1 and int(idade[c]) >= 18:
            retorno += ' '
    return retorno
