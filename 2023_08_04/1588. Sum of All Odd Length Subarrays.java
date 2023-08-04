// 1588. Sum of All Odd Length Subarrays.java

// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int sum = 0;
        for(int i = 0; i < arr.length; i++) {
            // Add to the sum for each contribution of the arr[i]
            sum += (((i + 1) * (arr.length - i) + 1) / 2) * arr[i];
        }
        return sum;
    }
}