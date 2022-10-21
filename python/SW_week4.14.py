a = sum([1,2,3,4])
b = sum([1,2,3,4], 5)
print(a,b)

s = "a = a + 100"
a = 100
exec(s)
print(a)

k = ['abc', 'bc', 'a']
print(sorted(k))
print(sorted(k, reverse=True))

s = "IwantotoknowPython "
print(ord(s[0]))
a = list(map(ord, s))
print(a)
aa = list(map(chr, a))
print(aa) # 대문자로 변환