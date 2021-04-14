import sys
sys.stdin = open('sample_input.txt')


def change(N):
    result = ''
    for i in range(1, 13):
        if N >= 1 / 2**i:
            result += '1'
            N -= 1 / 2**i
            if N == 0:
                return result
        else:
            result += '0'
    return 'overflow'


T = int(input())

for tc in range(1, T+1):
    N = float(input())

    print('#{} {}'.format(tc, change(N)))