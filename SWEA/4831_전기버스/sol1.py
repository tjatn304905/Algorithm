import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    stops = list(map(int, input().split()))

    # 충전기가 있는 곳을 리스트로 만듦
    chargers = [0]*(N+1)
    for stop in stops:
        chargers[stop] = 1
    # print(chargers)

    # 출발점에서 K를 더한 다음 거꾸로 오면서 가장 가까운 충전기를 찾음
    start = 0
    count = 0
    while start+K < N:
        for idx in range(start+K, start, -1):
            if chargers[idx]:
                start = idx
                count += 1
                break
        # 위의 조건에 걸리지 않을 때를 대비해 for else 활용
        else:
            count = 0
            break

    print('#{} {}'.format(tc, count))