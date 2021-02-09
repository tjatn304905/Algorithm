import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    dump_list = [0]*100

    # 박스 높이별 리스트
    for box in boxes:
        dump_list[box-1] += 1

    count = 0
    # 덤프 횟수가 될때까지 순회
    while count < dump:
        # 아래쪽에 쌓기
        for idx in range(99):
            if dump_list[idx]:
                dump_list[idx] -= 1
                dump_list[idx+1] += 1
                break
        # 위쪽에서 빼기
        for idx in range(99, 0, -1):
            if dump_list[idx]:
                dump_list[idx] -= 1
                dump_list[idx-1] += 1
                break
        count += 1


    for idx in range(99):
        if dump_list[idx]:
            minimum = idx
            break
    for idx in range(99, 0, -1):
        if dump_list[idx]:
            maximum = idx
            break

    result = maximum-minimum

    print('#{} {}'.format(tc, result))