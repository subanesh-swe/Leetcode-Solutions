// 1732. Find the Highest Altitude

// https://leetcode.com/problems/find-the-highest-altitude/

class Solution {
    public int largestAltitude(int[] gain) {
        int heighest = 0, preSum = 0;
        for(int i = 0 ; i < gain.length; i++) {
            preSum += gain[i];
            if(preSum > heighest){ heighest = preSum; }
        }
        return heighest;
    }
}