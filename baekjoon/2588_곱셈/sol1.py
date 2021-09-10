# https://www.acmicpc.net/problem/2588

# 세자리 숫자 두개를 입력한다
num1 = int(input())
num2 = int(input())
# 여기서도 습관적으로 map을 이용하려 했는데, map은 iterable한 객체에 사용된다.

# num2의 각 자리 숫자를 리스트 요소로 변환
numbers = []
numbers.extend(f'{num2}')
# 리스트 거꾸로 뒤집기
numbers.reverse()

# numbers 리스트를 순회하면서 num1와 곱한값 출력
total = 0
exponent = 0
for number in numbers:
    multiply = num1 * int(number)
    # total에 10의 지수를 늘려가며 더하기
    total += multiply * 10**exponent
    exponent += 1
    print(multiply)

# total 출력
print(total)