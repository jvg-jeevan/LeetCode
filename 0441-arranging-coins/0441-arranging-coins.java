class Solution {
    public int arrangeCoins(int n) {
        // i = rows of coins
        int i = 1;
        while (n >= i){
            // n-i gives the coins to be placed
            n -= i;
            // increment the rows
            i += 1;
        }
// return the rows upto which the coins are placed (i-1) because if the coins are not completely placed
        return i-1;
    }
}