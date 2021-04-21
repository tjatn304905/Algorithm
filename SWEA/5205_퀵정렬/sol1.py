import sys
sys.stdin = open('sample_input.txt')




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # quick_sort(numbers, 0, N-1)
