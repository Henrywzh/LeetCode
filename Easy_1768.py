# Merge Strings Alternatively

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0
        n, m = len(word1), len(word2)
        while i < min(n, m):
            res += word1[i] + word2[i]
            i += 1

        if n < m:  # word1 shorter than word2
            res += word2[n:]
        elif n > m:
            res += word1[m:]

        return res