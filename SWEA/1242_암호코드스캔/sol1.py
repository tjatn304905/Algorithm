import sys
sys.stdin = open('sample_input.txt')

# 암호코드 정보:
codeinfo = [
    [3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2],
    [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]
]

# 16진수를 2진수로
six_to_two = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 코드 입력받기
    codes = [list(input()) for _ in range(N)]

    # 해독하지 않은 코드 담는 리스트
    encrypt = []

    # 암호가 들어있는 코드 색출해서 encrypt에 담기
    for code in codes:
        for i in range(len(code)):
            if code[i] != '0' and code not in encrypt:
                encrypt.append(code)
    print('encrypt', encrypt)

    # 코드중에서 암호만 잘라내기
    new_encrypt = []
    for elem in encrypt:
        idx = 0
        while idx < len(elem):
            if elem[idx] == '0':
                idx += 1
            else:
                count = 1
                while elem[idx+count] != '0':
                    count += 1
                new_encrypt.append(elem[idx:idx+count])
                idx += count
    print('new_encrypt', new_encrypt)
    print('length_of new_encrypt', len(new_encrypt))

    # 암호화된 숫자 패스워드로 변환
    encrypt_password = []
    for elem in new_encrypt:
        string_password = ''
        for i in range(len(elem)):
            string_password += six_to_two[elem[i]]

        # 처음과 마지막이 1로 끝나게 만들기
        while string_password[-1] == '0' or string_password[0] == '0':
            if string_password[-1] == '0':
                string_password = string_password[:-1]
            if string_password[0] == '0':
                string_password = string_password[1:]

        # 56의 배수가 되게하기(앞에 0 붙여주기)
        length = len(string_password) // 56
        while len(string_password) < 56 * (length+1):
            string_password = '0' + string_password
        encrypt_password.append(string_password)

    # print('encrypt_password', encrypt_password)
    # for i in range(len(encrypt_password)):
    #     print('length', len(encrypt_password[i]))

    # 연속으로 나오는 0과 1의 개수를 뽑아서 리스트로 만들기
    half_decrypted = []
    count = 1
    for elem in encrypt_password:
        for i in range(1, len(elem)):
            if elem[i] == elem[i-1]:
                count += 1
                if i == len(elem) - 1:
                    half_decrypted.append(count)
            else:
                half_decrypted.append(count)
                count = 1
                if i == len(elem) - 1:
                    half_decrypted.append(count)
    # print('half_decrypted', half_decrypted)

    # 이 암호의 길이가 32의 배수인 경우, 모두 그 배수로 나눠주기
    n = len(half_decrypted) // 32
    if n > 1:
        for elem in half_decrypted:
            elem = elem // n

    # 숫자로 변환하기
    # 4개씩 슬라이스 하면서, 암호코드 정보가 가르키는 인덱스로 변환
    decrypted_password = []
    for i in range(0, len(half_decrypted), 4):
        for idx in range(len(codeinfo)):
            if codeinfo[idx] == half_decrypted[i:i+4]:
                decrypted_password.append(idx)
    print('decrypted_password', decrypted_password)

    # 적법한 암호인지 판별하기
    total = 0
    for i in range(len(decrypted_password)):
        if i % 2:
            total += decrypted_password[i]
        else:
            total += 3 * decrypted_password[i]
    if total % 10 == 0:
        print('#{} {}'.format(tc, sum(decrypted_password)))
    else:
        print('#{} {}'.format(tc, 0))


