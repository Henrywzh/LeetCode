from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        A = ['A', 'C', 'G', 'T']

        if endGene not in bank:
            return -1

        visited = {startGene}
        q = deque([(startGene, 0)])  # (gene, steps)

        while q:
            gene, steps = q.popleft()
            if gene == endGene:
                return steps

            for i in range(len(gene)):
                for g in A:
                    newGene = gene[:i] + g + gene[i + 1:]
                    if newGene in bank and newGene not in visited:
                        q.append((newGene, steps + 1))
                        visited.add(newGene)

        return -1
