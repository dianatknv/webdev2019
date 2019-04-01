def minn(a, b, c, d):
    return min(a, min(b, min(c, d)))


a = input().split()
print(minn(a[0], a[1], a[2], a[3]))