class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            neg = True
            x_s = str(x)[1:]
        else:
            neg= False
            x_s = str(x)
        x_s = x_s[::-1]
        if neg:
            bound = str(2**31)
        else:
            bound = str(2**31 -1)
        if len(x_s)>len(bound):
            return 0
        elif len(x_s) == len(bound):
            for index, digit in enumerate(x_s):
                if int(digit)>int(bound[index]):
                    return 0
                elif int(digit)<int(bound[index]):
                    break
        if neg:
            return -1*int(x_s)
        else:
            return int(x_s)
    
my_sol = Solution()
my_sol.reverse(-2147483412)