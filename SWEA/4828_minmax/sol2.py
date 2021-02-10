def Bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 전체 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    number = list(map(int, input().split()))

    # 정렬 후 출력
    # Bubble_sort(number)
    #
    # print('#{} {}'.format(tc, number[0]-number[-1]))

    max_value = 0
    min_value = 9213085132

    for i in range(N):
        # 최대값 갱신
        if max_value < number[i]:
            max_value = number[i]

        # 최소값 갱신
        if min_value > number[i]:
            min_value = number[i]

    print("#{} {}".format(tc, max_value-min_value))
