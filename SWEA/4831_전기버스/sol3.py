import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))
    ans = 0 # 충전 회수

    # 아래와 같은 코드
    charge = [0] + charge + [N]
    # charge.insert(0, 0)
    # charge.append(N)

    last = 0

    # 충전소에 출발점과 도착지를 넣어놓았으므로
    for i in range(1, M+2):
        if charge[i] - charge[i-1] > K:
            ans = 0
            break

        # 갈 수 있으면 아무작업 x
        # 갈 수 없다면 내 바로직전 충전소로 위치를 옮기고 횟수 1회 증가
        if charge[i] > last + K:
            last = charge[i-1]
            ans += 1


    print("#{} {}".format(tc, ans))