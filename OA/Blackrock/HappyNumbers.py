"""
Goal:
Given a positive integer N, determine if it’s a happy number.
A happy number eventually reaches 1 when repeatedly replaced
by the sum of the squares of its digits.
If it loops without reaching 1, it’s unhappy.

Input format:
- Each line contains a single integer N.
- Input ends at EOF.

Output format:
- For each integer: 1 if happy, 0 if unhappy.

Input:
1
7
22

Output:
1
1
0
"""


not_happy = set()

def is_happy(n: str):
    curr = int(n)
    seen = set()

    while curr != 1:
        if curr in seen:  # cycle detected → unhappy
            return False

        seen.add(curr)
        curr = sum(int(d) ** 2 for d in str(curr))

    return True


test = [1, 7, 22, 99994599]

for t in test:
    print(is_happy(str(t)))