"""
str = "89점"
try :
    score = int(str)
except ValueError : # ValueError 예외 발생 시 수행
    print("점수의 형식이 잘못됨")
except IndexError : # IndexError 예외 발생시 수행
    print("첨자가 범위를 벗어남")
else :
    print(score)
"""
"""
def calsum(n) :
    if (n < 0) :
        raise ValueError # 예외 이름 없이 raise 만 사용해도 됨
    sum = 0
    for a in range(n+1) :
      sum += a
    return sum
try :
    print(calsum(10))
    print(calsum(-5))
except :
    print("입력값이 잘못됨")
"""
"""
text = input()
if text.isdigit() == False :
    try :
        raise Exception("입력 문자열이 숫자가 아닙니다.")
    except Exception :
        print("예외가 일어났습니다.")
"""
"""
str = "89점"
try :
    score = int(str)
except ValueError as e :
    print(e)
else :
    print(score)
finally :
    print("무조건 수행합니다")
"""

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
     print("division by zero!")
    else:
     print("result is", result)
    finally:
     print("executing finally clause")
divide(2,1)
divide(2,0)
divide("2","1")

