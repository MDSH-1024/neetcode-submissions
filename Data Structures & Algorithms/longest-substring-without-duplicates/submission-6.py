class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length = 0
        left = 0 
        max_length = 0
        

        for i, sym in enumerate(s):
            while sym in seen:
                
                seen.remove(s[left])
                left += 1

                
            seen.add(sym)
            
            length = i - left + 1

            max_length = max(max_length,length)

        return max_length




                
                
