peniaze = int(input('peniaze:'))
den = int(input('den:'))
cas = int(input('cas:'))

if den == 1:
    if cas < 17:
        if peniaze >= 7:
            print('kino o 17')
    if cas < 20:
        if peniaze >= 7:
            print('kino o 20')
else:
    if cas < 20:
        if peniaze >= 18:
            print('divadlo o 20')
        if peniaze >= 7:
            print('kino o 20')
    if cas < 17:
        if peniaze >= 7:
            print('kino o 17')

print('life is not defined')
