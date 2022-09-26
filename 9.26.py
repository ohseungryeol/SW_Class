import a as a


def same_number(m,n):

    str1 = str(m)
    str2 = str(n)
    list1=[]
    list2=[]
    for i in str1:
        list1.append(i)

    for i in str2:
        list2.append(i)

    same_num =list(set(list1) & set(list2))
    print(same_num)



num1= int(input())
num2= int(input())

same_number(num1,num2)