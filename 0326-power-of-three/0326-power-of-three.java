class Solution {
    public boolean isPowerOfThree(int n) {
        // take while loop for n > 0
        while(n>0){
// if n becomes 1 then n completely divisible by 3 i.e the number is pow (3)
            if (n == 1){
                return true;
            }
    // if n is not divisible by 3 then return break and return False
            else if (n%3 != 0){
                break;
            } 
    // divide n by 3 and assign it to n
            n /= 3;
        }
        return false;
    }
}