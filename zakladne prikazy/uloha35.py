i = int(input('cislo od 2 - 9: '))

c = 1
for a in range(1,101):

    d = c // 100 
    e = c // 10  - d*10
    f = c // 1  -  d*100 - e*10

    if d == i or e == i or f == i:
        print('bum')

    elif c % i == 0:
        print('bum')

    else:
        print(c)

    c = c + 1
