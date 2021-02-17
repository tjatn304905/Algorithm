import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# k번째로 큰 수를 반환하는 함수
def select(list, k):
    for i in range(0, k):
        maxIndex = i
        for j in range(i+1, len(list)):
            if list[maxIndex] < list[j]:
                maxIndex = j
        list[i], list[maxIndex] = list[maxIndex], list[i]
    return list[k-1]

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 홀수일때와 짝수일때 규칙을 찾아서 함수 적용
    sorted_numbers = []
    for i in range(10):
        if i % 2:
            k = len(numbers) - (i // 2)
            sorted_numbers += [select(numbers, k)]
        else:
            k = (i // 2) + 1
            sorted_numbers += [select(numbers, k)]

    print('#{} {}'.format(tc, ' '.join(map(str, sorted_numbers))))