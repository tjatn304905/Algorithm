import sys
sys.stdin = open('input.txt')


def check(N, M):
    # 2진수 숫자들을 담을 길이 30의 리스트
    two_bit = [0] * 30

    for i in range(1, 31):
        if M >= 2**(30-i):
            two_bit[i-1] = 1
            M -= 2**(30-i)
            if M == 0:
                break

    for elem in two_bit[30-N:30]:
        if elem == 0:
            return 'OFF'
    return 'ON'


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    print('#{} {}'.format(tc, check(N, M)))


