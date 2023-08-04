# 1480. Running Sum of 1d Array

# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sm,ans = 0,[]
        for val in nums:
            sm += val
            ans.append(sm)
        return ans