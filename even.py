def check_even(n):
    if n % 2 == 0:
        print(f'{n} is even')
        return True
    else:
        print(f'{n} is odd')
        return False

if __name__ == '__main__':
    try:
        n = int(input('Enter number to check if it is even or odd: '))
        check_even(n) 
    except ValueError as e:
        print('Please provide only integer numbers')

def test_check_even():
    #cmd to run this test
    #python3 -c 'import even; even.test_check_even()'
    assert check_even(2) == True
    assert check_even(3) == False
    