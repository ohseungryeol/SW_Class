import self as self

"""
class Player:
    def __init__(self, name, height, weight) :
     self.number = 100
     self.name = name
     self.height = height
     self.weight = weight
    def print_info(self) :
     print(self.number)
     print(self.name)
     print(self.height)
     print(self.weight)

a = Player("gildong", 178,75)
a.print_info()
"""
"""
class TestPrivate :
    def __init__(self) :
      self.a = 100
      self.__b = 200
      self.__num =300
    def print_member(self) :
      print(self.a)
      print(self.__b)
      print(self.__num)

obj = TestPrivate()
obj.print_member()

#print(obj.a)
#print(obj.__b) 접근 불가 (Private이므로)
"""
"""
class MyClass :
    var = "안녕하세요!!" # 클래스 메소드 밖 멤버 (객체 생성과 무관하게 접근가능)


    def sayHello(self) : #self 는 obj객체
        msg1 ="안녕"
        self.msg2 = "Hi"
        print(msg1)
        print(self.var) # 객체의 var를 새로 정의하여 사용
        self.var = "Hello World"

obj = MyClass()
obj.sayHello()
print(obj.var)
print(MyClass.var)
"""
"""
class CalCounter :
    count = 0 # 클래스   멤버
    def __init__(self) :
        CalCounter.count += 1      # 클래스   멤버인   count의   값을   접근
    def print_count(self) :
        print(self.count)
a = CalCounter() #init 으로 초기화 count=1
a.print_count() # 1출력
b = CalCounter() # init 으로 초기화 count = 2
b.print_count()
"""
"""
class CalCounter :
    count = 0
    def __init__(self) : self.count += 1
    def print_count(self) : print(self.count)
a = CalCounter()
a.print_count()
b = CalCounter()
b.print_count()

"""
"""
class Human :
    def __init__(self, age, name) :
        self.age = age
        self.name = name
    def __eq__(self, other) : # 연산자 메소드 eq를 정의 (==를 통해 호출한다.)
        return self.age == other.age and self.name == other.name
kim = Human(29, "홍길동")
sang = Human(29, "홍길동")
moon = Human(30, "이순신")
print(kim==sang)
print(kim==moon)
"""

# 연습문제 p.17 1번
"""
class Human :
    def __init__(self, age, name) :
        self.age = age
        self.name = name
    def __eq__(self, other) : # 연산자 메소드 eq를 정의 (==를 통해 호출한다.)
        return self.name == other.name
    def __le__(self,other) :
        return self.age == other.age
kim = Human(29, "홍길동")
sang = Human(29, "홍길동")
moon = Human(30, "이순신")
print(kim==sang)
print(kim==moon)
"""
# 연습문제 17-2번
class Human :
    def __init__(self, age, name) :
        self.age = age
        self.name = name
    def __eq__(self, other) : # 연산자 메소드 eq를 정의 (==를 통해 호출한다.)
        return self.name == other.name
    def __le__(self,other) :
        return self.age <= other.age
    def __radd__(self,num) :
        return self.age+num
kim = Human(29, "홍길동")
sang = Human(29, "홍길동")
moon = Human(30, "이순신")
print(1+kim)


