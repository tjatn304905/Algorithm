import sys
sys.stdin = open('sample_input.txt')

def solution(x, y, matrix):
    stack = [[x, y, 0]]
    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]

    while stack:
        x, y, cnt = stack.pop(0)
        for idx in range(4):
            dx, dy = dxs[idx], dys[idx]
            if 0 <= x + dx < N and 0 <= y + dy < N and matrix[y+dy][x+dx] != 1:
                if matrix[y + dy][x + dx] == 3:
                    return cnt
                stack.append([x + dx, y + dy, cnt + 1])
                matrix[y + dy][x + dx] = 1
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 2:
                start = [x, y]

    print('#{} {}'.format(tc, solution(*start, matrix)))