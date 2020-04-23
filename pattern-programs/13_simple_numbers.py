
def pattern(n):
    for r in range(1, n + 1):
        for c in range(0, r):
            print(r, end=' ')
        print()


pattern(5)        

# O/P:
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''