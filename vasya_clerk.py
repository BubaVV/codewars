from codewars.test import Test as test

def max_note(notes, value):
    '''
    :param notes: array of banknotes, read-only
    :param value: amount of return
    :return: index of banknote or None
    '''
    sorted_notes = sorted([x for x in notes if x<=value], reverse=True)
    if len(sorted_notes) == 0:
        return None
    else:
        return notes.index(sorted_notes[0])

def tickets(people):
    PRICE = 25
    cash = []
    for request in people:
        cash.append(request)
        change = request - PRICE
        while change > 0:
            change_note = max_note(cash, change)
            if change_note is None:
                return 'NO'
            change -= cash.pop(change_note)

    return "YES"


test.assert_equals(max_note([10, 25, 50], 30), 1)
test.assert_equals(max_note([10, 25, 50], 100), 2)
test.assert_equals(max_note([10, 25, 50], 5), None)
test.assert_equals(tickets([25, 25, 50]), "YES")
test.assert_equals(tickets([25, 100]), "NO")