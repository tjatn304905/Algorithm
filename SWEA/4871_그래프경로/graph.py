"""
Graph

Node(Vertex, Vertices): 꼭지점
Edge: 간선

Undirected Graph: 간선에 방향이 없음(양방향 이동 가능)
Directed Graph: 간선에 방향이 있음(단방향 이동만 가능)

V: 6개
E: 5개

for _ in range(E):

"""

V = 6
E = 5

S = 1
G = 6

# 1. Dictionary
g = {
    'A': ['D', 'C'],
    'B': ['C', 'E'],
    'C': [],
    'D': ['F'],
    'E':[],
    'F':[]
}

# 2. Adjacency List(인접 리스트)
g = [
    [], # 0
    [4, 3], # 1
    [3, 5], # 2
    [], # 3
    [6], # 4
    [], # 5
    [] # 6
]

# 3. Adj Matrix(인접 매트릭스)


