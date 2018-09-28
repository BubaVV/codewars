from functools import reduce
from operator import xor

from codewars.test import Test as test

def find_it(seq):
    return reduce(xor, seq)

test.describe("Example")
test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)