import sys
sys.stdin = open('sample_input.txt')


def solution(matrix):
    # matrix의 [0][0] 에서 시작하여 [N-1][N-1]까지 도달하면 된다.
    # X좌표 또는 Y좌표 둘 중 하나를 1씩 더해가면 된다.
    # X축으로 (N-1)회, Y축으로 (N-1)회, 총 2 * (N-1)회 움직이게 된다.

    # X축 이동을 나타내는 리스트
    move = [1] * (N-1) + [0] * (N-1)

    # 이 리스트의 순열을 구하기
    perm(move, 0, len(move))


def perm(move, idx, length):
    global minimum
    if idx == length:
        print(move)
        # 리스트의 숫자가 1이면 X축으로, 0이면 Y축으로 이동하며 값을 더함
        x = 0
        y = 0
        result = matrix[x][y]
        for elem in move:
            if elem:
                x += 1
                result += matrix[x][y]
            else:
                y += 1
                result += matrix[x][y]
        if result < minimum:
            minimum = result
    else:
        for changer in range(idx, length):
            move[idx], move[changer] = move[changer], move[idx]
            perm(move, idx+1, length)
            move[idx], move[changer] = move[changer], move[idx]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    minimum = 99999

    solution(matrix)

    print(minimum)