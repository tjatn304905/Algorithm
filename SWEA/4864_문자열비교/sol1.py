import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    for i in range(len(str2)):
        # str1의 첫번째 글자와 같고, 그 부분에서 남은 길이가 str1 이상이라면
        if str1[0] == str2[i] and len(str2) - i >= len(str1):
            # 검사
            for j in range(1, len(str1)):
                if str1[j] != str2[i+j]:
                    result = 0
                    break
            else:
                result = 1
                break
        else:
            result = 0

    print('#{} {}'.format(tc, result))