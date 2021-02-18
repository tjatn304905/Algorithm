import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    bar_laser = input()
    count = idx = laser = 0
    result_list = []

    while idx < len(bar_laser):
        # laser
        if bar_laser[idx:idx+2] == '()':
            laser += 1
            result_list += [count] # bar layer 출력, 즉 그 laser가 지나가는 bar 개수
            idx += 2
        # bar layer 쌓기
        elif bar_laser[idx] == '(':
            count += 1
            idx += 1
        # bar layer 빼기
        else:
            count -= 1
            idx += 1

    # 원래 막대기 개수
    bar_count = -laser + bar_laser.count(')')

    result = sum(result_list) + bar_count

    print('#{} {}'.format(tc, result))