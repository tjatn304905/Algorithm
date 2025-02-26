import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, list(input())))

    # 길이가 10인 리스트 생성
    cards = [0]*10
    babygin = 0

    # numbers 리스트의 숫자를 인덱스로하는 cards 리스트 요소에 1 추가
    for num in numbers:
        cards[num] += 1

    # 오차를 없애기 위해 두번 검사
    for i in range(2):
        # triplet 검사
        for idx in range(len(cards)):
            if cards[idx] >= 3:
                cards[idx] -= 3
                babygin += 1

        # run 검사
        for idx in range(len(cards)-2):
            if cards[idx] and cards[idx+1] and cards[idx+2]:
                cards[idx] -= 1
                cards[idx+1] -= 1
                cards[idx+2] -= 1
                babygin += 1

    if babygin == 2:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))