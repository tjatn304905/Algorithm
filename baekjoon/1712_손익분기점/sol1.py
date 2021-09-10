# https://www.acmicpc.net/problem/1712

# A, B, C 를 입력받는다.
A, B, C = map(int, input().split())
# B가 C보다 크거나 같으면 손익분기점에 도달할 수 없다.
if B >= C:
    print(-1)
# B가 C보다 작으면
else:
    # 반복문으로 했더니 시간 초과!!
    # n = 0
    # # while 문을 계속 반복한다.
    # while True:
    #     n += 1
    #     # 밑의 식이 성립하면 n을 출력하고 break한다.
    #     if A + B*n < C*n:
    #         print(n)
    #         break

    # 다시 식을 짜보았다.
    # C와 B의 차이로 A를 나눈 몫에 1을 더해 출력한다!
    print((A // (C - B)) + 1)