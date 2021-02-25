import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 출발방, 도착방의 인덱스
    from_to = []
    for n in range(N):
        fr, to = map(int, input().split())
        from_to.append([(fr - 1) // 2, (to - 1) // 2])

    # 동선을 1로 표시
    route = [0] * 200
    for i in range(len(from_to)):
        if from_to[i][0] < from_to[i][1]:
            for j in range(from_to[i][0], from_to[i][1] + 1):
                route[j] += 1
        else:
            for j in range(from_to[i][1], from_to[i][0] + 1):
                route[j] += 1

    # 동선의 최대값을 출력
    mx = 0
    for r in route:
        if r > mx:
            mx = r

    print('#{} {}'.format(tc, mx))




