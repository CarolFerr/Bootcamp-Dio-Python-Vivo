class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        # se existir retorna ovalor senão retorna
        return self._x or 0

    @x.setter
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value

    @x.deleter
    def x(self):
        self._x = -1


foo = Foo(10)
print(foo.x)
foo.x = 10
del foo.x
print(foo.x)
