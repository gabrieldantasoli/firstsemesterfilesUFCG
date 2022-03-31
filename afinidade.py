def tem_afinidade(l1,l2):
    afinidade = 0 
    for c in l1:
        for d in l2:
            if c == d: afinidade += 1
    if afinidade >= 3: return True
    else:
        return False
