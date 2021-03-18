import sys
sys.stdin = open('sample_input.txt')

def solution(lexi):

    cores = search(lexi)

    result = 0

    for core in cores:
        i = core[1]
        j = core[2]

        min_wire = 12
        # 가장 짧은 길 찾기
        # 상
        for test in range(i-1, -1, -1):
            if lexi[test][j] != 0:
                break
        else:
            min_wire = i
            direction = 0

        # 하
        for test in range(i+1, N):
            if lexi[test][j] != 0:
                break
        else:
            if (N-1) - i < min_wire:
                min_wire = (N-1)-i
                direction = 1

        # 좌
        for test in range(j-1, -1, -1):
            if lexi[i][test] != 0:
                break
        else:
            if j < min_wire:
                min_wire = j
                direction = 2

        # 우
        for test in range(j+1, N):
            if lexi[i][test] != 0:
                break
        else:
            if (N-1) - j < min_wire:
                min_wire = (N-1) - j
                direction = 3

        # 전선 연결
        # 상
        if direction == 0:
            for wire in range(i - 1, -1, -1):
                lexi[wire][j] = 2
        # 하
        elif direction == 1:
            for wire in range(i + 1, N):
                lexi[wire][j] = 2
        # 좌
        elif direction == 2:
            for wire in range(j - 1, -1, -1):
                lexi[i][wire] = 2
        # 우
        elif direction == 3:
            for wire in range(j + 1, N):
                lexi[i][wire] = 2

        result += min_wire

    return result

def search(lexi):
    cores = []
    for i in range(N):
        for j in range(N):
            if lexi[i][j] == 1: # 코어가 있는 부분
                cnt = 0 # 코어가 가로막고 있는 방향 갯수
                #상
                for test in range(i - 1, -1, -1):
                    if lexi[test][j] == 1:
                        cnt += 1
                        break

                # 하
                for test in range(i + 1, N):
                    if lexi[test][j] == 1:
                        cnt += 1
                        break

                # 좌
                for test in range(j - 1, -1, -1):
                    if lexi[i][test] == 1:
                        cnt += 1
                        break

                # 우
                for test in range(j + 1, N):
                    if lexi[i][test] == 1:
                        cnt += 1
                        break

                cores.append((cnt, i, j))

    # 가로막힌 방향이 많은 코어순으로 정렬(많이 가로막힐수록 방향이 한정됨)
    cores.sort(reverse=True)
    for core in cores:
        if core[0] > 3:
            cores.remove(core)
    return cores

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lexi = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(tc, solution(lexi)))