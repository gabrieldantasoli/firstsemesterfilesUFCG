def inverte3a3(s):
    combinacoes = []
    retorno = ''
    tresatres = ''
    for c in s:
        tresatres += c
        if len(tresatres) == 3:
            combinacoes.append(tresatres)
            tresatres = ''
    for c in range(len(combinacoes)-1,-1,-1):
        retorno += combinacoes[c]
    return retorno
