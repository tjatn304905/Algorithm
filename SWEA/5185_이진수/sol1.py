import sys
sys.stdin = open('sample_input.txt')

def change(sixteen):
    # 0에서 15까지의 수를 2진수로 나타낸 딕셔너리
    two = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }

    result = ''

    for number in sixteen:
        result += two[number]

    return result



T = int(input())

for tc in range(1,T+1):
    N, sixteen = input().split()

    print('#{} {}'.format(tc, change(sixteen)))
