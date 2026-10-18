class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        breackets = {"(" : ")", "{" : "}" , "[" : "]"}

        for i in s:
            if i in breackets:
                seen.append(breackets[i])
            
            if not seen :
                return False


            if i in breackets.values():
                if i == seen[-1]:
                    seen.pop(-1)
                else:
                    return False
        if seen:
            return False
        return True