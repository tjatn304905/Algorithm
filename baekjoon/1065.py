# https://www.acmicpc.net/problem/1065

N = int(input())

count = 0
n = 1
while n <= N:
    if n < 10:
        count += 1
    elif n < 100:
        count += 1
    elif n < 1000:
        if (n // 100) - (n - (n // 100)*100) // 10 == (n - (n // 100)*100) // 10 -(n % 10):
            count +=1
    else:
        pass
    n += 1
print(count)