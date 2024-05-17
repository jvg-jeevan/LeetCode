class Solution {
    public int maximumCount(int[] nums) {
// inintialize pos and neg
        int pos = 0;
        int neg = 0;
// if num > 0 increment pos, num < 0 increment neg
        for (int i=0; i<nums.length; i++){
            if (nums[i] < 0) neg++;
            else if (nums[i] > 0) pos++;
        }
// return the max of both
        if (pos >= neg) return pos;
        else return neg;
    }
}