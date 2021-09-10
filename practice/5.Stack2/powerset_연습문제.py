# 원소의 합이 10인 부분집합 구하기

arr = list(range(1, 11))
sel = [0] * len(arr)

def powerset(idx):
    if idx == len(arr):
        total = 0
        arr2 = []
        for i in range(len(arr)):
            if sel[i]:
                total += arr[i]
                arr2.append(arr[i])
        if total == 10:
            print(arr2)
        return

    sel[idx] = 1
    powerset(idx+1)

    sel[idx] = 0
    powerset(idx+1)

powerset(0)