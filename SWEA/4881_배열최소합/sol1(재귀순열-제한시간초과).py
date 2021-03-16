import sys
sys.stdin = open('sample_input.txt')

def perm(idx):
    # 열마다 순열의 숫자에 해당하는 값들을 더함
    # 이미 나온 최소값보다 크면 더하는 것을 중지
    if idx == N:
        total = 0
        for order in range(N):
            total += matrix[order][sel[order]]
            if total > totals[-1]:
                break
        else:
            totals.append(total)
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i] # 값을 써라
                check[i] = 1 # 사용을 했다는 표시
                perm(idx+1)
                check[i] = 0 # 다음 반복문을 위한 원상복구


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    arr = list(range(0, N))

    sel = [0] * N # 결과들이 저장될 리스트
    check = [0] * N # 해당 원소를 이미 사용했는지 체크하는 리스트
    
    totals = [100] # 합들을 저장할 리스트

    perm(0) # 순열생성


    print('#{} {}'.format(tc, totals[-1]))