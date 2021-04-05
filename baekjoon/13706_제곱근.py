def binary(A):
    start = 0
    end = A

    while start <= end:
        mid = (start + end) // 2

        if mid * mid == A:
            return mid
        elif mid * mid < A:
            start = mid + 1
        else:
            end = mid - 1


A = int(input())

print(binary(A))