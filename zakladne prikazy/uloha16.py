vaha = float(input('vaha v kg:'))
vyska = float(input('vyska v m:'))
bmi = vaha/vyska**2

if bmi < 18.5:
    print('podvaha')
elif 18.5 <= bmi < 25:
    print('normalna hmotnost')
elif 25 <= bmi < 30:
    print('nadvaha')
elif bmi >= 30:
    print('obezita')
