
def pattern(n):
    x = 65
    for r in range(0, n):
        ch = chr(x)
        for c in range(0, r + 1):
            print(ch, end=' ')
        x += 1
        print()


pattern(5)


# O/P:
'''
A 
B B 
C C C 
D D D D 
E E E E E
'''