import sys
sys.stdin = open('sample_input.txt')
'''
LIFO(Last In First Out)
'''
T = int(input())

for tc in range(1, T+1):
    iron_bar = input()

    # 실제로 철봉이 담길 리스트
    s = []
    ans = 0

    for i in range(len(iron_bar)):
        # 열린괄호라면 s 리스트에 넣어놓기
        if iron_bar[i] == '(':
            s.append('(')
        else:
            #무조건 꺼내기
            s.pop()
            #레이저
            if iron_bar[i-1] == '(':
                ans += len(s)
            else:
                ans += 1

    print('#{} {}'.format(tc, ans))