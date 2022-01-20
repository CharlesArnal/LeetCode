class Solution:
    def countBits(self, n: int) -> List[int]:
        myarr = [0]
        while len(myarr) < n + 1:
            myarr +=[x+1 for x in myarr] 
        
        return myarr[0:n+1]

    
