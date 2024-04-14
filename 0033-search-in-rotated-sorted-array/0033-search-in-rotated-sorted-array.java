class Solution {
    public int search(int[] nums, int target) {
        // for elements in range(length of array)
        for(int i = 0; i < nums.length; i++){
        // if element is equal to target then return the index i
            if (target == nums[i]){
                return i;
            }
        }
        // if element is not matched then return -1
        return -1;
    }
}