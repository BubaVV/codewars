from codewars.test import Test as test

def find_uniq(arr):
    counter = {}
    for value in arr:
        if value not in counter:
            counter[value] = 1
        else:
            counter[value] += 1
    result = {k : v for k, v in counter.items() if v == 1}
    return next(iter(result))

test.describe("Basic Tests")
test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)