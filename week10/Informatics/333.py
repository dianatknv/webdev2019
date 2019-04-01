a = int(input())
b = int(input())
s = ''

while a <= b:
    if a % 2 == 0:
        s = s + str(a) + " "
    a += 1

print(s)
