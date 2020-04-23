def pattern(n):
    k = 2 * n - 2
    for r in range(n,0,-1):
        for s in range(k,0,-1):
            print(end=" ")
        k = k + 1
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