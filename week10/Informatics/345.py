n = int(input())
cnt = 0
for x in range(1, n+1):
    a = int(input())
    if a == 0:
        cnt+=1
print(cnt)