class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish_time = 0
        waiting_time = 0
        for arrival, time in customers:
            if finish_time <= arrival:
                finish_time = arrival + time
                waiting_time += time
            else:
                finish_time = finish_time + time
                waiting_time += finish_time - arrival

        return float(waiting_time)/len(customers)

        