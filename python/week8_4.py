class Person:
    def greeting(self):
        print('안녕하세요.', end='')


class Student(Person):
    def greeting(self):
        super().greeting()
        print(' 반갑습니다.')



kim = Student()
kim.greeting()
