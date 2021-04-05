def zoo(N, animals):
    # 먼저 sort로 오름차순으로 정렬
    animals.sort()

    # 가장 큰 숫자 + 1로 리스트를 만듦
    rabbits = [[] for _ in range(animals[-1] + 1)]
    # 동물 수에서 위의 길이를 뺀 리스트를 만듦
    cats = [[] for _ in range(N - animals[-1] - 1)]

    print(rabbits)
    print(cats)


N = int(input())
animals = list(map(int, input().split()))

zoo(N, animals)
