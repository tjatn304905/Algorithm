board = [[1,0,0,3],
         [2,0,0,0],
         [0,0,0,2],
         [3,0,1,0]]
r = 1
c = 0


def solution(board, r, c):
    cards = [[] for _ in range(7)]  # 카드 위치의 정보를 담고 있는 리스트(최대 숫자 6까지의 카드)
    print(cards)

    # board를 순회하면서 카드를 찾기
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_number = board[i][j]  # 그 위치의 숫자가 곧 카드종류임
                cards[card_number].append((i, j))  # 위에서 찾은 정보를 cards 내의 맞는 위치에 추가

    # print(cards)

    current = (r, c)  # 현재 커서의 위치






    answer = 0
    return answer


solution(board, r, c)
