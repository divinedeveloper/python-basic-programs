
def pattern(n):
    k = 2 * n - 2

    for r in range(0, n):
        x = 65
        for s in range(0, k):
            print(end=' ')
        k = k - 1

        for c in range(0, r + 1):
            ch = chr(x)
            print(ch, end=' ')
            x += 1
        print()

    k = n
    for r in range(n, 0, -1):
        for s in range(k, 0, -1):
            print(end=' ')
        k = k + 1

        for c in range(0, r - 1):
            ch = chr(x)
            print(ch, end=' ')
            x += 1
        print()


pattern(5)

# O/P:

'''
        A 
       A B 
      A B C 
     A B C D 
    A B C D E 
     F G H I 
      J K L 
       M N 
        O 
'''