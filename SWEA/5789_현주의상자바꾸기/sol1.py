import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    boxes = [0]*N
    i = 0

    for q in range(Q):
        L, R = map(int, input().split())
        i += 1
        for idx in range(L-1, R):
            boxes[idx] = i

    result = '#' + str(tc)
    for box in boxes:
        result += ' ' + str(box)

    print(result)
