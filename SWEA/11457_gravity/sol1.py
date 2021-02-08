import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    NT = int(input())
    g_list = list(map(int, input().split()))

    result = 0
    # 중력에 의해 가장 많이 떨어지는 부분은 오른쪽에 있는 수들 중에서 자기보다 작은 수의 개수이다
    for idx1 in range(len(g_list)):
        count = 0
        for idx2 in range(idx1+1, len(g_list)):
            if g_list[idx1] > g_list[idx2]:
                count += 1
        # 그 중에서 최대값을 sort한다.
        if result < count:
            result = count

    print('#{} {}'.format(tc, result))

