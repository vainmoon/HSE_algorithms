from collections import deque


def get_graph_components(graph):
    visited = set()
    component_list = []

    for start_v in graph:
        if start_v not in visited:
            component = []
            queue = deque([start_v])
            visited.add(start_v)
            while queue:
                v = queue.popleft()
                component.append(v)
                for neighbor_v in graph[v]:
                    if neighbor_v not in visited:
                        visited.add(neighbor_v)
                        queue.append(neighbor_v)

            component_list.append(component)

    return component_list
