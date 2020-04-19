
def gcd_or_hcf(x,y):
    """Using Eculidean algorithm.
    Alternative easy approach import math; math.gcd(60,48)
    """
    while(y):
        x,y = y, x % y
    return x

if __name__ == "__main__":
    try:
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        hcf = gcd_or_hcf(x,y)
        print(f'GCD or HCF of {x} and {y} is {hcf}')
    except ValueError as e:
        print('Please provide only integer numbers')


def test_gcd_or_hcf():
    # cmd to run this test
    # python3 -c 'import gcd_or_hcf; gcd_or_hcf.test_gcd_or_hcf()'
    assert gcd_or_hcf(36,60) == 12
    assert gcd_or_hcf(54,24) == 6
    assert gcd_or_hcf(-54,-24) == -6