# Pascal function
def pattern(n):
    '''
    C(line, i)   = line! / ( (line-i)! * i! )
    C(line, i-1) = line! / ( (line - i + 1)! * (i-1)! )
    We can derive following expression from above two expressions.
    C(line, i) = C(line, i-1) * (line - i + 1) / i

    So C(line, i) can be calculated from C(line, i-1) in O(1) time
    '''
    for line in range(1, n + 1):
        c = 1  # used to represent C(line, i)
        for i in range(1, line + 1):
            # The first value in a
            # line is always 1
            print(c, end=" ")
            c = int(c * (line - i) / i)
        print("")


pattern(5)

# O/P:

'''
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
'''