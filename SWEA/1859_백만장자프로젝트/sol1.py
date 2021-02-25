import sys
sys.stdin = open('input.txt')

def solution(prices):
    maximum = prices[-1]
    sum = 0
    for i in range(len(prices)-1, -1, -1):
        if prices[i] < maximum:
            sum += maximum - prices[i]
        else:
            maximum = prices[i]

    return sum


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    print('#{} {}'.format(tc, solution(prices)))