

def pattern(n):
    for r in range(n, 0, -1):
        for c in range(1, r + 1):
            print(c, end=' ')
        print()


pattern(5)


# O/P:
'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''