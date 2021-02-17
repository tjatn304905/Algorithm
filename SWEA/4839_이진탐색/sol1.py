import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    count_a = 0
    count_b = 0
    # A 찾는데 걸리는 횟수
    left = 1
    right = P
    while True:
        count_a += 1
        if A > int((left + right) / 2):
            left = int((left + right) / 2)
        elif A < int((left + right) / 2):
            right = int((left + right) / 2)
        else:
            break
    # B 찾는데 걸리는 횟수
    left = 1
    right = P
    while True:
        count_b += 1
        if B > int((left + right) / 2):
            left = int((left + right) / 2)
        elif B < int((left + right) / 2):
            right = int((left + right) / 2)
        else:
            break

    if count_a < count_b:
        result = 'A'
    elif count_a > count_b:
        result = 'B'
    else:
        result = 0

    print('#{} {}'.format(tc, result))



