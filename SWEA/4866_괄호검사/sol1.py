import sys
sys.stdin = open('sample_input.txt')

def test(str1):
    test_list = []

    for i in str1:
        if i == '(' or i == '{' or i == '[':
            test_list.append(i)
        elif i == ')':
            if len(test_list) == 0:
                return 0
            elif test_list[-1] == '(':
                test_list.pop()
            else:
                return 0
        elif i == '}':
            if len(test_list) == 0:
                return 0
            elif test_list[-1] == '{':
                test_list.pop()
            else:
                return 0
        elif i == ']':
            if len(test_list) == 0:
                return 0
            elif test_list[-1] == '[':
                test_list.pop()
            else:
                return 0

    if len(test_list) == 0:
        return 1
    else:
        return 0


T = int(input())

for tc in range(1, T+1):
    str1 = input()


    print('#{} {}'.format(tc, test(str1)))
