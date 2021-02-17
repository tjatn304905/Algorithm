N = int(input())

count = 0

while N >= 3:
    if N % 5 == 0:
        count += N // 5
        N = 0
    elif N % 3 == 0:
        count += N // 3
        N = 0
    elif N >= 5:
        count += 1
        N -= 5
    elif N >= 3:
        count += 1
        N -= 3

print(count) if N == 0 else print(-1) 