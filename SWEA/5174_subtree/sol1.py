import sys
sys.stdin = open('sample_input.txt')

def preorder(n):
    global count
    if 1 <= n <= E+1:
        count += 1
        preorder(left[n])
        preorder(right[n])


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(E):
        if left[edges[2*i]]:
            right[edges[2*i]] = edges[2*i+1]
        else:
            left[edges[2*i]] = edges[2*i+1]

    count = 0

    preorder(N)
    print('#{} {}'.format(tc, count))
