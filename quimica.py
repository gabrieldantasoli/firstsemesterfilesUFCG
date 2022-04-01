H=1
S=32
O=16
C=12
Ca=40
Na=23
P=31

lista = []
while True:
    x=input()
    if x == 'fim': break
    x=x.split()
    for c in x:
        print(c.isdigit())
