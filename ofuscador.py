def ofuscador(linha):
    lista = []
    lista2 = linha.split(' ')
    espacos = 0
    for c in range(len(linha)):
        if linha[c] == ' ':
            espaco = '*'*len(lista2[espacos])
            lista.append(espaco)
            espacos += 1
        elif ord(linha[c]) >= 65 and ord(linha[c]) <= 122:
            if ord(linha[c]) >= 97:
                lista.append(chr(ord(linha[c]) - 32))    
            elif ord(linha[c]) < 97:
                lista.append(chr(ord(linha[c]) + 32))
        else:
            lista.append(linha[c])
            
    for c in range(len(lista)):
                if lista[c] == 'a' or lista[c] == 'A':
                    lista[c] = 4
                elif lista[c] == 'b' or lista[c] == 'B':
                    lista[c] = 8
                elif lista[c] == 'e' or lista[c] == 'E':
                    lista[c] = 3
                elif lista[c] == 'g' or lista[c] == 'G':
                    lista[c] = 6
                elif lista[c] == 'i' or lista[c] == 'I':
                    lista[c] = 1
                elif lista[c] == 'l' or lista[c] == 'L':
                    lista[c] = 7
                elif lista[c] == 's' or lista[c] == 'S':
                    lista[c] = 5
                elif lista[c] == 'o' or lista[c] == 'O':
                    lista[c] = 0
    retorno = ''
    for c in lista:
        retorno += str(c)
    return retorno

def test_1():
    assert ofuscador('Meu carro e azul') == 'm3U***C4RR0*****3*4ZU7'

def test_2():
    assert ofuscador('comprei um carro') == 'C0MPR31*******UM**C4RR0'

def test_3():
    assert ofuscador('Eu prefiro javascript') == '3U**PR3F1R0*******J4V45CR1PT'
