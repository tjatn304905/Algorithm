import sys
sys.stdin = open('sample_input.txt')

def my_reverse(line):
    r_line = []
    # 뒤에서부터 읽어오면서 뒤집은 리스트를 만들자!
    for i in range(len(line)-1, -1, -1):
        r_line.append((line[i]))

    return r_line

def my_find():
    # 전체크기가 N
    for i in range(N):
        # 가로검사
        for j in range(N-M+1):
            # 부분문자열을 위한 빈리스트
            tmp = []
            # 부분문자열 완성!!
            for k in range(M):
                tmp.append(words[i][j+k])
            # 회문검사
            if tmp == my_reverse(tmp):
                return tmp
        #################################
        # 세로검사
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(words[j+k][i])
            if tmp == my_reverse(tmp):
                return tmp
    # 문제에서 회문이 1개 존재한다고 하였으므로 필요하지는 않음
    return []

T = int(input())

for tc in range(1, T+1):
    # N: 2차원 리스트의 크기 10 <= N <= 100
    # M: 우리가 찾고 싶은 회문의 길이 5 <= M < N
    N, M = map(int, input().split())

    # 리스트 내포 방식을 이용한 입력 처리
    words = [list(input()) for _ in range(N)]

    ans = my_find()

    print('#{} {}'.format(tc, ''.join(ans)))