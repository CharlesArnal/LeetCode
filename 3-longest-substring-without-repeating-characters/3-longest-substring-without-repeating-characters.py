class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        up = 0
        curr_s = set()
        L = 0
        for char in s:
            while up<len(s) and s[up] not in curr_s:
                up+=1
                curr_s.add(s[up-1])
                L = max(len(curr_s),L)
            if up == len(s):
                return L
            curr_s.remove(char)
        return 0
            