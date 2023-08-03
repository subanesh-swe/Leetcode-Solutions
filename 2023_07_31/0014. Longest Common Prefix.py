#14. Longest Common Prefix

#https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        milen,miind=202,0
        for i in range(len(strs)):
            presentlen=len(strs[i])
            if milen>presentlen:
                milen=presentlen
                miind=i
        st1=str(strs[miind])
        for st in strs:
            l1=len(st1)
            l2=len(st)
            newlen=l1
            for i in range(min(l1,l2)):
                if st1[i]!=st[i]:
                    newlen=i
                    break
            st1=st1[0:newlen]
        return st1