import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]

    count = 0

    for i in range(N):
        count += 1
        matrix[0][i] = count

    col = 0
    row = N-1
    N -= 1

    while N != 0:
        if (len(matrix) - N) % 2:
            for i in range(N):
                count += 1
                col += 1
                matrix[col][row] = count
            for i in range(N):
                count += 1
                row -= 1
                matrix[col][row] = count
        else:
            for i in range(N):
                count += 1
                col -= 1
                matrix[col][row] = count
            for i in range(N):
                count += 1
                row += 1
                matrix[col][row] = count
        N -= 1

    print('#{}'.format(tc))
    for i in range(len(matrix)):
        print(' '.join(map(str,matrix[i])))