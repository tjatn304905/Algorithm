import sys
sys.stdin = open('sample_input.txt')

def solution(forth):
    stack = []

    for elem in forth:
        # 부호일때
        if elem == '+' or elem == '-' or elem == '*' or elem == '/':
            # 부호가 나왔는데 스택이 두개보다 적을때는 에러
            if len(stack) < 2:
                return 'error'
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if elem == '+':
                    stack.append(b + a)
                elif elem == '-':
                    stack.append(b - a)
                elif elem == '*':
                    stack.append(b * a)
                elif elem == '/':
                    stack.append(b // a)
        # '.'일때
        elif elem == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'
        # 숫자일때
        else:
            stack.append(elem)


T = int(input())

for tc in range(1, T+1):
    forth = list(input().split())

    print('#{} {}'.format(tc, solution(forth)))
