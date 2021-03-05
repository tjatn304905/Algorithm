import sys
sys.stdin = open('sample_input.txt')

# 팀을 나누는 함수
def divide(N):
    teams = [N] + [0] * (N-1)
    while True:
        new_teams = [0] * N
        # 팀 나누기
        for idx in range(len(teams)):
            if teams[idx] > 2:
                new_teams[idx * 2] = (teams[idx] + 1) // 2
                new_teams[idx * 2 + 1] = teams[idx] - (teams[idx] + 1) // 2
        for idx in range(len(new_teams)):
            teams[idx] = new_teams[idx]
        print(teams, tc)
        # while 종료조건
        cnt = 0
        for team in teams:
            if team > 2:
                cnt = 1
        if cnt == 0:
            return teams

def game(tournament, teams):

    for team in teams:
        if team == 2:


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    teams = divide(N)
    tournament = []
    for idx in range(N):
        tournament.append([cards[idx], idx + 1])

    print('#{} {}'.format(tc, game(tournament, teams)))
