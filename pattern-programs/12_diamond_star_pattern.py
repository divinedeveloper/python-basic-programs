
def pattern(n):
    for r in range(n):
        for c in range(n):
            if r + c == 2 or r - c == 2 or c - r == 2 or r + c ==  6:
                print('*', end='')
            else:
                print(end=' ')
        print()


pattern(5)


# O/P: