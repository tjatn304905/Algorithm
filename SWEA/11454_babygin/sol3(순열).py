arr = [6, 6, 7, 7, 6, 7]

N = 6


def perm(idx):
    global babygin

    if idx == 6:
        print(arr)
        if (arr[0] == arr[1] == arr[2]) or (arr[0] == arr[1] - 1 and arr[1] == arr[2] - 1):
            if (arr[3] == arr[4] == arr[5]) or (arr[3] == arr[4] - 1 and arr[4] == arr[5] - 1):
                babygin = 1

    else:
        for i in range(idx, N):
            # 순서를 바꾸고
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx + 1)
            # 원상복귀
            arr[idx], arr[i] = arr[i], arr[idx]

babygin = 0

perm(0)

if babygin == 1:
    print('babygin')