class Solution {
    public boolean isPowerOfFour(int n) {
        // while n > 0
        while(n>0){
            // if n becomes 1 then n is power of 4
            if (n==1)   return true;
            // if remainder on dividing by 4 is not 1 then not a pow of 4
            else if (n%4 != 0)  break;
            // divide n by 4
            n /= 4;
        }
        // return false if not pow of 4
        return false; 
    }
}