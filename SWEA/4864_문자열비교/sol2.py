import sys
sys.stdin = open('sample_input.txt')

def 브루트포스1(p, t):
    # for문
    for i in range(len(t)-len(p)+1):
        # 패턴의 길이만큼 반복
        is_ok = True # for else 구문이 생각나지 않을때 변수를 활용
        for j in range(len(p)):
            if p[j] != t[i+j]:
                is_ok = False
                break
        # else:
        #     return 1
        if is_ok:
            return 1
    return 0

def 브루트포스2(p, t):
    i = 0 # t텍스트를 컨트롤 하는 인덱스
    j = 0 # p패턴을 컨트롤 하는 인덱스

    # j가 패턴의 길이가 된다면 찾았다면 멈춘다.
    # i가 텍스트의 길이가 된다면 멈춘다.
    while j < len(p) and i < len(t):
        if p[j] != t[i]:
            i = i-j # 시작 위치로 돌아가고
            j = -1
        i += 1
        j += 1

    # 패턴을 찾았다
    if j == len(p): return 1
    else: return 0

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # if str1 in str2:
    #     print('#{} 1'.format(tc))
    # else:
    #     print('#{} 0'.format(tc))

    # ans = 0
    # if str2.find(str1) != -1:
    #     ans = 1
    # print('#{} {]'.format(tc, ans))

    # print(브루트포스1(str1, str2))

    print(브루트포스2(str1, str2))


