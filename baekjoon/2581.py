# https://www.acmicpc.net/problem/2581

# 자연수 M과 N을 입력받는다.
M = int(input())
N = int(input())

# 소수들을 담을 리스트 생성
sosu_list = []

# M이상 N이하인 자연수들을 순회
for num in range(M, N+1):
    # num이 1이라면 넘어간다.
    if num == 1:
        continue
    # num이 1이 아니라면
    else:
        # 2 이상, num미만의 자연수를 순회하며
        for i in range(2, num):
            # 약수가 있다면 빠져나오고
            if num % i == 0:
                break
        # 약수가 없어서 빠져나왔다면,
        else:
            # 소수 리스트에 num을 추가한다.
            sosu_list.append(num)

if len(sosu_list):   
    print(sum(sosu_list))
    print(sosu_list[0])
else:
    print(-1)
            