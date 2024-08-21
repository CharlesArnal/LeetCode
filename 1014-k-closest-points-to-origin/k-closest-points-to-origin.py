
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k_smallest = [[float('inf'),float('inf')] for i in range(k)]
        # for p in points:
        #     if p[0]**2+p[1]**2 < k_smallest[-1][0]**2 + k_smallest[-1][1]**2:
        #         k_smallest.pop()
        #         k_smallest.append(p)
        #         k_smallest.sort(key = lambda point : point[0]**2 + point[1]**2)
        # return k_smallest

        enriched_points = []
        for point in points:
            enriched_points.append((point,point[0]**2 + point[1]**2 ))
        enriched_points.sort(key = lambda p : p[1])
        return [p[0] for p in enriched_points[:k]]

        