import sys
sys.stdin = open('sample_input.txt')

def solution(cheese, N):
    # 피자 번호와 치즈의 양을 나타내는 리스트
    pizzas = []
    for i in range(len(cheese)):
        pizzas.append([i+1, cheese[i]])

    # 처음 오븐에 피자 넣기
    oven = []
    for _ in range(N):
        oven.append(pizzas.pop(0))

    while True:
        # 첫번째 피자는 치즈의 양이 반으로 줄어듦
        oven[0][1] = oven[0][1] // 2
        # 오븐의 첫번째 피자의 치즈가 다 녹고, 넣을 피자가 남아있다면
        if oven[0][1] == 0 and pizzas:
            oven.pop(0)
            oven.append(pizzas.pop(0))
        # 오븐의 첫번째 피자의 치즈가 다 녹고, 넣을 피자가 없다면
        elif oven[0][1] == 0:
            oven.pop(0)
            oven.append([0, 0])
        else:
            oven.append(oven.pop(0))

        # 종료조건
        sum = 0
        for pizza in oven:
            if pizza != [0, 0]:
                sum += 1
                last = pizza
        if sum == 1:
            return last[0]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    print('#{} {}'.format(tc, solution(cheese, N)))