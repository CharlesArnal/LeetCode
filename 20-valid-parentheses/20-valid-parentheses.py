class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        conversion = {")":"(","]":"[","}":"{"}
        for char in s:
            if char not in conversion:
                my_stack.append(char)
            elif len(my_stack)!=0 and my_stack[-1] == conversion[char]:
                my_stack.pop()
            else:
                return False
        if len(my_stack) != 0:
            return False
        return True

    