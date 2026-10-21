class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letterCounts = [0] * 26

        for ind in range(len(s)):
            letterCounts[ord(s[ind]) - 97] += 1
            letterCounts[ord(t[ind]) - 97] -= 1
        
        for val in letterCounts:
            if val != 0:
                return False
        
        return True

    
        
        
        