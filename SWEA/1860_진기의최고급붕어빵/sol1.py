import sys
sys.stdin = open('input.txt')

def solution(M, K, customers):
    # 손님 카운트하는 리스트
    count = [0] * 11112
    for customer in customers:
        count[customer] += 1

    time = -1
    bread = 0
    idx = 0
    while idx < len(count):
        # 시간 카운트
        time += 1

        # M 도달하면 초기화, 빵의 개수에 K개 더하기
        if time > 0 and time % M == 0:
            bread += K

        # 손님이 오면 손님 수만큼 빵에서 빼기
        if count[idx]:
            bread -= count[idx]

        if bread < 0:
            return 'Impossible'

        idx += 1

    return 'Possible'



T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))

    print('#{} {}'.format(tc, solution(M, K, customers)))