def is_substring(str1,str2):
    for c in range(len(str1)-len(str2)+1):
        comp = ''
        for v in range(c,len(str2)+c):
            comp += str1[v]
        if comp == str2:
            return True
    else:
        return False


print(is_substring('casorio','casa'))

