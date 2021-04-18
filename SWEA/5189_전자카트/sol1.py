import sys
sys.stdin = open('sample_input.txt')

def perm(numbers, idx):
    global candis

    if idx == N-1:
        # 1뺀 나머지에 대한 순열 -> 후보군 리스트에 더해주기
        candis.append([1] + numbers[:] + [1]) # 그냥 numbers와 numbers[:] 썼을 때 차이는??

    else:
        for i in range(idx, N-1):
            numbers[idx], numbers[i] = numbers[i], numbers[idx]
            perm(numbers, idx+1)
            numbers[idx], numbers[i] = numbers[i], numbers[idx]


def solution(candis):

    minimum = 10000

    for candi in candis:
        result = 0
        for idx in range(1, len(candi)):
            if idx == len(candi) - 1:
                result += golf_zone[candi[idx-1]-1][candi[idx]-1]
                if result < minimum:
                    minimum = result
            else:
                result += golf_zone[candi[idx-1]-1][candi[idx]-1]

    return minimum


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    golf_zone = [list(map(int, input().split())) for _ in range(N)]

    # 1뺀 나머지 숫자들 리스트
    numbers = []
    for i in range(2, N + 1):
        numbers.append(i)

    # 후보군 리스트
    candis = []

    # 순열 실행
    perm(numbers, 0)

    print('#{} {}'.format(tc, solution(candis)))

