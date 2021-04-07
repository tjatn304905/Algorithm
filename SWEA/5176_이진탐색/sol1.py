import sys
sys.stdin = open('sample_input.txt')

def preorder(n):
    global cnt
    if 1 <= n <= N:
        preorder(left[n])
        cnt += 1
        values[n] = cnt
        preorder(right[n])

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    left = [0] * (N+1)
    right = [0] * (N+1)
    values = [0] * (N+1) # 노드의 값을 담아줄 리스트
    cnt = 0

    # 완전 이진트리 만들기
    for i in range(1, N//2 + 1):
        left[i] = i*2
        if i*2+1 <= N:
            right[i] = i*2+1

    preorder(1)

    print('#{} {} {}'.format(tc, values[1], values[N//2]))
