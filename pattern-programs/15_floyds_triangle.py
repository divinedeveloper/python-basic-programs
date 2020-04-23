
def pattern(n):
    value = 1
    for r in range(0,n):
        for c in range(0,r+1):
            print(value, end=' ')
            value += 1
        print()
            

pattern(4)