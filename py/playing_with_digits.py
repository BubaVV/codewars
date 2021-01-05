from codewars.test import Test as test

def dig_pow(n, p):
    result = 0
    for position, digit in enumerate(str(n), p):
        result += int(digit)**position
    if result % n == 0:
        return result / n
    else:
        return -1

test.assert_equals(dig_pow(89, 1), 1)
test.assert_equals(dig_pow(92, 1), -1)
test.assert_equals(dig_pow(46288, 3), 51)