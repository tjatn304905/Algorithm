import sys
sys.stdin = open('sample_input.txt')


def solution(idx, total):
    global minimum

    # 유망하지 않은 것은 가지치기
    if total >= minimum:
        return

    # 재귀함수를 이용한 순열로 순서를 하나씩 나열
    if idx == N:
        if total < minimum:
            minimum = total
    else:
        for i in range(N):
            if check[i] == 0:
                # 비용 합산하기
                total += V[idx][order[i]]
                check[i] = 1

                solution(idx+1, total)

                # 다음 반복문을 위한 원상복구
                check[i] = 0
                total -= V[idx][order[i]]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]

    order = list(range(N))  # 인덱스 순서 리스트

    sel = [0] * N  # 결과들이 저장될 리스트
    check = [0] * N  # 해당 원소를 이미 사용했는지 안했는지에 대한 체크

    minimum = 15 * 99

    solution(0, 0)

    print('#{} {}'.format(tc, minimum))