def check_palindrome(n):
    # simple trick is to use slicing
    # rev = int(str(n)[::-1])
    rev = 0; temp = n
    while n:
        r = n % 10
        n = n // 10
        rev = rev * 10 + r
    return True if temp == rev else False


if __name__ == "__main__":
    try:
        n = int(input('Enter a number to check if it is Palindrome: '))
        res = check_palindrome(n)
        result = "Palindrome number" if res else "not Palindrome number" 
        print(f'{n} is {result}')
    except ValueError as e:
        print('Please provide only integer numbers')


def test_check_palindrome():
    # cmd to run this test
    # python3 -c 'import palindrome_number; palindrome_number.test_check_palindrome()'
    assert check_palindrome(153) == False
    assert check_palindrome(121) == True