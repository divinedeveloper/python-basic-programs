import math

def check_prime(n):
    """Number which is divisible only by 1 and itself.
    we will use the efficient sqrt approach."""
    if n == 1: return False

    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        x = int(input('Enter a number to check if it is prime or not: '))
        res = check_prime(x)
        print(f'{x} is {"Prime" if res else "not Prime"}')
    except ValueError as e:
        print('Please provide only integer numbers')

def test_check_prime():
    # cmd to run this test
    # python3 -c 'import prime; prime.test_check_prime()'
    assert check_prime(5) == True
    assert check_prime(4) == False
    