
def swap_two_variables(a,b):
    a,b = b, a
    return a,b


if __name__ == "__main__":
    a = input('Enter content for first variable: ')
    b = input('Enter content for second variable: ')
    a,b = swap_two_variables(a,b)

    print(f'Value of first variable is {a}')
    print(f'Value of second variable is {b}')

def test_swap_two_variables():
    # cmd to run this test
    # python3 -c 'import swap_two_variables; swap_two_variables.test_swap_two_variables()'
    assert swap_two_variables(3,2) == (2,3)
    assert swap_two_variables('abc', 'def') == ('def', 'abc')