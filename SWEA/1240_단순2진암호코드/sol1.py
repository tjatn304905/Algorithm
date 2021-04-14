import sys
sys.stdin = open('input.txt')

# 암호코드 정보:
codeinfo = [
    [3, 2, 1, 1],
    [2, 2, 2, 1],
    [2, 1, 2, 2],
    [1, 4, 1, 1],
    [1, 1, 3, 2],
    [1, 2, 3, 1],
    [1, 1, 1, 4],
    [1, 3, 1, 2],
    [1, 2, 1, 3],
    [3, 1, 1, 2]
]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 코드 입력받기
    codes = [list(input()) for _ in range(N)]

    # 암호가 들어있는 코드 색출하기
    for code in codes:
        if '1' in code:
            password = code
            break

    # 암호코드의 마지막은 1로 끝난다.
    # 뒤에서 첫번째 1을 찾고, 56개를 슬라이싱
    for idx in range(len(password)-1, -1, -1):
        if password[idx] == '1':
            password = password[idx-55:idx+1]
            break

    # 연속으로 나오는 0과 1의 개수를 뽑아서 리스트로 만들기
    pass_code = []
    count = 1
    for i in range(1, 56):
        if password[i] == password[i-1]:
            count += 1
            if i == 55:
                pass_code.append(count)
        else:
            pass_code.append(count)
            count = 1
            if i == 55:
                pass_code.append(count)

    # 숫자로 변환하기
    # 4개씩 슬라이스 하면서, 암호코드 정보가 가르키는 인덱스로 변환
    numbers = []
    for i in range(0, 32, 4):
        for idx in range(len(codeinfo)):
            if codeinfo[idx] == pass_code[i:i+4]:
                numbers.append(idx)

    # 적법한 암호인지 판별하기
    total = 0
    for i in range(len(numbers)):
        if i % 2:
            total += numbers[i]
        else:
            total += 3 * numbers[i]
    if total % 10 == 0:
        print('#{} {}'.format(tc, sum(numbers)))
    else:
        print('#{} {}'.format(tc, 0))


