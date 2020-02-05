a = int(input('prve cislo: '))
b = int(input('druhe cislo: '))

sucet = 0
cislo = 0
if a > b:
    cislo = cislo + b
    for i in range(1,a - b + 1):
        if cislo % 3 == 0:
            sucet = sucet + cislo
        cislo = cislo +1
    
else:
    cislo = cislo + a
    for i in range(1,b - a + 1):
        if cislo % 3 == 0:
            sucet = sucet + cislo
        cislo = cislo + 1

print(sucet)
