

def pattern(n):
    x = 65
    k = 2 * n - 2
    for r in range(0, n):
        for s in range(0, k):
            print(end=' ')
        k = k - 1
        for c in range(0, r + 1):
            ch = chr(x)
            print(ch, end=' ')
            x += 1
        print()


pattern(7)


# O/P:
'''
            A 
           B C 
          D E F 
         G H I J 
        K L M N O 
       P Q R S T U 
      V W X Y Z [ \
'''