
def gcd_or_hcf(x,y):
    """Using Eculidean algorithm.
    Alternative easy approach import math; math.gcd(60,48)
    """
    while(y):
        x,y = y, x % y
    return x

def compute_lcm(x,y):
    """Using Formula
    x * y = LCM(x,y) * GCD(x,y)
    """
    lcm = (x * y) // gcd_or_hcf(x,y)
    return lcm

if __name__ == "__main__":
    try:
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        lcm = compute_lcm(x,y)
        print(f'LCM of {x} and {y} is {lcm}')
    except ValueError as e:
        print('Please provide only integer numbers')


def test_compute_lcm():
    # cmd to run this test
    # python3 -c 'import lcm; lcm.test_compute_lcm()'
    assert compute_lcm(15,25) == 75
    assert compute_lcm(54,24) == 216
    assert compute_lcm(-54,-24) == -216