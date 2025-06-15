from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}

        for string in strs:
            chr_map = [0] * 26
            for c in string:
                chr_map[ord(c) - ord('a')] += 1

            chr_map = ' '.join([str(u) for u in chr_map])

            if chr_map in str_map:
                str_map[chr_map].append(string)
            else:
                str_map[chr_map] = [string]

        return list(str_map.values())


"""
Explanation:
- We need to achieve O(N*M) complexity
- Solve the question in two parts,
1. First make a list of O(26) size to record the freq of each char for each str
2. Then use the list of O(26) as a key in the hash map for grouping
- Make the values into a list
"""
