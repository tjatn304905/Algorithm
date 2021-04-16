import sys
sys.stdin = open('sample_input.txt')


def solution():

    for idx in range(len(numbers)):
        if idx % 2:
            player_2[numbers[idx]] += 1
        else:
            player_1[numbers[idx]] += 1
        # 1번 플레이어가 이길경우
        for i in range(10):
            if player_1[i] == 3 or (player_1[i] and player_1[i+1] and player_1[i+2]):
                return 1
        # 2번 플레이어가 이길경우
        for i in range(10):
            if player_2[i] == 3 or (player_2[i] and player_2[i+1] and player_2[i+2]):
                return 2

    return 0


T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))

    player_1 = [0] * 12
    player_2 = [0] * 12

    print('#{} {}'.format(tc, solution()))


