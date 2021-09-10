arr = [55, 7, 78, 12, 42]

def BubbleSort(a): # 정렬할 List
    for i in range(len(a)-1, 0, -1) : # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

BubbleSort(arr)

print(arr)