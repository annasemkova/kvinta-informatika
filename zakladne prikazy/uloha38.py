a = int(input("prirodzene cislo n: "))
vsetko = ""
vsetko2 = 0

for x in range(1,2*a-1,2):
    vsetko2 = vsetko2 + x
    vsetko = vsetko + str(x) + " + "
vsetko = vsetko + str(2*a-1)
vsetko2 = vsetko2 + 2*a-1

print(vsetko, "=", vsetko2)
