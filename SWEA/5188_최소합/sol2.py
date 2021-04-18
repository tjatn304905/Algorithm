import sys
sys.stdin = open('sample_input.txt')

dx = [1, 0]
dy = [0, 1]


def solution(x, y):

    global result, minimum

    # 가는 길마다 더해주고
    result += matrix[x][y]

    if x == y == N-1:
        if minimum > result:
            minimum = result
        return

    # 가능성이 없는 애들은 가지치기
    if result >= minimum:
        return

    for i in range(2):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:

            solution(x + dx[i], y + dy[i])

            # 원상복귀
            result -= matrix[x + dx[i]][y + dy[i]]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    minimum = 100000
    result = 0

    solution(0, 0)

    print('#{} {}'.format(tc, minimum))