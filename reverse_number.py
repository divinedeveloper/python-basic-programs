def reverse_number(n):
    # simple trick is to use slicing
    # rev = int(str(n)[::-1])
    rev = 0
    while n:
        r = n % 10
        n = n // 10
        rev = rev * 10 + r
    return rev


if __name__ == "__main__":
    try:
        n = int(input('Enter a number to reverse it: '))
        res = reverse_number(n)
        print(f'Reverse of {n} is {res}')
    except ValueError as e:
        print('Please provide only integer numbers')


def test_reverse_number():
    # cmd to run this test
    # python3 -c 'import reverse_number; reverse_number.test_reverse_number()'
    assert reverse_number(153) == 351
    assert reverse_number(1634) == 4361
    assert reverse_number(121) == 121