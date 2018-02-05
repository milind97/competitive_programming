import heapq
from sys import stdin, stdout


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
        self._outgoing[x] = {}
        if self.is_directed():
            self._incoming[x] = {}

    def insert_edge(self, u, v, x=None):
        self._outgoing[u][v] = x
        self._incoming[v][u] = x


t = int(input())
while t:
    t -= 1
    g = Graph()
    n, k, x, m, s = map(int, stdin.readline().split())
    [g.insert_vertex(j) for j in range(1, n + 1)]
    for i in range(m):
        a, b, c = map(int, stdin.readline().split())
        g.insert_edge(a, b, c)
    dist = {}
    for i in range(1, n + 1):
        dist[i] = float('inf')
    ans = [-1]*n
    dist[s] = 0
    h = []
    heapq.heappush(h, (dist[s], s))
    while len(h):
        u = heapq.heappop(h)[1]
        ans[u-1] = dist[u]
        if u <= k:
            l = list(range(1, k + 1))
            l.remove(u)
            l.extend(g.adjacent_vertex(u))
        else:
            l = g.adjacent_vertex(u)
        for v in l:
            if v <= k and u <= k:
                weight = x
            else:
                weight = g.get_edge(u, v)
            if dist[u] + weight < dist[v]:
                if ans[v-1] == -1:
                    dist[v] = dist[u] + weight
                    heapq.heappush(h, (dist[v], v))
    for x in ans:
        stdout.write("%s " % x)
    print()
