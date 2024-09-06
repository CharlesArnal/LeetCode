import random

class Solution:

    def __init__(self, w: List[int]):
        W = []
        total = 0
        for weight in w:
            total+=weight
            W.append(total)
        self.W = W
        

    def pickIndex(self) -> int:
        r = random.uniform(0,self.W[-1])
        sorted_list = sorted(self.W + [r])
        i = sorted_list.index(r)
        return i

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()