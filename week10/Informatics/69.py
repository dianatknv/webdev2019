a = []
n = int(input())
a = input().split()
cnt = 0
for x in range(0, int(n/2)):
    m = int(a[x])
    a[x] = int(a[n - x - 1])
    a[n - x - 1] = m
for x in range(0, n):
    print(a[x], end=" ")