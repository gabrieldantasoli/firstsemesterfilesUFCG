def balanco(d1,d2):
    retorndict = {}

    for a in d1:
        retorndict[a] = d1[a]

    for b in d2:
        for c in retorndict:
            if b == c:
                retorndict[b] = d1[b] + d2[b]
                break
        else:
            retorndict[b] = d2[b]
    
    return retorndict
