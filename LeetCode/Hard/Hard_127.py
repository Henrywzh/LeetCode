from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        q = deque([(beginWord, 1)])  # (word, steps)
        chars = [chr(ord('a') + i) for i in range(26)]
        visited = {beginWord}

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for c in chars:
                    if c == word[i]:
                        continue
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordList and newWord not in visited:
                        q.append((newWord, steps + 1))
                        visited.add(newWord)

        return 0
