def pattern(n):
    for r in range(n,0,-1):
        for c in range(0, r):
            print("*", end=" ")
        print()

pattern(5)

# O/P
'''
* * * * * 
* * * * 
* * * 
* * 
*
'''