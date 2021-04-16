import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    numbers, N = input().split()

    numbers = list(map(int, numbers))
    N = int(N)

    n = 0

    print(numbers)

    # N번만큼만 선택정렬
    for i in range(len(numbers)):

        if n == N:
            break

        n += 1

        maxi = i
        for j in range(i+1, len(numbers)):
            if numbers[j] >= numbers[maxi]:
                maxi = j
            numbers[i], numbers[maxi] = numbers[maxi], numbers[i]

    print('sorted', numbers)




