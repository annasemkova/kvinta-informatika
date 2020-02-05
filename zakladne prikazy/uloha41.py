a = int(input("zadane cislo n: "))

print("a)")
for x in range(a):
    print(a*"*")

print("b)")
for x in range(a):
    print(x*"*")

print("c)")
b = list(range(a))
b.reverse()
for x in b:
    print(x*"*")

print("d)")
l = a*2-1
m, n = 0, 0
for x in range(a):
    s = m*" " + l*"*" + n*" "
    print(s)
    l = l - 2
    m = m + 1
    n = n + 1

print("e)")
print(a*"*")
for x in range(a-2):
    s = "*" + (a-2)*" " + "*"
    print(s)
print(a*"*")

print("f)")
l = a
m = 0
for x in range(a):
    s = m*" " + l*"*"
    print(s)
    l = l - 1
    m = m + 1

print("g)")
a = list(range(1,a))
b = list(a)
b.reverse()
b.remove(b[0])
c = a + b
for x in c:
    print(x*"*")

print("h)")
for x in c:
    print((x-1)*" " + "*")





















