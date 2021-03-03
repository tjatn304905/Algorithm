import sys
from pandas import DataFrame
sys.stdin = open('sample_input.txt')

def dfs(x, y):
    global found
    # nonlocal found # nonglobal 이라는 뜻도 포함
    visited[y][x] = True
    # matrix[y][x] = 'V'
    # print(DataFrame(matrix))
    if matrix[y][x] == 3:
        found = 1
    else:
        dys = [-1, 1, 0 ,0]
        dxs = [0, 0, -1, 1]
        for idx in range(4):
            dy, dx = dys[idx], dxs[idx]
            # 1. 이동하려는 좌표값이 0 <= x, y < N을 만족하는가
            if 0 <= x + dx < N and 0 <= y + dy < N:
                # 2. 벽이 아닌가(길, 목적지, 출발지)
                if matrix[y + dy][x + dx] != 1:
                    # 3. 방문했는지..?
                    if not visited[y + dy][x + dx]:
                        dfs(x + dx, y + dy)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 2:
                start = (x, y)
            elif matrix[y][x] == 3:
                goal = (x, y)

    visited = [[False for _ in range(N)] for _ in range(N)]
    found = 0

    dfs(*start)

    print('#{} {}'.format(tc, found))