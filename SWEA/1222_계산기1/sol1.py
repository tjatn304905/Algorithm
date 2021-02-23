import sys
sys.stdin = open('input.txt')

def solution(length, string):
    sign = [] # 부호 스택
    number = [] # 숫자 스택

    for i in range(length):
        if string[i] == '+':
            sign.append(string[i])
        else:
            number.append(int(string[i]))

    for i in range(len(sign)-1, -1, -1):
        # 뒤에서부터 부호를 꺼내면서
        if sign.pop() == '+':
            # 맨 뒤 숫자 꺼내서 그 이전 숫자에 더해주기
            number[i] += number.pop()

    return number[0]

T = 10

for tc in range(1, T+1):
    length = int(input())
    string = input()

    print('#{} {}'.format(tc, solution(length, string)))