# 1572. Matrix Diagonal Sum

# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ln = len(mat)
        sm = 0
        for i in range(ln):
            sm += (mat[i][i] + mat[ln-i-1][i])
        if ln & 1:
            sm -= mat[ln//2][ln//2]
        return sm