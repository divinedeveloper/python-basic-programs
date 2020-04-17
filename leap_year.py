
def check_leap_year(year):
    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        print(f'{year} is a leap year')
        return True
    else:
        print(f'{year} is Not a leap year')
        return False



if __name__ == "__main__":
    try:
        year = int(input('Enter year to check if it is leap year or not: '))
        if year > 0:
            check_leap_year(year)
        else:
            print('Please provide year only in positive numbers')
    except ValueError as e:
        print('Please provide year only in  numbers')

def test_check_leap_year():
    # cmd to run this test
    # python3 -c 'import leap_year; leap_year.test_check_leap_year()'
    assert check_leap_year(2000) == True
    assert check_leap_year(2001) == False
    