# https://www.acmicpc.net/problem/2869

# 수를 입력받는다.
ABV = list(map(int, input().split()))
A = ABV[0]
B = ABV[1]
C = ABV[2]

result = 0

# C에서 A를 뺀구간부터는 한번에 간다. 따라서 그 전까지의 몫을 구하고 1을 더해준다.
result += (C - A) // (A - B) + 1
# 나머지가 0이 아니었다면 1을 더해준다.
if (C - A) % (A - B):
    result += 1
print(result)