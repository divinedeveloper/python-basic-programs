
def pattern(n):
    for r in range(0, n):
        for c in range(0, r + 1):
            print("*", end=" ")
        print()

pattern(5)

# O/P
'''
*
* *
* * *
* * * *
* * * * *
'''
