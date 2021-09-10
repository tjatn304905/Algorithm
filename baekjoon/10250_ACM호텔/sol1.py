# https://www.acmicpc.net/problem/10250

T = int(input())

for tc in range(1, T+1):
    H, W, N = map(int, input().split())

    # 층수는 N을 H로 나눈 나머지에 100을 곱한수
    # 방 번호는 몫에 1을 더한 값이다.
    # 나머지가 0이라면 층수는 최고층수이고, 방 번호는 그냥 몫이다
    if N % H:
        YY = (N % H) * 100
        XX = (N // H) + 1
    else:
        YY = H * 100
        XX = (N // H)
     
    print(YY + XX)