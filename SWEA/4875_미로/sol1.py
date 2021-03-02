import sys
sys.stdin = open('sample_input.txt')

def solution(matrix):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [['1' for _ in range(N+2)]] + [['1'] + list(input()) + ['1'] for _ in range(N)] + [['1' for _ in range(N+2)]]

    print(matrix)

    print('#{} {}'.format(tc, solution(matrix)))