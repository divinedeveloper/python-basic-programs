def sum_digits_number(n):
    s = 0 
    while n:
        r = n % 10
        n = n // 10
        s = s + r
    return s

if __name__ == "__main__":
    try:
        n = int(input('Enter a number to find sum of its digits: '))
        res = sum_digits_number(n)
        print(f'Sum of individual digits of {n} is {res}')
    except ValueError as e:
        print('Please provide only integer numbers')


def test_sum_digits_number():
    # cmd to run this test
    # python3 -c 'import sum_digits_of_number; sum_digits_of_number.test_sum_digits_number()'
    assert sum_digits_number(2000) == 2
    assert sum_digits_number(121) == 4