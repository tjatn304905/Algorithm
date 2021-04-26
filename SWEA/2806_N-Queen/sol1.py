import sys
sys.stdin = open('sample_input.txt')


def solution(idx, board):
    global count

    # 종료조건
    if idx == N:
        count += 1
        return

    for i in range(N):
        put_queen = True  # 퀸을 놓을 수 있는지 여부

        # 가지치기를 위한 코드
        for j in range(N):
            # 세로 확인
            if board[j][i]:
                put_queen = False
                break
            # 대각선 확인
            if i + abs(idx-j) < N and board[j][i + abs(idx-j)]:
                put_queen = False
                break
            if 0 <= i - abs(idx-j) and board[j][i - abs(idx-j)]:
                put_queen = False
                break

        if put_queen:
            board[idx][i] = 1  # 퀸을 놓음
            solution(idx+1, board)  # 다음줄에 퀸을 놓음
            board[idx][i] = 0  # 원상복구


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    board = [[0] * N for _ in range(N)]  # 체스판

    count = 0  # 가능한 경우의 수

    solution(0, board)

    print('#{} {}'.format(tc, count))