class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        for index, character in enumerate(y):
            if character != y[-index-1]:
                return False
        return True