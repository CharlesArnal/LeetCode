class Solution:
    def romanToInt(self, s: str) -> int:
        translator = {"I":1,"V":5,"X":10,"L":50, "C":100, "D":500, "M" :1000}
        n = len(s)
        if n==0:
            return 0
        total = 0
        for i, char in enumerate(s):
            if i==n-1:
                total += translator[char]
            else:
                if translator[char]>= translator[s[i+1]]:
                    total+= translator[char]
                else:
                    total-= translator[char]
                

        return total
        # if n==0:
        #     return 0
        # elif n == 1:
        #     return translator[s]
        # else:
        #     if translator[s[0]] >= translator[s[1]]:
        #         return translator[s[0]] + self.romanToInt(s[1:])
        #     if  translator[s[0]] < translator[s[1]]:
        #         return translator[s[1]]-translator[s[0]] + self.romanToInt(s[2:])