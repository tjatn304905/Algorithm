str1 = 'ABCD'

str2 = "ABCD"

print(str1)
print(str2)


str1 = '''asdfsdafasdf
asdfasdfasdf
'''

print(str1)


str1 = '안녕'
str2 = '하세요'
N = 1

print(str1 + str2 + str(N))

str3 = "-"*20
str4 = "--------------------"
print(str3)
print(str4)

arr = [1,2,3]

print(arr[1])
arr[1] = 4
print(arr)

# str1 = '123'
#
# print(str[1])
# str[1] = 4

line = '안녕하세요'

print(line.replace('세', '시'))
print(line)
line = line.replace('세', '시')
print(line)
print(line.split('하'))

# 비밀번호 영어숫자를 조합해서 작성해야 한다.
password = 'abcde'

flag_alpha = False
flag_number = False

for i in password:
    if i.isalpha():
        flag_alpha = True

    if i.isalpha():
        flag_number = True

if not flag_alpha:
    print('비밀번호에 알파벳이 사용되지 않았음')
elif not flag_number:
    print('비밀번호에 숫자가 사용되지 않았음')
else:
    print('완벽한 비밀번호이다.')

line2 = '안녕하시녕요'
# print(line2.find('녕'))
print(line2.find('ㄹ'))
print(line2.index('녕'))
# print(line2.index('ㄹ'))