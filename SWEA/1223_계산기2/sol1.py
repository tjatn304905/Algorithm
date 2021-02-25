import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    length = int(input())
    numbers = input()
    order = {'+': 1, '*': 2}
    sign_stack = []
    stack = []

    for number in numbers:
        # 부호일때
        if number in order.keys():
            if not sign_stack:
                sign_stack.append(number)
            # 자신의 우선순위가 높으면 push
            elif order[number] > order[sign_stack[-1]]:
                sign_stack.append(number)
            # 그렇지 않으면 자신의 우선순위가 높을때까지 pop
            else:
                while sign_stack and order[number] <= order[sign_stack[-1]]:
                    stack.append(sign_stack.pop())
                sign_stack.append(number)
        # 숫자일때
        else:
            stack.append(int(number))
    # 부호 스택에 남아있는거 모두 pop
    while sign_stack:
        stack.append(sign_stack.pop())

    while len(stack) > 1:
        for i in range(len(stack)):
            if stack[i] == '+':
                stack[i - 2] = stack[i - 2] + stack[i - 1]
                stack.pop(i)
                stack.pop(i-1)
                break
            elif stack[i] == '*':
                stack[i-2] = stack[i-2] * stack[i-1]
                stack.pop(i)
                stack.pop(i-1)
                break
    print('#{} {}'.format(tc, *stack))


