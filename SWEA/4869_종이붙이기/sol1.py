import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    n = N // 10
    # n은 n-1일때에 양쪽에 20x10 하나씩 붙이는 방법과, n-2일때 양쪽에 20x20 하나씩 붙이는 방법이 있다.
    f = [1, 3]

    for i in range(2, n):
        f.append(f[i-1] + f[i-2]*2)

    print('#{} {}'.format(tc, f[n-1]))

