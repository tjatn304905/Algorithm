import sys
sys.stdin = open('sample_input.txt')


def solution(x, y):
    global route
    route += matrix[x][y]

    if len(route) == 7:
        routes.add(route)
        return

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        if 0 <= x+dx[i] < 4 and 0 <= y+dy[i] < 4:
            solution(x+dx[i], y+dy[i])
            # 원상복귀
            route = route[:-1]


T = int(input())

for tc in range(1, T+1):
    matrix = [list(input().split()) for _ in range(4)]
    routes = set()
    route = ''

    for i in range(4):
        for j in range(4):
            route = ''
            solution(i, j)

    print('#{} {}'.format(tc, len(routes)))
