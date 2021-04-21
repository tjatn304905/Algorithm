import sys
sys.stdin = open('sample_input.txt')


def charge(idx, count):
    global minimum_count

    bus_stop = [] # 현재 갈 수 있는 정류장

    for i in range(1, chargers[idx]+1):
        if idx + i <= N:
            bus_stop.append(idx + i)

    # 첫번째 충전이 아니면 횟수에 1 더하기
    if idx != 1:
        count += 1

    # N번 정류장에 도착할 수 있다면 종료
    if bus_stop[-1] == N:
        if minimum_count > count:
            minimum_count = count
        return

    # 갈 수 있는 정류장에서 다시 출발(완전탐색)
    for stop in bus_stop:
        # count가 최소환승횟수보다 작을때만 실행(pruning)
        if count < minimum_count:
            charge(stop, count)


T = int(input())

for tc in range(1, T+1):
    chargers = list(map(int, input().split())) # N과 충전기

    N = chargers[0] # 정류장 개수

    minimum_count = 100 # 최소 충전 횟수

    charge(1, 0)

    print('#{} {}'.format(tc, minimum_count))