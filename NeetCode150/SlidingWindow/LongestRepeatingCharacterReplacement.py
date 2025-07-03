class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        chrCnt = dict()
        maxFreq = 0

        for r in range(len(s)):
            chrCnt[s[r]] = 1 + chrCnt.get(s[r], 0)
            maxFreq = max(chrCnt[s[r]], maxFreq)

            while r - l + 1 - maxFreq > k:
                chrCnt[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
