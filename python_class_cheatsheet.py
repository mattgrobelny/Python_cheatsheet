class MyClass():
    """A simple example class"""
    i = 12345
    a = 0

    def __init__(self):
        # set default self values
        self.data = [1, 2, 3]
        self.i = 12345
        self.a = 0
    # set up self functions

    def f(self):
        return 'hello world'

    # functions which effect self
    def test_add(self, x, y):
        self.a = x + y
        return self.a


x = MyClass()
print x.i
print x.f()
print x.data
print x.a
print x.test_add(1, 2)
print x.a
