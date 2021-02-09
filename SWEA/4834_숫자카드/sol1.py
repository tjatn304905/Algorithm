import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 카드들
    cards = list(map(int, list(input())))
    # 카드 개수
    numbers = [0]*10

    for card in cards:
        numbers[card] += 1

    index = 0 # 숫자
    count = 0 # 개수
    for idx in range(len(numbers)):
        if numbers[idx] >= count:
            count = numbers[idx]
            index = idx

    print('#{} {} {}'.format(tc, index, count))
