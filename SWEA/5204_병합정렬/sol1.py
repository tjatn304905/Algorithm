import sys
sys.stdin = open('sample_input.txt')


# 분할과정
def merge_sort(numbers):
    # 종료조건
    if len(numbers) < 2:
        return numbers

    left = numbers[0:len(numbers)//2]
    right = numbers[len(numbers)//2:len(numbers)]

    left = merge_sort(left)
    right = merge_sort(right)

    # 병합과정
    global count

    result = []
    l = r = 0

    # left의 마지막 요소가 right의 그것보다 크다면 count 를 1 더해준다
    if left[-1] > right[-1]:
        count += 1

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]

    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    count = 0

    ans = merge_sort(numbers)

    print('#{} {} {}'.format(tc, ans[N//2], count))

