from collections import deque 

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starting_points = deque(sorted(intervals, key = lambda interval : interval[0]))
        # ending_points = intervals.sort(key = lambda interval : interval[1])
        all_points = sorted([inter[0] for inter in intervals] + [inter[1] for inter in intervals])
        currently_active = []
        max_n = 0
        cur = 0
        for point in all_points:
            if point in currently_active:
                currently_active.pop()
                cur -= 1 
            elif point == starting_points[0][0]:
                cur+=1
                currently_active.append(starting_points[0][1])
                currently_active.sort(reverse = True)
                starting_points.popleft()
                max_n = max(max_n,cur)
            #print(f"point {point} cur {cur}")
        return max_n
            


        