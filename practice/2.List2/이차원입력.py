arr = [[1, 2, 3, 4], [1, 2, 3]]

for i in arr:
    print(i)

# 크게 3가지?

N, M = map(int, input().split())

# 1
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

# 2
# arr = [0] * N
#
# for i in range(N):
#     arr[i] = (list(map(int, input().split())))

# 3
# arr = [list(map(int, input().split())) for _ in range(N)]

for i in arr:
    print(i)