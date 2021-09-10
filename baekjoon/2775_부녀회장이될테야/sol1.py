# https://www.acmicpc.net/problem/2869

T = int(input())

for tc in range(1, T+1):
    k = int(input())
    n = int(input())

    # 0층을 포함한 2차원 배열
    rooms_floor = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
    for floor in range(k):
        total = 0
        rooms = []
        # total은 바로 밑에 층의 같은 호수까지 더한 숫자
        for room in range(n):
            total += rooms_floor[floor][room]
            # total이 모여서 rooms 리스트를 만들고
            rooms += [total]
        # rooms가 모여서 rooms_floor를 만듦
        rooms_floor += [rooms]
        # 확인용 출력
        # print(total)
        # print(rooms)
        # print(rooms_floor)

    print(rooms_floor[k][n-1])