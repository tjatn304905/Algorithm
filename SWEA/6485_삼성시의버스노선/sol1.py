import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = []
    B = []
    # 숫자 a, b 저장
    for n in range(N):
        a, b = map(int, input().split())
        A += [a]
        B += [b]

    P = int(input())
    bus_stop = [0] * 5000 # 버스정류장
    C = []
    for p in range(P):
        c = int(input())
        C += [c]

    # 버스정류장에 노선 개수 표시
    for idx in range(len(A)):
        for bus in range(A[idx] - 1, B[idx]):
            bus_stop[bus] += 1
    # C에 대한 노선개수 저장
    result = []
    for c in C:
        result += [bus_stop[c-1]]

    # 결과 출력
    ans = ' '.join(map(str,result))
    print('#{} {}'.format(tc, ans))