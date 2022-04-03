x = input()

x = x.split()

def soma(num) :
    total = 0
    for c in num:
        total += int(c)
    return total

s = soma(x)
print(s)
