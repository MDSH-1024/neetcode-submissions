class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        length = 0
        count = {}
        max_rep = 0

        for right,ch in enumerate(s):

            count[ch] = count.get(ch,0) + 1

            max_rep = max(count.values())

            if right - left + 1 - max_rep > k:
                count[s[left]] -= 1
                left += 1
            else:
                length = max(length, right - left + 1)
        

        return length

