txt1 = 'aAbBcCdDeEfFgGhH'
print(txt1[0::2]) #홀수번째 문자만 출력  :: 두개있는 이유는 [시작인덱스:끝:스텝] 구조인데 가운데를 비우면 자동 끝 인덱스로 지정되서 가운데가 빈 것 뿐이다.
print(txt1[::-1]) # txt1 거꾸로 출력

reverseTxt1 = ''
for c in txt1: # txt1 거꾸로 출력
    reverseTxt1 = c+reverseTxt1
print(reverseTxt1)

str = "a:b:c:d"
print(str.replace(":","#"))  # :을 #으로 대체

list = [1,3,5,4,2]
list.sort(reverse=True) # list를 내림차순으로 정렬
print(list)

list = ['Life','is','too','short']
str = ' '.join(list) # list를 문자열로 변환!
print(str)

