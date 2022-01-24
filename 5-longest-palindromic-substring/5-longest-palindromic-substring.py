class Solution:
    def longestPalindrome(self, s: str) -> str:
        L_s = ""
        for i in range(0,2*len(s)-1):
            if i%2==0:
                center = int(i/2)
                j=1
                current_s = s[center]
                while center+j<len(s) and center-j>=0:
                    if s[center+j]==s[center-j]:
                        current_s = s[center-j] + current_s + s[center+j]
                    else:
                        break
                    j+=1
                if len(current_s)>len(L_s):
                    L_s = current_s
            else:
                j=0
                current_s = ""
                while (i-1)/2-j>=0 and (i+1)/2+j<len(s):
                    if s[int((i-1)/2)-j] == s[int((i+1)/2)+j]:
                        current_s = s[int((i-1)/2)-j] + current_s + s[int((i+1)/2)+j]
                    else:
                        break
                    j+=1
                if len(current_s)>len(L_s):
                    L_s = current_s
            #print(str(i)+"  "+current_s)
        return L_s