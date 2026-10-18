class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word_1 = {}
        word_2 = {}
        for sym in s:
            if sym in word_1:
                word_1[sym] += 1
            else:
                word_1[sym] = 1
        for sym in t:
            if sym in word_2:
                word_2[sym] += 1
            else:
                word_2[sym] = 1
        if word_1 != word_2:
            return False
        return True