x = int(input('cislo vacsie ako nula a mensie ako sto: '))
# styri + dsat/desiat + dva
# dva   + nast        + ''
# a     + b           + c
# jeden, jedenast, dvadastjeden, tridsatjeden, styridsatjeden, 

#pole
if x == 1:
    pole = str('sedela')
    vrany = str('vrana')
elif 2 <= x <= 4:
    pole = str('sedeli')
    vrany = str('vrany')
else:
    pole = str('sedelo')
    vrany = str('vran')


#vacsie ako 10
if x <= 19:
    if x <= 10:
        if x == 1:
            cislo = str('jedna')
        elif x == 2:
            cislo = str('dve')
        elif x == 3:
            cislo = str('tri')
        elif x == 4:
            cislo = str('styri')
        elif x == 5:
            cislo = str('pat')
        elif x == 6:
            cislo = str('sest')
        elif x == 7:
            cislo = str('sedem')
        elif x == 8:
            cislo = str('osem')
        elif x == 9:
            cislo = str('devat')

            
    elif 11 <= x <= 19:
        if x == 11:
            cislo = str('jedenast')
        elif x == 12:
            cislo = str('dvanast')
        elif x == 13:
            cislo = str('trinast')
        elif x == 14:
            cislo = str('strnast')
        elif x == 15:
            cislo = str('patnast')
        elif x == 16:
            cislo = str('sestnast')
        elif x == 17:
            cislo = str('sedemnast')
        elif x == 18:
            cislo = str('osemnast')
        elif x == 19:
            cislo = str('devatnast')
    print('Na poli '+ pole + ' ' + cislo +' '+ vrany)

else:
    #a
    m = x // 10
    if m == 2:
        a = str('dva')
    elif m == 3:
        a = str('tri')
    elif m == 4:
        a = str('styri')
    elif m == 5:
        a = str('pat')
    elif m == 6:
        a = str('sest')
    elif m == 7:
        a = str('sedem')
    elif m == 8:
        a = str('osem')
    elif m == 9:
        a = str('devat')

    #b
    if 10 < x < 50:
        b = str('dsat')
    elif 50 <= x:
        b = str('desiat')
        
    #c
    n = x % 10
    if n == 2:
        c = str('dva')
    elif n == 3:
        c = str('tri')
    elif n == 4:
        c = str('styri')
    elif n == 5:
        c = str('pat')
    elif n == 6:
        c = str('sest')
    elif n == 7:
        c = str('sedem')
    elif n == 8:
        c = str('osem')
    elif n == 9:
        c = str('devat')

    print('Na poli '+ pole +' '+ a+b+c+' '+ vrany)

