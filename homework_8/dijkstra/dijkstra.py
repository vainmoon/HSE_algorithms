import heapq


def dijkstra(graph, start):
    d = {v: float("inf") for v in graph}
    d[start] = 0

    heap = [(0, start)]
    visited = set()

    while heap:
        dist, u = heapq.heappop(heap)

        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph[u].items():
            new_dist = dist + weight
            if new_dist < d[v]:
                d[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return d
