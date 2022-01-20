class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=-1
        for letter in s:
            n+=1
            while n<len(t) and t[n]!=letter:
                n+=1
            if n>= len(t):
                return False
        return True