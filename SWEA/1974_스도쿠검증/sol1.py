import sys
sys.stdin = open('input.txt')

def solution(sudoku):
    for i in range(9):
        test_row = []
        test_col = []
        for j in range(9):
            if sudoku[i][j] in test_row:
                return 0
            if sudoku[j][i] in test_col:
                return 0
            test_row.append(sudoku[i][j])
            test_col.append(sudoku[j][i])
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            test_box = []
            for ii in range(2):
                for jj in range(2):
                    if sudoku[i+ii][j+jj] in test_box:
                        return 0
                    test_box.append(sudoku[i+ii][j+jj])

    return 1

T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]


    print('#{} {}'.format(tc, solution(sudoku)))