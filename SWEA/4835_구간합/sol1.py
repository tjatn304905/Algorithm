import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))
    
    # 최대값, 최소값 초기화
    maximum = 0
    minimum = 0
    for idx in range(M):
        minimum += numbers[idx]
    # 더할 구간의 범위 지정하기
    for idx in range(len(numbers)-M+1):
        total = 0
        # 구간합 구하기
        for i in range(idx, idx+M):
            total += numbers[i]

        if total > maximum:
            maximum = total
        if total < minimum:
            minimum = total

    result = maximum - minimum

    print('#{} {}'.format(tc, result))