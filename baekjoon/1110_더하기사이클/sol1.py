# https://www.acmicpc.net/problem/1110

N = int(input())

x = (N % 10) * 10 + (N // 10 + N % 10) % 10
count = 1

while x != N:
    x = (x % 10) * 10 + (x // 10 + x % 10) % 10
    count += 1

print(count)