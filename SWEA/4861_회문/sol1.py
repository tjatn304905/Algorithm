import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    for n1 in range(N):
        for n2 in range(N):
            # 가로
            if n2+M-1 < N and matrix[n1][n2] == matrix[n1][n2+M-1]:
                for i in range(1, M//2):
                    if matrix[n1][n2+i] != matrix[n1][n2+M-1-i]:
                        break
                else:
                    result = ''
                    for r in range(n2, n2+M):
                        result += matrix[n1][r]
            # 세로
            if n1+M-1 < N and matrix[n1][n2] == matrix[n1+M-1][n2]:
                for i in range(1, M//2):
                    if matrix[n1+i][n2] != matrix[n1+M-1-i][n2]:
                        break
                else:
                    result = ''
                    for r in range(n1, n1 + M):
                        result += matrix[r][n2]

    print('#{} {}'.format(tc, result))