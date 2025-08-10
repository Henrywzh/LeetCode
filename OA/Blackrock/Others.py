"""
Q3: Cyclic String Indexing
Goal:
Repeat a string cyclically until it reaches length ≥ n, then output the character at position n (1-indexed).

Input format:

First line: string S (non-empty, length ≤ 100).

Second line: integer n (1 ≤ n ≤ 10^6).

Output format:

A single character: the nth character of the infinitely repeated string.
"""

def cyclic_string_indexing(xs: str, n: int) -> str:
    size = len(xs)
    idx = n % size - 1

    return xs[idx]


"""
Q4: Common Elements in Two Lists
Goal:
Given two lists of strings, find the intersection and output them sorted in lexicographical order.

Input format:

First line: space-separated list of strings (list A).

Second line: space-separated list of strings (list B).

Output format:

Space-separated list of common strings in ascending order.

If no common elements, output an empty line.
"""

def common_elements(list1, list2) -> list:
    return sorted(set(list1) & set(list2))


"""
Q6: Department Employee Count
Goal:
Count the number of employees in each department and print the results in alphabetical order of department name.

Input format:

Each line: Name,Department.

Input ends at EOF.

Output format:

One line per department: Department Count (space-separated).
"""

d = """John,Finance\nAlice,Engineering\nBob,Finance"""

def department_employee_count(data):
    data = [data.split(',') for data in data.split('\n')]
    department_count = {}

    for employee, department in data:
        department_count[department] = department_count.get(department, 0) + 1

    return [f'{dep} {department_count[dep]}' for dep in sorted(department_count)]
