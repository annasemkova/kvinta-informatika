a = int(input('prve cislo:'))
b = int(input('druhe cislo:'))
c = int(input('tretie cislo:'))

x1, x2, x3 = 0, 0, 0

if a > b and a > c:
    x1 = a
    if b > c:
        x2 = b
        x3 = c
    else:
        x2 = c
        x3 = b


if b > a and b > c:
    x1 = b
    if a > c:
        x2 = a
        x3 = c
    else:
        x2 = c
        x3 = a

if c > b and c > a:
    x1 = c
    if b > a:
        x2 = b
        x3 = a
    else:
        x2 = a
        x3 = b

print(x3, x2, x1)
 
