
def pattern(n):
    k = 2 * n - 2
    x = 65
    for r in range(0, n):
        for s in range(0, k):
            print(end=' ')
        k = k - 1
        ch = chr(x)
        for c in range(0, r + 1):
            print(ch, end=' ')
        x += 1
        print()


pattern(5)