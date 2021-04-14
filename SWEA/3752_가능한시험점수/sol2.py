import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))

    visited = [0] * (sum(scores) + 1)
    visited[0] = 1
    count = 1

    for score in scores:
        for i in range(len(visited)-1, -1, -1):
            if visited[i] and visited[i + score] == 0:
                visited[i + score] = 1
                count += 1

    print('#{} {}'.format(tc, count))