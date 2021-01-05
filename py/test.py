class Test():
    def __init__(self):
        pass

    @staticmethod
    def describe(arg):
        pass

    @staticmethod
    def assert_equals(func, result, *args):
        if func == result:
            return True
        else:
            print(func, '!=', result)
            raise AssertionError