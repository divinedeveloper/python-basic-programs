from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_series_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_series_recursion(n-1) + fibonacci_series_recursion(n-2)

def fib_sequence(n):
    results = []
    for i in range(n):
        results.append(str(fibonacci_series_recursion(i)))
        # we can print here alsobut using list for unit test purpose
        # print(fibonacci_series_recursion(i), end=' ')
    return results

if __name__ == "__main__":
    try:
        n = int(input('Enter a number of terms for fibonacci series: '))
        if n <= 0:
            print('Please provide only positive integer number')
        else:
            res = fib_sequence(n)
            print(' '.join(res))
        
    except ValueError as e:
        print('Please provide only positive integer number')       

def test_fibonacci_series():
    # cmd to run this test
    # python3 -c 'import fibonacci_series; fibonacci_series.test_fibonacci_series()'
    assert fib_sequence(5) == ['0', '1', '1', '2', '3']