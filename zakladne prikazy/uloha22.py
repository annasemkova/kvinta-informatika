import random

p = 0

for i in range(100000):
    m = random.randint(0,101)
    z = random.randint(0,101)
    if m <= 4 and z <= 5:
        print('matrix time')
    
