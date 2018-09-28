from codewars.test import Test

def duplicate_encode(word):
    result = ['(' if word.lower().count(x) == 1 else ')' for x in word.lower()]
    return ''.join(result)


if __name__ == '__main__':
    Test.assert_equals(duplicate_encode("din"), "(((")
    Test.assert_equals(duplicate_encode("recede"), "()()()")
    Test.assert_equals(duplicate_encode("Success"), ")())())", "should ignore case")
    Test.assert_equals(duplicate_encode("(( @"), "))((")
    Test.assert_equals(duplicate_encode('x@bR!Plyv'), '(((((((((')