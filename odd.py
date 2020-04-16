def check_odd(n):
    if n % 2 != 0:
        print(f'{n} is odd')
        return True
    else:
        print(f'{n} is not odd')
        return False

if __name__  == '__main__':
    try:
        n = int(input('Enter number to check if it is odd or not: '))
        check_odd(n)
    except ValueError as e:
        print('Please provide only integer numbers')

def test_check_odd():
    #cmd to run this test
    #python3 -c 'import odd; odd.test_check_odd()'
    assert check_odd(0) == False
    assert check_odd(1) == True
    assert check_odd(-1) == True
    assert check_odd(2) == False
    assert check_odd(-2) == False