class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for c in s:
            if c not in s_map:
                s_map[c] = 1
            else:
                s_map[c] += 1

        for c in t:
            if c not in t_map:
                t_map[c] = 1
            else:
                t_map[c] += 1

        return s_map == t_map
