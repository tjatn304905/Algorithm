N = int(input())

result = 0

# 5의 배수일때, 무조건 5로 나눈 몫
if N % 5 == 0:
    result = N // 5
# 5의 배수가 아닐 때, 3씩 빼면서 5로 나누어지는지 확인
else:
    while N > 0:
        N -= 3
        result += 1
        if N % 5 == 0:
            result += N // 5
            break
    # 끝까지 안나누어 지고 나머지가 남는다면 -1 출력
    else:
        result = -1

print(result)
 