class Solution {
    public int singleNumber(int[] nums) {
        // take res as the first number
        int res = nums[0];
        // for every element after 1st element i.e index 1 to last
        for(int i=1; i< nums.length; i++){
// xor of same element results in zero and xor of 0 and number is number
            res ^= nums[i];
// so if number repeats the res becomes zero and after zero xor results in unique element
        }
        return res;
    }
}