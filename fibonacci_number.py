from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_number_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_number_recursion(n-1) + fibonacci_number_recursion(n-2)

if __name__ == "__main__":
    try:
        n = int(input('Enter nth fibonacci number: '))
        if n < 0:
            print('Please provide only positive integer number')
        else:
            res = fibonacci_number_recursion(n)
            print(res)
        
    except ValueError as e:
        print('Please provide only positive integer number')       

def test_fibonacci_number():
    # cmd to run this test
    # python3 -c 'import fibonacci_number; fibonacci_number.test_fibonacci_number()'
    assert fibonacci_number_recursion(5) == 5
    assert fibonacci_number_recursion(4) == 3