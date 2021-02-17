import sys
# from pandas import DataFrame
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    tc = int(input())
    matrix = [
        list(map(int, input().split())) for _ in range(100)
    ]

    # print(DataFrame(matrix))

    # 목표지점 찾기
    for idx in range(100):
        if matrix[99][idx] == 2:
            row = idx
            break

    # col이 0이 될때까지
    col = 99
    while col:
        if row == 0:
            if matrix[col][row+1]:
                while True:
                    if row < 99 and matrix[col][row+1]:
                        row += 1
                    else:
                        col -= 1
                        continue
                col -= 1
            else:
                col -= 1
        elif row == 99:
            if matrix[col][row-1]:
                while True:
                    if row > 0 and matrix[col][row-1]:
                        row -= 1
                    else:
                        col -= 1
                        continue
            else:
                col -= 1
        else:
            if matrix[col][row+1]:
                while True:
                    if row < 99 and matrix[col][row+1]:
                        row += 1
                    else:
                        col -= 1
                        continue
            elif matrix[col][row-1]:
                while True:
                    if row > 0 and matrix[col][row-1]:
                        row -= 1
                    else:
                        col -= 1
                        continue
            else:
                col -= 1

    print(row)