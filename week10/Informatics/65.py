a = []
n = int(input())
a = input().split()
cnt = 0
for x in range(0, n):
    if int(a[x]) > 0:
        cnt += 1
print(cnt)
