"""
Q1: Corporate Ladder (Graph Distance)
Description:
Given a list of employee–manager pairs, find the number of levels between two people in the hierarchy.
If unrelated, return -1.

Key skills: graph building, BFS/DFS, dictionary mapping.

Input:
Susan/Amy
Susan/John
John/Amy

Output:
2
"""

from collections import deque


def corporateLadder(start, end, employees):
    queue = deque()
    graph = {}
    # graph construction, employee points to manager
    for employee, manager in employees:
        graph[employee] = graph.get(employee, []).append(manager)

    visited = set()
    queue.append((start, 0))

    while queue:
        employee, level = queue.popleft()

        for manager in graph[employee]:
            if manager == end:
                return level + 1

            if manager not in visited:
                visited.add(manager)
                queue.append((manager, level + 1))

    return -1
