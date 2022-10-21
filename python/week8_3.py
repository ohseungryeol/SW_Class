class BaseA:
    def __init__(self):
        print('BaseA.__init__()')


class B(BaseA):
    def __init__(self):
        print('B.__init__()')
        super().__init__()

b=B()