import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    ziphops = []

    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]

    while True:
        # 부분집합의 시작점을 찾는다.
        exit = 0
        for y in range(n):
            for x in range(n):
                if matrix[y][x]:
                    start = (x, y)
                    exit = 1
        if exit == 0:
            break

        stack = [start]
        mini = n
        maxi = 0
        cnt = 0
        while stack:
            (x, y) = stack.pop(0)
            if maxi < y:
                maxi = y
            if mini > y:
                mini = y
            for idx in range(4):
                dx = dxs[idx]
                dy = dys[idx]
                if 0 <= x + dx < n and 0 <= y + dy < n and matrix[y + dy][x + dx]:
                    stack.append((x + dx, y + dy))
                    matrix[y + dy][x + dx] = 0
                    cnt += 1
            rows = maxi - mini + 1
            cols = cnt // rows
        ziphops.append((cnt, rows, cols))

    # 집합의 크기, 행렬 수로 정렬
    for i in range(len(ziphops)):
        min = i
        for j in range(i+1, len(ziphops)):
            if ziphops[min][0] > ziphops[j][0]:
                min = j
            elif ziphops[min][0] == ziphops[j][0]:
                if ziphops[min][1] > ziphops[j][1]:
                    min = j
        ziphops[i], ziphops[min] = ziphops[min], ziphops[i]


    print('#{} {}'.format(tc, len(ziphops)), end = ' ')
    for ziphop in ziphops:
        print(ziphop[1], ziphop[2], end = ' ')
    print()



