import sys
sys.stdin = open('sample_input.txt')


def backtrack(a, k, N):
    global minimum
    c = [0] * (N+1)

    if k == N:
        total = 0
        for i in range(1, k+1):
            total += matrix[i-1][a[i]-1]
            if total > minimum:
                break
        else:
            minimum = total
            totals.append(minimum)

    else:
        k += 1
        ncandidates = construct_candidates(a, k, N, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, N)


def construct_candidates(a, k, N, c):
    visited = [False] * (N+1)

    for i in range(1, k):
           visited[a[i]] = True

    ncandidates = 0
    for i in range(1, N+1):
       if visited[i] == False:
           c[ncandidates] = i
           ncandidates += 1

    return ncandidates

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    a = [0] * (N+1)
    k = 0
    totals = []
    minimum = 100

    backtrack(a, k, N)

    print('#{} {}'.format(tc, totals[-1]))