class Outer():
    some_var = None
    def __init__(self, some):
        Outer.some_var = some

    class Inner:
        def func(self):
            print Outer.some_var
