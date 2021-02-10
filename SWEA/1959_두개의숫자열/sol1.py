import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))


    maximum = 0

    if N < M:
        for add in range(M - N + 1):
            total = 0
            for idx in range(N):
                total += A[idx] * B[idx+add]
            if total > maximum:
                maximum = total
    else:
        for add in range(N - M + 1):
            total = 0
            for idx in range(M):
                total += B[idx] * A[idx + add]
            if total > maximum:
                maximum = total

    print('#{} {}'.format(tc, maximum))