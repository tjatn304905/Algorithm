import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix += [list(map(int, input().split()))]

    count = 0

    # row
    for i in range(N):
        for j in range(N-K+1):
            for k in range(K):
                if matrix[i][j+k] == 0:
                    break
            else:
                if j > 0:
                    if matrix[i][j-1]:
                        continue
                if j+k < N-1:
                    if matrix[i][j+k+1]:
                        continue
                count += 1

    # column
    for j in range(N):
        for i in range(N-K+1):
            for k in range(K):
                if matrix[i+k][j] == 0:
                    break
            else:
                if i > 0:
                    if matrix[i-1][j]:
                        continue
                if i+k < N-1:
                    if matrix[i+k+1][j]:
                        continue
                count += 1

    print('#{} {}'.format(tc, count))




