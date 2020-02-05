k = int(input('k:' ))
l = int(input('l:' ))
m = int(input('m:' ))

if k + l > m and k + m > l and l + m > k:
    print('trojuholnik mozny')

    if k == m == l:
        print('rovnostranny')
    elif k == m or k == l or m == l:
        print('rovnoramenny')
    elif k**2 == l**2 + m**2  or l**2 == k**2 + m**2 or m**2 == k**2 + l**2:
        print('pravouhly')
    else:
        print('iny')
else:
    print('trojuholnik nemozny')
