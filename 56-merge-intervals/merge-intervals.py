class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])
        all_values = sorted([[start,0] for start in starts]+ [[end,1] for end in ends], key = lambda a: a[0])
        merged = []
        count = 0
        current = None
        for t in all_values:
            if t[1] == 0:
                if count == 0:
                    current = t[0]
                count += 1
            else:
                assert count>=1
                count -=1
                if count == 0:
                    merged += [[current,t[0]]]
        return merged
                    


        