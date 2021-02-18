import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    idx = 0
    count = 0
    while idx <= len(A):
        if idx == len(A):
            break
        elif A[idx:idx + len(B)] == B:
            idx += len(B)
            count += 1
        else:
            idx += 1
            count += 1

    print('#{} {}'.format(tc, count))