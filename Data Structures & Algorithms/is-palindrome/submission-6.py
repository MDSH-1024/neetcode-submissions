class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = []
        for char in s:
            if char.isalpha() or char.isalnum():
                s_new.append(char.lower())
        
        
        
        p1 = 0
        p2 = len(s_new) - 1

        while p1 <= p2:
            if s_new[p1] != s_new[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True