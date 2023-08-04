// 2574. Left and Right Sum Differences.java

// https://leetcode.com/problems/left-and-right-sum-differences/

class Solution {
    public int[] leftRigthDifference(int[] nums) {
        int i,li=0,lsum=0,rsum=0,ln = nums.length;
        int[] ans = new int[ln];
        for(i = 0; i < ln ; i++){
            ans[li++] = lsum;
            //System.out.print(lsum+" ");
            lsum += nums[i];
        }
        System.out.println();
        for(i = ln-1; i >= 0 ; i--){
            ans[i] = Math.abs(ans[i] - rsum);
            //System.out.print(rsum+" ");
            rsum += nums[i];
        }
        return ans;
    }
}