class Solution {
    public int addDigits(int number) {
        int sumOf = 0;
        int rem = 1;
        int length = String.valueOf(number).length();
        for(int i = 0; i < length; i++){
            rem = number % 10;
            sumOf += rem;
            number /= 10;
        }
        if(String.valueOf(sumOf).length() > 1){
            return addDigits(sumOf);
        }
        return sumOf;
    }
}