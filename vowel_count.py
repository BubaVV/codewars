from codewars.test import Test


def getCount(inputStr):
    return len([x for x in inputStr if x in 'aeiou'])

Test.assert_equals(getCount("abracadabra"), 5)