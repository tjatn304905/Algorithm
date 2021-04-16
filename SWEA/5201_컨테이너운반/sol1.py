import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    # 무게별로 남은 컨테이너의 갯수를 담은 딕셔너리
    containers = {}
    for weight in weights:
        if weight in containers.keys():
            containers[weight] += 1
        else:
            containers[weight] = 1

    result = 0

    # 트럭 적재용량을 순회하면서 적재용량별로 최대로 담을 수 있는 컨테이너 옮기기
    for truck in trucks:
        maximum = 0
        for container in containers.keys():
            if maximum < container <= truck and containers[container]:
                maximum = container
        # 맥시멈이 바뀌지 않았으면 그대로, 바뀌었으면 1 줄이기
        if maximum != 0:
            containers[maximum] -= 1
            result += maximum

    print('#{} {}'.format(tc, result))
