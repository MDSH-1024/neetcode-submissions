class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        
        key_1 = {}
        for i in s1:
            key_1[i] = key_1.get(i, 0) + 1
        
        key_2 = {}
        for i in range(0, len(s1)):
            key_2[s2[i]] = key_2.get(s2[i], 0) + 1

        for right in range(len(s1), len(s2)):
            left = right - len(s1)
            
            if key_1 == key_2:
                return True
            
            key_2[s2[left]] -= 1
            if key_2[s2[left]] == 0:
                del key_2[s2[left]]

            key_2[s2[right]] = key_2.get(s2[right], 0) + 1
        
        if key_1 == key_2:
                return True

        return False
                



            


