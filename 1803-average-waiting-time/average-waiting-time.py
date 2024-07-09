class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish_time = 0
        waiting_time = 0
        for customer in customers:
            if finish_time <= customer[0]:
                finish_time = customer[0] + customer[1]
                waiting_time += customer[1]
            else:
                finish_time = finish_time + customer[1]
                waiting_time += finish_time - customer[0]

        return float(waiting_time)/len(customers)

        