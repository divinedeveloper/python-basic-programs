

def pattern(n):
    for r in range(0, n):
        for c in range(0, n):
            if c == 0 or r - c == 3 or r + c == 3:
                print('*', end='')
            else:
                print(end=' ')
        print()


pattern(7)


# O/P:
'''

*  *   
* *    
**     
*      
**     
* *    
*  *   

'''