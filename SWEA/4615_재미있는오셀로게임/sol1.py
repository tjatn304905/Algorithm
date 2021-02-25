import sys
sys.stdin = open('sample_input(1).txt')

def solution(N, turns):
    # 1: 흑 2: 백 N: 판 크기 M: 턴 횟수
    # 보드
    matrix = [[0] * N for _ in range(N)]
    # 기본 말
    matrix[N // 2][N // 2 - 1] = matrix[N // 2 - 1][N // 2] = 1
    matrix[N // 2 - 1][N // 2 - 1] = matrix[N // 2][N // 2] = 2

    for turn in turns:
        i, j, color = turn[1]-1, turn[0]-1, turn[2]

        # 가로축
        idx = 1
        while 0 <= j + idx < N and matrix[i][j+idx]:
            if matrix[i][j+idx] == color:
                for k in range(idx):
                    matrix[i][j+k] = color
                break
            idx += 1
        idx = 1
        while 0 <= j - idx < N and matrix[i][j-idx]:
            if matrix[i][j-idx] == color:
                for k in range(idx):
                    matrix[i][j-k] = color
                break
            idx += 1

        # 세로축
        idx = 1
        while 0 <= i + idx < N and matrix[i+idx][j]:
            if matrix[i+idx][j] == color:
                for k in range(idx):
                    matrix[i+k][j] = color
                break
            idx += 1
        idx = 1
        while 0 <= i - idx < N and matrix[i-idx][j]:
            if matrix[i-idx][j] == color:
                for k in range(idx):
                    matrix[i-k][j] = color
                break
            idx += 1

        # 대각선
        idx = 1
        while 0 <= i-idx < N and 0 <= j-idx < N and matrix[i-idx][j-idx]:
            if matrix[i-idx][j-idx] == color:
                for k in range(idx):
                    matrix[i - k][j - k] = color
                break
            idx += 1
        idx = 1
        while 0 <= i + idx < N and 0 <= j - idx < N and matrix[i + idx][j - idx]:
            if matrix[i + idx][j - idx] == color:
                for k in range(idx):
                    matrix[i + k][j - k] = color
                break
            idx += 1
        idx = 1
        while 0 <= i - idx < N and 0 <= j + idx < N and matrix[i - idx][j + idx]:
            if matrix[i - idx][j + idx] == color:
                for k in range(idx):
                    matrix[i - k][j + k] = color
                break
            idx += 1
        idx = 1
        while 0 <= i + idx < N and 0 <= j + idx < N and matrix[i + idx][j + idx]:
            if matrix[i + idx][j + idx] == color:
                for k in range(idx):
                    matrix[i + k][j + k] = color
                break
            idx += 1

    black = white = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                black += 1
            if matrix[i][j] == 2:
                white += 1

    return black, white


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    turns = [list(map(int, input().split())) for _ in range(M)]

    print('#{} {} {}'.format(tc, *solution(N, turns)))