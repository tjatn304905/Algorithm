import sys
sys.stdin = open('sample_input.txt')


def solution(matrix, x, y):

    global result, results

    dx = [1, 0]
    dy = [0, 1]

    result += matrix[x][y]

    if x == y == N-1:
        results.append(result)
        print(results)
        return result


    for i in range(2):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
            x = x + dx[i]
            y = y + dy[i]

            # 가는 길마다 더해주고


            solution(matrix, x, y)

            # 원상복귀
            result -= matrix[x][y]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = matrix[0][0]
    results = []

    solution(matrix, 0, 0)

    print(min(results))