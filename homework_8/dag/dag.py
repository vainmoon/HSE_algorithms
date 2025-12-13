def find_cycle(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in graph}
    parent = {}
    cycle = []

    def dfs(v):
        nonlocal cycle
        color[v] = GRAY

        for u in graph[v]:
            if color[u] == WHITE:
                parent[u] = v
                if dfs(u):
                    return True
            elif color[u] == GRAY:
                cycle.append(u)
                cur = v
                while cur != u:
                    cycle.append(cur)
                    cur = parent[cur]
                cycle.append(u)
                cycle.reverse()
                return True

        color[v] = BLACK
        return False

    for v in graph:
        if color[v] == WHITE:
            parent[v] = None
            if dfs(v):
                return cycle

    return None


def get_topological_sort(graph):
    visited = set()
    order = []

    def dfs(u):
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                dfs(v)
        order.append(u)

    for v in graph.keys():
        if v not in visited:
            dfs(v)

    order.reverse()
    return order


def dag(graph):
    cycle = find_cycle(graph)
    if cycle:
        return cycle
    else:
        return get_topological_sort(graph)
