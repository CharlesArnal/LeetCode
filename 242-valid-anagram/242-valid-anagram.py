class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stacks = {}
        for character in s:
            if character in stacks:
                stacks[character] +=1
            else:
                stacks[character] =1
        for character in t:
            if character in stacks:
                stacks[character] -=1
            else:
                return False
        for char_key in stacks:
            if stacks[char_key] !=0:
                return False
        return True
        