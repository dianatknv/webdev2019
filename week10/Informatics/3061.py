import math
a = int(input())
def pow(number):
    a = 1
    cnt = 0
    while(a < number):
        a *= 2
        cnt += 1
    return cnt
print(pow(a))