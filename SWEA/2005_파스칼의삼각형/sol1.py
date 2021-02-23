import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    print('#{}'.format(tc))

    triangle = [1]

    for i in range(1, N):
        # 첫번째 줄 출력
        print(*triangle)
        # 뒤 순서부터 값을 갱신해야 다음 값에 영향을 안 미침
        for j in range(len(triangle)-1, 0, -1): # 끝부터 1번 인덱스까지 값을 갱신
            triangle[j] = triangle[j-1] + triangle[j]
        # 값이 하나씩 늘어나면서 마지막 숫자는 무조건 1
        triangle.append(1)
    print(*triangle)