import sys
sys.stdin = open('sample_input(1).txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    turns = [tuple(map(int, input().split())) for _ in range(M)]

    board = [[0] * (N + 2) for _ in range(N + 2)]
    board[N // 2 + 1][N // 2] = board[N // 2][N // 2 + 1] = 1
    board[N // 2][N // 2] = board[N // 2 + 1][N // 2 + 1] = 2

    di = [0, -1, -1, -1, 0, 1, 1, 1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    for turn in turns:
        board[turn[0]][turn[1]] = turn[2]
        for idx in range(8):
            itr = 1
            stones = []
            while board[turn[0] + di[idx] * itr][turn[1] + dj[idx] * itr] == (abs(turn[2] - 2) + 1):
                stones.append((turn[0] + di[idx] * itr, turn[1] + dj[idx] * itr))
                itr += 1
            if board[turn[0] + di[idx] * itr][turn[1] + dj[idx] * itr] == turn[2]:
                for stone in stones:
                    board[stone[0]][stone[1]] = turn[2]

    black = 0
    white = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))