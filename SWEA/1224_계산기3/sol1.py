import sys
sys.stdin = open('input.txt')

def solution(cal):
    signs = {'+': 1, '-': 1, '*': 2, '/': 2, ')': 0, '(': 0}
    sign_stack = [] # 연산자가 머무르는 스택
    stack = [] # 계산식 스택

    for elem in cal:
        # 연산자일때
        if elem in signs.keys():
            # 스택이 비어있을때
            if not sign_stack:
                sign_stack.append(elem)
            # 여는 괄호일때
            elif elem == '(':
                sign_stack.append(elem)
            # 닫는 괄호일때
            elif elem == ')':
                while sign_stack[-1] != '(':
                    stack.append(sign_stack.pop())
                sign_stack.pop()
            # 이전 연산자보다 순서가 더 클때
            elif signs[sign_stack[-1]] < signs[elem]:
                sign_stack.append(elem)
            # 이전 연산자보다 순서가 더 크지 않을때
            else:
                while sign_stack and signs[sign_stack[-1]] >= signs[elem]:
                    stack.append(sign_stack.pop())
                sign_stack.append(elem)
        # 숫자일때
        else:
            stack.append(elem)

    cal_stack = [] # 실제 계산용 스택
    # stack 계산하기
    for elem in stack:
        if elem in signs.keys():
            if elem == '+':
                cal_stack[-2] = int(cal_stack[-2]) + int(cal_stack[-1])
                cal_stack.pop()
            elif elem == '-':
                cal_stack[-2] = int(cal_stack[-2]) - int(cal_stack[-1])
                cal_stack.pop()
            elif elem == '*':
                cal_stack[-2] = int(cal_stack[-2]) * int(cal_stack[-1])
                cal_stack.pop()
            elif elem == '/':
                cal_stack[-2] = int(cal_stack[-2]) // int(cal_stack[-1])
                cal_stack.pop()
        else:
            cal_stack.append(elem)

    return cal_stack.pop()

T = 10

for tc in range(1, T+1):
    length = int(input())
    cal = input()

    print('#{} {}'.format(tc, solution(cal)))