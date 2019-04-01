import math
a = int(input())
b = 1
while b <= a:
    c = math.sqrt(b)
    if c - int(c) == 0:
        print(b)
    b += 1