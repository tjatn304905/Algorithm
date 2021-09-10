# https://www.acmicpc.net/problem/1193

# X를 입력받는다.
X = int(input())

# n! 과 (n+1)!번째 사이에 있는 수의 분자와 분모의 합이 (n+1)인 규칙이 있음 
count = 0
add = 0

# 1씩 추가되는 add를 count에 더함으로써 팩토리얼을 구현
while True:
    add += 1
    count += add
    # X가 count보다 작거나 같아지는 순간에 break
    # 이때 add가 바로 n임
    if count >= X:
        break

# add가 홀수냐 짝수냐에 따라서 분모와 분자의 시작값이 바뀐다는 특성이 있음
# add가 홀수일때 분모가 1, 분자가 add로 시작, add가 짝수일때는 그 반대.
# count에서 X를 뺀 값을 이용
# add가 홀수라면
if add % 2:
    result1, result2 = (count - X + 1), (add - (count - X))
# add가 짝수라면 
else:
    result1, result2 = (add - (count - X)), (count - X + 1)

print(f'{result1}/{result2}')
