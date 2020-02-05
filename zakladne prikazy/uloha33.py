i = int(input('save me pls (alternativne sestmiestne cislo): '))

a = i // 100000
b = i // 10000 - a*10
c = i // 1000 - a*100 - b*10
d = i // 100 - a*1000 - b*100 - c*10
e = i // 10  - a*10000 - b*1000 - c*100 - d*10
f = i // 1  - a*100000 - b*10000 - c*1000 - d*100 - e*10

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
