from codewars.test import Test as test

def rgb(*args):
    valid_args = [x if x>0 else 0 for x in args]
    valid_args = [x if x<=255 else 255 for x in valid_args]
    return '{:02X}{:02X}{:02X}'.format(*valid_args)

test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")