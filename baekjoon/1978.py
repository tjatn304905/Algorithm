# https://www.acmicpc.net/problem/1978

# N을 입력받는다.
N = int(input())

# N회만큼 자연수를 입력받는다.
num_list = list(map(int, input().split()))

count = 0
for num in num_list:
    # 자연수가 1이라면
    if num == 1: 
        continue
    # 자연수가 1이 아니라면
    else:
        # 2부터 그 자연수보다 1작은 수까지 약수가 있다면 빠져나오고
        for i in range(2, num):
            if num % i == 0:
                break
        # 그렇지 않다면 count에 1을 더하고 빠져나온다.
        else:
            count += 1
print(count)

# 여기서 배운것은 ??? for~else 문!!