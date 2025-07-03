class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = dict()
        for c in t:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1

        l = 0
        res = s[:]
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] -= 1

            while r - l + 1 > len(t):
                if s[l] in count:
                    if count[s[l]] >= 0:
                        break
                    else:
                        count[s[l]] += 1

                l += 1

            if all(v <= 0 for v in count.values()):
                res = min(res, s[l:r + 1], key=len)

        if all(v <= 0 for v in count.values()):
            return res
        else:
            return ""
