import sys
sys.stdin = open('sample_input.txt')

T = int(input())
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, T+1):
    a, b = map(int, input().split())
    count = 0
    for i in range(1<<12):
        total = 0
        total_list = []
        for j in range(13):
            if i & (1<<j):
                total += num_list[j]
                total_list += [num_list[j]]

        if len(total_list) == a and total == b:
            count += 1

    print('#{} {}'.format(tc, count))