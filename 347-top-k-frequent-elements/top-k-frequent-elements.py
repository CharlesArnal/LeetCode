class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = []
        counts = dict()
        for element in nums:
            if element in counts:
                counts[element]+=1
            else:
                elements.append(element)
                counts[element]=1
        f = lambda element : counts[element]
        elements.sort(key = f, reverse = True)
        return elements[:k]