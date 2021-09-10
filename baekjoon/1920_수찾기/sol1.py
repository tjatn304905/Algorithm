N = int(input())
n_list = list(map(int, input().split()))

M = int(input())
m_list = list(map(int, input().split()))


n_list.sort()

for j in range(len(m_list)):
    start = 0
    end = len(n_list) - 1
    while start <= end:
        middle = (start + end) // 2
        if m_list[j] == n_list[middle]:
            print(1)
            break
        elif m_list[j] > n_list[middle]:
            start = middle + 1
        else:
            end = middle - 1
    else:
        print(0)
    