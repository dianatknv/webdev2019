import math
a = int(input())
def pow(number):
    a = 1
    while(a < number):
        a *= 2
    if a == number:
        return True
    return False
if pow(a):
    print("YES")
else:
    print("NO")