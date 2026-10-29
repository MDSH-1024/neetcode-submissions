


class Solution {
    
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int length = 0;
        int max_length = 0;
        Set<Character> seen = new HashSet<>();

        for(int i = 0;i < s.length();i++){
            while(seen.contains(s.charAt(i))){
                seen.remove(s.charAt(left));
                left += 1;
            }

            seen.add(s.charAt(i));
            length = i - left + 1;
            max_length = Math.max(max_length, length);

        }
        
        return max_length;
    }
}
