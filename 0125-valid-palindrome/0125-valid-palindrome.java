class Solution {
    public boolean isPalindrome(String s) {
        if(s == " "){
            return true;
        }

        // s = s.replaceAll(" ", "");
        // s = s.replaceAll(",", "");
        // s = s.replaceAll(":", "");
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        s = s.toLowerCase();
        System.out.println(s);
        StringBuilder sb = new StringBuilder(s);
        if(s.equals(sb.reverse().toString())){
            return true;
        }
        else{
            return false; 
        }
    }
}