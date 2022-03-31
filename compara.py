def compara_senhas(senha1, senha2):
    compa1 = 0
    compa2 = 0
    for c in range(len(senha1)):
        if c < len(senha1) and c < len(senha2):
            if senha1[c] != senha2[c]:
                compa1 += 1
    for c in range(len(senha2)):
        if c < len(senha2) and c < len(senha1):
            if senha2[c] != senha1[c]:
                compa2 += 1
    if compa1 == compa2:
        return compa1
