class school:
    def __init__(self):
        print('school')

    def __call__(self):
        print('__call__() 호출하였음!!')

b=school()
b()