from collections import deque


def topological_sort(vertices, relations):
    adjacency = {v: [] for v in vertices}
    indegree = {v: 0 for v in vertices}

    for a, b in relations:
        if a == b:
            continue
        adjacency[a].append(b)
        indegree[b] += 1

    queue = deque(v for v in vertices if indegree[v] == 0)
    result = []

    while queue:
        v = queue.popleft()
        result.append(v)
        for u in adjacency[v]:
            indegree[u] -= 1
            if indegree[u] == 0:
                queue.append(u)

    if len(result) != len(vertices):
        raise ValueError("Отношение содержит цикл.")

    return result


if __name__ == "__main__":
    A = ["a", "b", "c", "d", "e", "f"]
    relations = [
        ("a", "c"),
        ("b", "c"),
        ("b", "d"),
        ("c", "e"),
        ("d", "e"),
        ("e", "f"),
    ]
    linear_order = topological_sort(A, relations)
    print("Линейный порядок:", " < ".join(linear_order))
