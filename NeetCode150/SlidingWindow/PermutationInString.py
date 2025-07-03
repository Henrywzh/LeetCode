class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = dict()

        for c in s1:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1

        l = 0
        for r in range(len(s2)):
            if s2[r] in count:
                count[s2[r]] -= 1

            while r - l + 1 > len(s1):
                if s2[l] in count:
                    count[s2[l]] += 1
                l += 1

            if all(v == 0 for v in count.values()):
                return True

        return False

