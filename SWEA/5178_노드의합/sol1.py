import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    values = [0] * (N+1)

    for i in range(M):
        node, value = map(int, input().split())
        values[node] = value
    
    # 번호 거꾸로 순회하면서 부모노드에 누적
    for i in range(N, 1, -1):
        values[i//2] += values[i]

    print('#{} {}'.format(tc, values[L]))