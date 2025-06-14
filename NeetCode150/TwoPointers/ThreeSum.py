from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ns = sorted(nums)  # O(nlogn)
        # so ns[k] + ns[j] = -ns[i], i j k distinct!
        # find all twoSum s.t. equals to one of num in nums

        res = []
        for i in range(len(ns)):
            j, k = i + 1, len(ns) - 1
            while j < k:
                if ns[j] + ns[k] > -ns[i]:
                    k -= 1
                elif ns[j] + ns[k] < -ns[i]:
                    j += 1
                else:
                    three_sum = [ns[i], ns[j], ns[k]]
                    if three_sum in res:  # break if duplicated
                        break

                    res.append(three_sum)
                    j += 1  # move on to next
                    k -= 1  # move on to next

                    # if prev left == curr left, still duplicates move
                    while ns[j] == ns[j - 1] and j < k:
                        j += 1

        return res

