a = []
n = int(input())
a = input().split()
cnt = 0
for x in range(1, n):
    if int(a[x]) > int(a[x-1]):
        cnt += 1
print(cnt)