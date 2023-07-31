#13. Roman to Integer

#https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        val={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans,i,l=0,0,len(s)
        while i<l:
            v1=val[s[i]]
            if i+1==l:
                ans+=v1
                break
            v2=val[s[i+1]]
            if v1>=v2:
                ans+=v1
                i+=1
            else:
                ans+=(v2-v1)
                i+=2
        return ans
