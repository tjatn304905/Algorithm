# https://www.acmicpc.net/problem/4673

not_self_number = set()

n = 1
while n <= 10000:
    x = n
    sum1 = 0
    while x != 0:
        sum1 += x % 10
        x = x // 10
    sum2 = sum1 + n
    not_self_number = not_self_number | {sum2} 
    if n not in not_self_number:
        print(n)
    n += 1
