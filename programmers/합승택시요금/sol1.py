def solution(n, s, a, b, fares):
    # 간선을 나타내는 2차원 리스트
    roads = [[] for _ in range(n + 1)]

    # 간선에 양쪽 노드와 비용 정보를 담아줌
    for fare in fares:
        roads[fare[0]].append((fare[1], fare[2]))
        roads[fare[1]].append((fare[0], fare[2]))

    # 이미 쓰인 노드 리스트
    U = [s]

    # 시작 노드로부터 각 노드별로 가는 비용
    D = [0] * (n + 1)
    for elem in roads[s]:
        D[elem[0]] = elem[1]

    minimum = 100000
    # 시작 노드로부터 비용이 최소인 점
    for i in range(len(D)):
        if D[i] and D[i] < minimum:
            minumum = i
    print(minimum)

    answer = 0
    return answer









n, s, a, b, fares = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
solution(n, s, a, b, fares)