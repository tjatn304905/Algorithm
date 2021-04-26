import sys
sys.stdin = open('input.txt')


def solution(idx, total):
    global maximum

    # 유망하지 않은 것은 가지치기
    if total <= maximum:
        return

    # 재귀함수를 이용한 순열로 순서를 하나씩 나열
    if idx == N:  # 종료조건
        if total > maximum:
            maximum = total
    else:
        for i in range(N):
            if check[i] == 0:
                # 확률 곱하기
                total_here = total
                total *= P[idx][order[i]] / 100
                check[i] = 1

                solution(idx+1, total)

                # 다음 반복문을 위한 원상복구
                check[i] = 0
                total = total_here


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    order = list(range(N))  # 인덱스 순서 리스트

    sel = [0] * N  # 결과들이 저장될 리스트
    check = [0] * N  # 해당 원소를 이미 사용했는지 안했는지에 대한 체크

    maximum = 0

    solution(0, 1)

    print('#{} {}'.format(tc, format(maximum * 100, ".6f")))