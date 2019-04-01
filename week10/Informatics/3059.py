import math
a = int(input())
b = 1
def pow(number):
    a = 1
    while(a < number):
        a *= 2
    if a == number:
        return True
    return False
while b <= a:
    if pow(b):
        print(b, end=" ")
    b += 1
