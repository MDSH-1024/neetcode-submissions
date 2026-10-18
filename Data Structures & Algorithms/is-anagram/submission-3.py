class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def counter(text: str) -> dict:
            word = {}
            for sym in text:
                if sym in word:
                    word[sym] += 1
                else:
                    word[sym] = 1
            return word
        if counter(s) != counter(t):
            return False
        return True