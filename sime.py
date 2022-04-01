# Universidade Federal de Campina Grande
# aluno : Gabriel Dantas De Oliveira
# matrícula : 121110669
# questão : Soma simétricos - soma elementos "opostos" em posição de uma lista

def soma_simetricos(lista):
    listaRetorno = []
    central = ''

    if len(lista) % 2 != 0:
        x = int((len(lista) - 1) / 2)
        central = lista[x]
        lista.pop(x)
    
    indiceoposto = len(lista) - 1
    if len(lista) > 1:
        for a in range(0,int((len(lista) - 1) / 2) + 1):
            listaRetorno.append(lista[a]+lista[indiceoposto])
            indiceoposto -= 1

    if central != '':
        listaRetorno.append(central)

    return listaRetorno


def test_1():
    assert soma_simetricos([0]) == [0]

def test_2():
    assert soma_simetricos([1]) == [1]
    
def test_3():
    assert soma_simetricos([2]) == [2]

def test_4():
    assert soma_simetricos([]) == []

def test_5():
    assert soma_simetricos([2, 8]) == [10]
    
def test_6():
    assert soma_simetricos([4, 9]) == [13]
    
def test_7():
    assert soma_simetricos([0, 0, 0, 0, 0]) == [0, 0, 0]
    
def test_8():
    assert soma_simetricos([4, 7, 10, 8, 7]) == [11, 15, 10]
    
def test_9():
    assert soma_simetricos([2, 9, 3, 9, 1, 0, 4, 7]) == [9, 13, 3, 10]
    
def test_10():
	assert soma_simetricos([1, 2, 3, 4, 9, 5, 6, 7, 8]) == [9, 9, 9, 9, 9]
