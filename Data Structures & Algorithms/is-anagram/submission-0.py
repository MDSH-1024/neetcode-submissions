class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_1 = sorted(s)
        word_2 = sorted(t)

        if word_1 == word_2:
            return True
        return False