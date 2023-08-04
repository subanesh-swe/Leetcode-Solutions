# 2485. Find the Pivot Integer.py

# https://leetcode.com/problems/find-the-pivot-integer/

class Solution:
    def pivotInteger(self, n: int) -> int:
        y = (n * n + n) // 2
        x = int(math.sqrt(y))
        if x * x == y:
            return x 
        return -1