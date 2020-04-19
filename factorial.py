
def factorial_recursion(n):
    #alternative iterative approach
    #f=1, n
    # for  i in range(n, 0 , -1): f = f* i

    if n <= 1:
        return 1
    else:
        return n * factorial_recursion(n-1)

if __name__ == "__main__":
    try:
        x = int(input('Enter a number to find its factorial: '))
        res = factorial_recursion(x)
        print(f'Factorial of {x} is {res}')
    except ValueError as e:
        print('Please provide only integer numbers')

def test_factorial():
    # cmd to run this test
    # python3 -c 'import factorial; factorial.test_factorial()'
    assert factorial_recursion(5) == 120
    assert factorial_recursion(-5) == 1