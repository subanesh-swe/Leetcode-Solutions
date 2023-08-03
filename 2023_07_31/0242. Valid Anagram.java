//242. Valid Anagram

//https://leetcode.com/problems/valid-anagram/

class Solution {
    public boolean isAnagram(String s, String t) {
        int [] ascii = new int[26];
        int s_len = 0, t_len = 0;
        for(char ch : s.toCharArray()){
            ascii[ch-'a']++;
            s_len++;
        }
        for(char ch : t.toCharArray()){
            if(ascii[ch-'a']-- < 1)     return false;
            t_len++;
        }
        if(s_len != t_len)  return false;
        return true;
    }
}