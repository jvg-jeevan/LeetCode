class Solution {
    public int hammingWeight(int n) {
        int res = 0;
        // while n is not zero 
        while(n!=0){
            // if remainder is not zero then increment res
            if (n%2 != 0)
            res += 1;
            // divide the number n by 2
            n = n >> 1; 
        }
        return res;
    }
}