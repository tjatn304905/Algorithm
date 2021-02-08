import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    length = int(input())
    # 입력 숫자를 리스트로 바꾼다.
    buildings = list(map(int, input().split()))
    count = 0
    # 양쪽 두개는 순회할 때 제외한다.
    for idx in range(2, length - 2):
        # 양쪽 두개의 건물보다 높아야 한다.
        if buildings[idx] > buildings[idx-1] and buildings[idx] > buildings[idx-2] and buildings[idx] > buildings[idx+1] and buildings[idx] > buildings[idx+2]:
            # 양쪽 두개의 건물중에 가장 높은 건물을 찾는다.
            # 좌측 두개 비교
            if buildings[idx-2] > buildings[idx-1]:
                left = buildings[idx-2]
            else:
                left = buildings[idx-1]

            # 우측 두개 비교
            if buildings[idx+1] > buildings[idx+2]:
                right = buildings[idx+1]
            else:
                right = buildings[idx+2]

            # 좌우측 비교
            if left > right:
                count += buildings[idx] - left
            else:
                count += buildings[idx] - right

    print('#{} {}'.format(tc, count))