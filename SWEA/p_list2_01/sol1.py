import sys
sys.stdin = open("input.txt", encoding='utf8')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    d_col = [-1, 1, 0, 0]
    d_row = [0, 0, -1, 1]
    sum_sum = 0

    # 가장자리 미포함
    for col in range(1, N-1):
        for row in range(1, N-1):
            abs_sum = 0
            for d in range(4):
                center = matrix[col][row]
                test_col = col + d_col[d]
                test_row = row + d_row[d]
                around = matrix[test_col][test_row]
                abs_sum += abs(center - around)
            sum_sum += abs_sum

    print("#{} {}".format(tc, sum_sum))
