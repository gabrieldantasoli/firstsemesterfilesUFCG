def decifra(chave,palavra):
    retorno = ''
    for a in palavra:
        if chave[a]:
            retorno += chave[a]
        else:
            retorno += a
    return retorno
