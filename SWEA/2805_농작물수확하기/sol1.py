import sys
sys.stdin = open('input.txt')

def solution(N, farm):
    total = 0

    for i in range(N):
        # 중간까지: 중앙에서부터 수확을 한칸씩 늘이면서
        if i <= N // 2:
            total += int(farm[i][N//2]) # 중앙에 있는 수확물
            if i > 0:
                for j in range(1, i+1):
                    total += int(farm[i][N//2 - j]) + int(farm[i][N//2 + j])
        # 중간이후: 중앙에서부터 수확을 한칸씩 줄이면서
        else:
            total += int(farm[i][N // 2])  # 중앙에 있는 수확물
            if i < N-1:
                for j in range(1, N - i):
                    total += int(farm[i][N//2 - j]) + int(farm[i][N//2 + j])

    return total
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [input() for _ in range(N)]

    print('#{} {}'.format(tc, solution(N, farm)))