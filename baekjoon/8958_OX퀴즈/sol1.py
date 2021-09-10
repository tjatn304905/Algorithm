# https://www.acmicpc.net/problem/8958

# 테스트 케이스의 개수를 입력받는다.
num = int(input())
# 그 개수만큼 테스트 케이스를 입력받는다.
for i in range(num):
    test_case = input()
    count = 0
    score = 0
    # 테스트 케이스의 길이만큼 순회하면서
    for i in range(len(test_case)):
        # 문자열이 O 라면
        if test_case[i] == 'O':
            # count 에 1을 더해주고 score에 합산
            count += 1
            score += count
        # 문자열이 X 라면
        else:
            # count를 초기화
            count = 0
    # score를 출력
    print(score)