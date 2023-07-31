#125. Valid Palindrome

#https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''
        for ch in s:
            ch = ch.lower()
            if ord('a')<=ord(ch)<=ord('z') or ch in '1234567890':
                st+=ch
        return True if st==st[::-1] else False