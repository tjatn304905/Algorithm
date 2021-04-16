import sys
sys.stdin = open('sample_input.txt')


def solution():
    numbers = []

    # i는 1과 0을 바꿔줄 인덱스
    for i in range(len(two)):
        number = 0
        for j in range(len(two)):
            if i == j:
                # -1 한다음 절대값 씌워서 숫자 바꿔주기
                number += abs(int(two[j]) - 1) * (2 ** (len(two) - j - 1))
            else:
                number += int(two[j]) * (2 ** (len(two) - j - 1))
        numbers.append(number)

    new_numbers = []

    # 리스트에 있는 숫자들을 3진수로 바꿔주기
    for number in numbers:
        new_number = 0
        for i in range(40, -1, -1):
            if number >= 3**i * 2:
                number -= 3**i * 2
                new_number += 2 * (10**i)
            elif number >= 3**i:
                number -= 3**i
                new_number += 1 * (10**i)
        new_numbers.append(new_number)

    for idx in range(len(new_numbers)):
        elem = str(new_numbers[idx])
        count = 0
        if len(elem) == len(three):
            for i in range(len(elem)):
                if elem[i] != three[i]:
                    count += 1
            if count == 1:
                return numbers[idx]


T = int(input())

for tc in range(1, T+1):
    two = input()
    three = input()

    print('#{} {}'.format(tc, solution()))



