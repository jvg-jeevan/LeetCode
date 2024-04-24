class Solution {
    public int tribonacci(int n) {
// similar to fibo if n value < 2 then return 1 and if n = 0 then return 0
        if(n == 0)
            return 0;
        else if (n < 3)
            return 1;

        else{
// initialize n0, n1, n2
            int n0 = 0, n1 = 1, n2 = 1;
            for (int i=3; i<=n;i++){
// Tn+3 = Tn + Tn+1 + Tn+2
                int temp = n0 + n1 + n2;
// assign the new values of n0, n1, n2
                n0 = n1;
                n1 = n2;
                n2 = temp;
            }
// return the value for n3 
            return n2;
        }
        
    }
}