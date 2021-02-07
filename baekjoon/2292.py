# https://www.acmicpc.net/problem/2292

# 1부터 거리가 1인 수들, 2인 수들, 3인 수들....
# 위처럼 수들을 1부터의 거리별로 모아봤을때 갯수는 6개, 12개, 18개....로 6개씩 늘어난다는 규칙을 보인다.

# N을 입력받는다.
N = int(input())

count = 0
num = 0
while True:
    # count는 1, 2, 3, 4,...
    count += 1
    # num은 1, 3, 6, 10,...
    num += count
    if N == 1:
        print(1)
        break
    elif 6 * num > N-2:
        print(count+1)
        break
