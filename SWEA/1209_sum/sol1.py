import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    number = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    total_list = []
    for i in range(100):
        row_total = 0
        col_total = 0
        for j in range(100):
           row_total += matrix[i][j]
           col_total += matrix[j][i]
        total_list += [row_total, col_total]

    dia1_total = 0
    dia2_total = 0
    for i in range(100):
        dia1_total += matrix[i][i]
        dia2_total += matrix[99-i][i]
    total_list += [dia1_total, dia2_total]

    maximum = 0
    for idx in range(len(total_list)):
        if maximum <= total_list[idx]:
            maximum = total_list[idx]

    print('#{} {}'.format(tc, maximum))