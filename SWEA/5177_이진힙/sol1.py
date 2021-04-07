import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    values = list(map(int, input().split()))

    # 인덱스에 값을 담는 리스트
    pa = [0] * (N+1)

    # 값 넣어주기
    for i in range(1, N+1):
        pa[i] = values[i-1]
        # 부모랑 계속해서 비교하기
        cur_1 = i
        while cur_1 > 0:
            if pa[cur_1//2] > pa[cur_1]:
                pa[cur_1//2], pa[cur_1] = pa[cur_1], pa[cur_1//2]
                cur_1 = cur_1//2
            else:
                break

    cur_2 = N // 2
    result = 0
    while cur_2 > 0:
        result += pa[cur_2]
        cur_2 = cur_2 // 2

    print('#{} {}'.format(tc, result))
