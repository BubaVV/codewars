from codewars.test import Test

def order(sentence):
  words = sentence.split()
  words.sort(key=lambda word: int(''.join(c for c in word if c.isdigit())))
  return ' '.join(words)

Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")