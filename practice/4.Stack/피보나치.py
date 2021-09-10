# def fibo(n):
#
#     arr[n] += 1
#     if n < 2:
#         return n
#
#     return fibo(n-1) + fibo(n-2)
#
# # 호출 횟수
# arr = [0] * 35
#
# print(fibo(30))
# print(arr)
# print(sum(arr))

# 메모이제이션
def fibo1(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]

print(fibo1(40))
print(memo)

####################################

memo2 = [-1] * 21
memo2[0] = 0
memo2[1] = 1

def fibo2(n):
    if memo2[n] == -1:
        memo2[n] = fibo2(n-1) + fibo2(n-2)

    return memo2[n]

print(fibo2(10))
print(memo2)