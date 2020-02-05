#vypocet datumu velkej noci

while True:
    rok = int(input('Ktorý rok v 20. a 21. storočí? '))
    a = rok % 19
    b = rok % 4
    c = rok % 7
    m = 24
    n = 5
    d = (19*a + m) % 30
    e = (n + 2*b + 4*c + 6*d) % 7
    marec = 22 + d + e
    april = d + e - 9

    if rok == 2076 or rok == 1981:
        print(april-7,'.april')

    else:
        if marec <= 31:
            print(marec,'.marec')

        if april <= 30:
            print(april,'.april')

   
    


