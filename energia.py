def calcula_conta(tabela):
    total = 0
    wattHora = 0
    for a in range(1,len(tabela)):
        watts=1
        for b in range(1,len(tabela[a])):
            watts *= tabela[a][b]
        wattHora += watts
    kwh = wattHora/1000
    total = kwh * 0.28
    total = f"R$ {total:.2f}"
    return total
