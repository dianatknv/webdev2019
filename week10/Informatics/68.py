a = []
n = int(input())
a = input().split()
cnt = 0
for x in range(1, n - 1):
    if int(a[x]) > int(a[x-1]) and int(a[x]) > int(a[x+1]):
        cnt += 1
print(cnt)