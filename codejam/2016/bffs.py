class Graph:
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edge_weight(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update((secondary_map.values()))
        return result

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def adjacent_vertex(self, u):
        if self.is_directed():
            return list(self._outgoing[u].keys())
        else:
            temp = set(self._outgoing[u].keys())
            temp |= set(self._incoming[u].keys())
            return list(temp)

    def insert_vertex(self, x=None):
        self._outgoing = {j: [] for j in range(1, x+1)}
        if self.is_directed():
            self._incoming = {j: [] for j in range(1, x+1)}

    def insert_edge(self, u, v, x=None):
        self._outgoing[u].append(v)
        self._incoming[v].append(u)


def incoming(vrtx, cnt):
    global temp
    if g._incoming[vrtx] == [] or temp[g._incoming[vrtx][0]] :
        return cnt
    else:
        return max([incoming(x, cnt+1) for x in g._incoming[vrtx]])

t = int(input())
for i in range(1, t+1):
    n = int(input())
    g = Graph(True)
    g.insert_vertex(n)
    ans = []
    stu = list(map(int, input().split()))
    for j in range(1, n+1):
        g.insert_edge(j, stu[j-1])
    for j in range(1, n+1):
        count = 1
        vertex = j
        temp = [False] * (n+1)
        temp[vertex] = True
        while not temp[g._outgoing[vertex][0]]:
            vertex = g._outgoing[vertex][0]
            temp[vertex] = True
            count += 1
        if g._outgoing[vertex][0] != g._outgoing[g._outgoing[vertex][0]][0]:
            aux = incoming(vertex, count)
            if aux == count and g._outgoing[g._outgoing[vertex][0]][0] != g._outgoing[j][0]:
                aux -= 1
            ans.append(aux)
        else:
            ans.append(incoming(vertex, count))
    print("Case #{}: {}".format(i, max(ans)))


