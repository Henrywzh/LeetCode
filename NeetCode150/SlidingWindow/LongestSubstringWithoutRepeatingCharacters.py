class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, r = 0, 0
        res = 0

        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                charSet.remove(s[l])
                l += 1

        return res

