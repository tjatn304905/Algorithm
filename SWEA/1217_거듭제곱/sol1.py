import sys
sys.stdin = open('input.txt')

def solution(N, M):
    if M == 0:
        return 1

    return N * solution(N, M-1)


T = 10

for _ in range(1, 1+T):
    tc = int(input())
    N, M = map(int, input().split())

    print('#{} {}'.format(tc, solution(N, M)))