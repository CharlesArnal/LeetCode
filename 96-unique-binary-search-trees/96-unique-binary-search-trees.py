class Solution:
    def numTrees(self, n: int) -> int:
        num = [1,1] # 0 node and 1 node
        for i in range(2,n+1):
            num.append(sum([num[j-1]*num[i-j] for j in range(1,i+1)]))
        return num[n]
    