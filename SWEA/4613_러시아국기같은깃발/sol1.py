import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = []
    for _ in range(N):
        flag.append(list(input()))

    # 조합 만들기(각 색깔의 끝 지점을 표시)
    com = []
    for w in range(1, N - 1):
        for b in range(w + 1, N):
            for r in range(b + 1, N + 1):
                if r == N:
                    com.append([w, b, r])

    minimum = 2500

    # 색칠하기
    for c in com:
        cnt = 0
        for row in range(c[0]):
            for i in range(M):
                if flag[row][i] != 'W':
                    cnt += 1
        for row in range(c[0], c[1]):
            for i in range(M):
                if flag[row][i] != 'B':
                    cnt += 1
        for row in range(c[1], c[2]):
            for i in range(M):
                if flag[row][i] != 'R':
                    cnt += 1
        if minimum > cnt:
            minimum = cnt

    print('#{} {}'.format(tc, minimum))


