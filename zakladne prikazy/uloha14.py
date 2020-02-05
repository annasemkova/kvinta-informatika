k = int(input('k:' ))
l = int(input('l:' ))
m = int(input('m:' ))

if k + l > m and k + m > l and l + m > k:
            print('trojuholnik mozny')
else:
    print('trojuholnik nemozny')
