s = int(input('sekundy: '))
h = s//(60*60)
m = (s-h*60*60)//60
s = s - h*60*60 - m*60
print(h, 'h', m, 'm', s, 's')
