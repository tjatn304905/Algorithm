import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    trucks = [list(map(int, input().split())) for _ in range(N)]

    # 현재시각
    current = 0

    count = 0

    # 현재시각 이상이면서 가장 빨리 끝나는 화물차 지정
    while True:
        minimum = 25
        for truck in trucks:
            if current <= truck[0] and truck[1] < minimum:
                minimum = truck[1]
        # 그 화물차의 종료시각을 현재시각으로 설정
        current = minimum

        # minimum이 바뀌지 않았을 경우 종료
        if minimum == 25:
            break

        count += 1

    print('#{} {}'.format(tc, count))