def idosos_inicio(fila):
    position = 0
    for a in range(len(fila)):
        if fila[a] >= 60:
            fila[position] , fila[a] = fila[a] , fila[position]
            position += 1


