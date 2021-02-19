import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    cnt = [0] * len(str1)

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt[i] += 1

    ans = 0
    # 가장 큰값 찾기
    for i in range(len(cnt)):
        if ans < cnt[i]:
            ans = cnt[i]

    # ans = max(cnt)

    print('#{} {}'.format(tc, ans))
