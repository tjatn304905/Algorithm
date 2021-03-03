import sys
sys.stdin = open('input.txt')

def solution(password):
    i = 0
    while True:
        if password[0] - (i % 5 + 1) > 0:
            password.append(password.pop(0) - (i % 5 + 1))
        else:
            password.pop(0)
            password.append(0)
            return password
        i += 1

T = 10

for tc in range(1, T+1):
    tc = int(input())
    password = list(map(int, input().split()))

    print('#{} {} {} {} {} {} {} {} {}'.format(tc, *solution(password)))