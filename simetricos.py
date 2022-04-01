def soma_simetricos(valores):
    listaRetorno = []
    ok = False
    if len(valores) % 2 != 0:
        central = valores[int(((len(valores)-1)/2)+1)-1]
        valores.pop(int(((len(valores)-1)/2)+1)-1)
        ok = True
    primeiros = 0
    ultimos = len(valores)-1
    for c in range(int(((len(valores)-1)/2)+1)):
        listaRetorno.append(valores[primeiros]+valores[ultimos])
        primeiros += 1
        ultimos -= 1
    
    if ok:
        listaRetorno.append(central)
    return listaRetorno

