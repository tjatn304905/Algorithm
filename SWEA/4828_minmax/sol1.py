import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 최대값
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    # 최소값
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number

    result = maximum - minimum
    print('#{} {}'.format(tc, result))