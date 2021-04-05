import sys
sys.stdin = open('input.txt')

# 전위순회 함수
def preorder(n):
    visited = [0] * (V+1)
    cnt = 0
    if 1<= n <= V:
        visited[n] = 1
        cnt += 1
        preorder(left[n])
        preorder(right(n))
    # A와 B를 자식으로 갖는다면 리턴값을 가지게 된다.
    if visited[A] == visited[B] == 1:
        return n, cnt


T = int(input())
for tc in range(1, T+1):
    V, E ,A, B = map(int, input().split())
    edges = list(map(int, input().split()))
    left = [0] * (V + 1) # 왼쪽자식을 담는 리스트
    right = [0] * (V + 1) # 오른쪽자식을 담는 리스트
    pa = [0] * (V + 1) # 자식의 인덱스에 부모를 담는 리스트
    for i in range(E):
        if left[edges[2*i]] == 0:
            left[edges[2*i]] = edges[2*i+1]
        else:
            right[edges[2*i]] = edges[2*i+1]
        pa[edges[2*i+1]] = edges[2*i]

    x = A
    # A의 부모, 그 부모의 부모 순으로 전위순회하면서 A와 B를 자식으로 갖는 노드를 찾는다.
    while True 
        if preorder(pa[x]) == None:
            x = pa[x]
        else:
            break