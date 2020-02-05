spotreba = int(input('spotreba auta na 100km: '))
cena = int(input('cena benzinu za 1 liter: '))
vzdialenost = int(input('vzdialenost v km: '))
vysledok = spotreba/100*cena*vzdialenost
print('cena benzinu potrebneho na cestu: ', vysledok)
