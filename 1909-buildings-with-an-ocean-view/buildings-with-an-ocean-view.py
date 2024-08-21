class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        i = n-1
        hasview = []
        current_max = -float('inf')
        while i>=0:
            if heights[i]>current_max:
                hasview.append(i)
                current_max = heights[i]
            i-=1

        return [hasview[-1-i] for i in range(len(hasview))]
