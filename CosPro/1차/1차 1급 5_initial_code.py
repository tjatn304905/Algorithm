# You may use import as below.
#import math
#import pprint

def solution(n):
    # Write code here.
    answer = 0
    arr = [[0 for j in range(n)] for i in range(n)]

    dir_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dir_cnt = 0
    dir = dir_list[dir_cnt]

    now = [0, 0]

    for i in range(n*n):
        arr[now[0]][now[1]] = i + 1

        next = [now[0] + dir[0], now[1] + dir[1]]
        if next[0] >= n or next[1] >= n or arr[next[0]][next[1]] != 0:
            dir_cnt += 1
            if dir_cnt >= 4:
                dir_cnt = 0
            dir = dir_list[dir_cnt]
        now = [now[0] + dir[0], now[1] + dir[1]]

    for i in range(n):
        answer += arr[i] [i]

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(arr)
    return answer


#The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret1, ".")
    
n2 = 2
ret2 = solution(n2)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret2, ".")