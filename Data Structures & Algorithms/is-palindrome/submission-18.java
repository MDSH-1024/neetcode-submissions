class Solution {
    public boolean isPalindrome(String s) {
        if(s.length() == 1 || s.length() == 0){
            return true;
        }

        short p1 = 0;
        short p2 = (short) (s.length() - 1);

        while(p1 <= p2){
            
            while(p1 < s.length()  && !Character.isLetterOrDigit(s.charAt(p1))){
                p1 ++;
                
            } 
            while(p2 > 0 && !Character.isLetterOrDigit(s.charAt(p2))){
                p2 --;
            }
            if(p1 > p2){
                    return true;
                }
            if(Character.toLowerCase(s.charAt(p1)) != Character.toLowerCase(s.charAt(p2))){
                return false;
            }
            p1++;
            p2--;
        }

        return true;
    }
}
