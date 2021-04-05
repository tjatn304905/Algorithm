import sys
sys.stdin = open('input.txt')

def inorder(n, tree):
    if 1 <= n <= N: # n번째 노드가 존재한다면
        inorder(int(tree[n][1]), tree)
        print(tree[n][0], end='')
        inorder(int(tree[n][2]), tree)


T = 10

for tc in range(1, T+1):
    N = int(input())

    # 이진트리를 담을 리스트
    tree = [[0, 0, 0] for _ in range(N+1)]

    for _ in range(N):
        info = list(input().split())
        for idx in range(1, len(info)):
            tree[int(info[0])][idx-1] = info[idx]


    print('#{}'.format(tc), end=' ')
    inorder(1, tree)
    print()