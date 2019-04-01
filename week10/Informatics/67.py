a = []
n = int(input())
a = input().split()
cnt = 0
for x in range(1, n):
    if (int(a[x]) > 0 and int(a[x-1]) > 0) or (int(a[x]) < 0 and int(a[x-1]) < 0):
        cnt += 1
if cnt > 0:
    print("YES")
else:
    print("NO")