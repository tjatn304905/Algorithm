# https://www.acmicpc.net/problem/2884

# 두 수를 입력 받는다.
a, b = map(int,input().split())

# 기존 알람 시간이 0시 45분보다 작을때
if a == 0 and b < 45:
    a = 23
    b = b + 15
# 그렇지 않으면
else:      
    # 기존 알람에 설정한 분이 45분보다 작을때
    if b < 45:
        # a에서 1을 빼준다
        a = a - 1 
        # b에서는 (60-45)를 더해준다.
        b = b + 15
    # 그렇지 않으면
    else:
        # b에서 45를 빼준다.
        b = b -45
        
print(a, b)