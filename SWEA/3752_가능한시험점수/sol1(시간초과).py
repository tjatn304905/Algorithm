import sys
sys.stdin = open('sample_input.txt')


def solution(new_scores):

    n = len(new_scores)

    possible_scores = []

    for i in range(1<<n): # 부분집합의 개수
        total = 0
        for j in range(n+1): # 원소의 수만큼 비트를 비교
            if i & (1<<j): # i의 j번째 비트가 1이면 총합에 더하기
                total += list(new_scores.keys())[j]
                if total not in possible_scores:
                    possible_scores.append(total)
                # 중복 개수가 1이 넘을때
                if list(new_scores.values())[j] > 1:
                    multiple = total
                    # 중복인 개수까지 더하면서 결과값이 리스트에 없으면 추가
                    for n in range(list(new_scores.values())[j] - 1):
                        multiple += list(new_scores.keys())[j]
                        if multiple not in possible_scores:
                            possible_scores.append(multiple)

    return len(possible_scores) + 1 # 공집합일 경우도 포함


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))

    # 점수, 중복 개수를 포함한 딕셔너리
    new_scores = {}
    for score in scores:
        if score in new_scores.keys():
            new_scores[score] += 1
        else:
            new_scores[score] = 1

    print('#{} {}'.format(tc, solution(new_scores)))
