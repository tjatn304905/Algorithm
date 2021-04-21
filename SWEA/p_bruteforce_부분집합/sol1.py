numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(numbers)

visited = [False] * N

# 1. 재귀 함수 호출
def recursion(idx):
    if idx == N:
        subset = []
        for i in range(N):
            if visited[i]:
                subset.append(numbers[i])
        if sum(subset) == 10:
            print(subset)
        return

    visited[idx] = True
    recursion(idx + 1)
    visited[idx] = False
    recursion(idx + 1)


recursion(0)

print()

# 2. 비트 연산
for i in range(1 << N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append(numbers[j])

    if sum(subset) == 10:
        print(subset)