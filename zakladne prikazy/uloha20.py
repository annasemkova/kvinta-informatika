a = int(input('prve cislo: '))
b = int(input('druhe cislo: '))
c = int(input('tretie cislo: '))

if a == b == c:
    print('vsetky tri rovnake')
elif a == b or b == c or a == c:
    print('iba dve rovnake')
else:
    print('vsetky tri rozne')
