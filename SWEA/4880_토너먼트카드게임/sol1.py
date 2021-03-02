import sys
sys.stdin = open('sample_input.txt')

def solution(cards):

    if len(cards) == 1:
        return cards.pop()
    elif len(cards) == 2:
        if cards[0] == 1:
            if cards[1] == 2:
                return cards.pop()
            else:
                cards.pop()
                return cards.pop()
        elif cards[0] == 2:
            if cards[1] == 3:
                return cards.pop()
            else:
                cards.pop()
                return cards.pop()
        else:
            if cards[1] == 1:
                return cards.pop()
            else:
                cards.pop()
                return cards.pop()
    else:
        cards1 = cards[0:(len(cards) + 1) // 2]
        cards2 = cards[(len(cards) + 1) // 2:len(cards)]
        solution()

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    print(cards)

    print('#{} {}'.format(tc, solution(cards)))
