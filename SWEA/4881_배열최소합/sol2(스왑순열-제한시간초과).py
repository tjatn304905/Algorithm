import sys
sys.stdin = open('sample_input.txt')


def perm(idx):
    if idx == N:
        total = 0
        for order in range(N):
            total += matrix[order][arr[order]]
        totals.append(total)

    else:
        for i in range(idx, N):
            # 순서를 바꾸고
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx+1)
            # 원상복귀
            arr[idx], arr[i] = arr[i], arr[idx]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    arr = list(range(0, N))

    totals = []  # 합들을 저장할 리스트

    perm(0)  # 순열생성

    minimum = totals[0]
    for total in totals:
        if total < minimum:
            minimum = total

    print('#{} {}'.format(tc, minimum))