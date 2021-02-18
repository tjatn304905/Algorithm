import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    tc = input()

    matrix = [list(input()) for _ in range(100)]
    length_list = []

    # 가로
    for i in range(100):
        # 길이가 홀수
        for j in range(1, 99):
            idx = 1
            while j-idx >= 0 and j+idx < 100 and matrix[i][j-idx] == matrix[i][j+idx]:
                idx += 1
            length_list.append(idx * 2 - 1)
        # 길이가 짝수
        for j in range(99):
            if matrix[i][j] == matrix[i][j+1]:
                idx = 1
                while j-idx >= 0 and j+1+idx < 100 and matrix[i][j-idx] == matrix[i][j+1+idx]:
                    idx += 1
                length_list.append(idx * 2)
    # 세로
    for j in range(100):
        # 길이가 홀수
        for i in range(1, 99):
            idx = 1
            while i-idx >= 0 and i+idx < 100 and matrix[i-idx][j] == matrix[i+idx][j]:
                idx += 1
            length_list.append(idx * 2 - 1)
        # 길이가 짝수
        for i in range(99):
            if matrix[i][j] == matrix[i+1][j]:
                idx = 1
                while i-idx >= 0 and i+1+idx < 100 and matrix[i-idx][j] == matrix[i+1+idx][j]:
                    idx += 1
                length_list.append(idx * 2)

    print('#{} {}'.format(tc, max(length_list)))

