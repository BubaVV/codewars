from codewars.test import Test as test


def openOrSenior(data):
    return ['Senior' if x[0] >= 55 and x[1] > 7 else 'Open' for x in data]

test.assert_equals(openOrSenior([[45, 12], [55, 21], [19, -2], [104, 20]]), ['Open', 'Senior', 'Open', 'Senior'])
test.assert_equals(openOrSenior([[16, 23], [73, 1], [56, 20], [1, -1]]), ['Open', 'Open', 'Senior', 'Open'])