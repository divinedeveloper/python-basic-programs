
def pattern(n):
    k = 2 * n - 2
    for r in range(0,n):
        for s in range(0, k):
            print(end=' ')
        k = k - 1
        for c in range(0, r + 1):
            print('10', end='')
        print()


pattern(5)


# O/P:
'''
        10
       1010
      101010
     10101010
    1010101010
'''