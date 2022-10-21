"""
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __str__(self):
        return "이름   %s, 나이   %d" % (self.name, self.age)


kim = Human(23, "백길이")
# 객체   kim을   print -> __str__ 메소드가   호출됨
print(kim)
"""


class School:
    def __init__(self, school, dept, grade):
        self.school = school
        self.dept = dept
        self.grade = grade

    def __str__(self):
        return "제 학교는 %s, 과는 %s, 학년은 %d 입니다." % (self.school,self.dept,self.grade)
oh = School('명지대','컴퓨터공학과',4)
print(oh)
