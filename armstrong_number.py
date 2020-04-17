def check_armstrong(n):
    s = 0; temp = n
    order = len(str(n)) 
    while n:
        r = n % 10
        n = n // 10
        s = s + (r ** order)
    return True if s == temp else False


if __name__ == "__main__":
    try:
        n = int(input('Enter a number to check if it is armstrong number: '))
        res = check_armstrong(n)
        result = "armstrong number" if res else "not armstrong number" 
        print(f'{n} is {result}')
    except ValueError as e:
        print('Please provide only integer numbers')


def test_armstrong_number():
    # cmd to run this test
    # python3 -c 'import armstrong_number; armstrong_number.test_armstrong_number()'
    assert check_armstrong(153) == True
    assert check_armstrong(1634) == True
    assert check_armstrong(121) == False
    assert check_armstrong(1253) == False