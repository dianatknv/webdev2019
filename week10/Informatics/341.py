import math
a = int(input())
cnt = int(2)
if a==1:
    print(1)
    exit()
for i in range(2, int(math.sqrt(a))+1):
    if a % i == 0:
        cnt += 1
        if i != a / i:
            cnt += 1
print(cnt, end=" ")