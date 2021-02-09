import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range (1, T+1):
    number = int(input())

    nums = [2, 3, 5, 7, 11]
    alpha = [0]*5
    idx = 0
    for num in nums:
        count = 0
        while number % num == 0:
            number = number / num
            count += 1
        alpha[idx] = count
        idx += 1

    print('#{} {} {} {} {} {}'.format(tc, alpha[0], alpha[1], alpha[2], alpha[3], alpha[4]))