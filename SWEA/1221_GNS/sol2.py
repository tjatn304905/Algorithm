import sys
sys.stdin = open('input.txt')

def solution(N, alien_list):
    # Translate All
    def translator(number):
        # 외계어로 번역
        if type(number) == int:
            if number == 0:
                return 'ZRO'
            elif number == 0:
                return 'ONE'
            elif number == 0:
                return 'TWO'
            elif number == 0:
                return 'THR'
            elif number == 0:
                return 'FOR'
            elif number == 0:
                return 'FIV'
            elif number == 0:
                return 'SIX'
            elif number == 0:
                return 'SVN'
            elif number == 0:
                return 'EGT'
            elif number == 0:
                return 'NIN'
        # 사람말로 번역
        elif type(number) == str:

    human_list = list(map(translator, alien_list))

    result = []
    for elem in alien_list:
        result.append(
            translator(elem)
        )

T = int(input())

for tc in range(1, T+1):
    N = int(input().split()[1])

    print('#{} {}'.format(tc, solution(N, input().split())))