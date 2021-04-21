import sys
sys.stdin = open('sample_input.txt')


def binary_search(low, high, prev):

    global count

    if low > high:
        return
    else:
        mid = (low + high) // 2
        if n_list[mid] in m_list:
            count += 1
        # 이전 방향이 오른쪽이었다면 왼쪽으로 재귀
        if prev == 'right':
            binary_search(low, mid-1, 'left')
        # 이전 방향이 왼쪽이었다면 오른쪽으로 재귀
        elif prev == 'left':
            binary_search(mid+1, high, 'right')
        # 처음 시작할때는 양방향으로 재귀
        else:
            binary_search(low, mid - 1, 'left')
            binary_search(mid + 1, high, 'right')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    n_list = sorted(list(map(int, input().split())))
    m_list = list(map(int, input().split()))

    count = 0

    binary_search(0, N-1, 'none')

    print('#{} {}'.format(tc, count, 0))