a = []
n = int(input())
a = input().split()
for x in range(0, n):
    if int(a[x]) % 2 == 0:
        print(a[x], end=" ")