import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 10 x 10 매트릭스 만들기
    matrix = [[0] * 10 for _ in range(10)]
    # 사각형마다 색칠하기
    for n in range(N):
        row_1, col_1, row_2, col_2, color = map(int, input().split())
        count = 0
        for i in range(row_1, row_2 + 1):
            for j in range(col_1, col_2 + 1):
                matrix[i][j] += color

        for i in range(10):
            for j in range(10):
                if matrix[i][j] == 3:
                    count += 1

    print('#{} {}'.format(tc, count))
    
