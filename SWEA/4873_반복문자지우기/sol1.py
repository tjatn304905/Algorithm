import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    string = list(input())

    while True:
        for i in range(1, len(string)):
            if string[i] == string[i-1]:
                string.pop(i)
                string.pop(i-1)
                break # pop한 뒤에 index 에러가 나지 않도록 break
        else:
            break # 더 이상 pop할 것이 남아있지 않으면 while문 break

    print('#{} {}'.format(tc, len(string)))