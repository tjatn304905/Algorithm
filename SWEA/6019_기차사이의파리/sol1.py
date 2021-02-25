import sys
sys.stdin = open('s_input.txt')

def solution(D, A, B, F):

    total = 0

    for _ in range(100):
        t = D / (F + B)
        total += F * t
        D -= (A+B) * t

        t = D / (F + A)
        total += F * t
        D -= (A+B) * t

    return total


T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())

    print('#{} {}'.format(tc, solution(D, A, B, F)))