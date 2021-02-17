import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix += [list(map(int, input().split()))]

    total = 0
    maximum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            for m1 in range(M):
                for m2 in range(M):
                    total += matrix[i+m1][j+m2]
            if maximum < total:
                maximum = total
            total = 0
    print('#{} {}'.format(tc, maximum))
