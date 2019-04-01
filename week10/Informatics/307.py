def pow(a, n):
    k = 1
    cnt = 0
    while cnt < n:
        k *= a
        cnt += 1
    return k


a = input().split()
print(pow(float(a[0]), int(a[1])))