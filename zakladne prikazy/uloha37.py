for x in range(1,1000001):
    suciny = 0
    for y in range(1,x):
        if x % y == 0:
            suciny = suciny + y

    if x == suciny:
        print(x)

print("you have reached the end of matrix")
