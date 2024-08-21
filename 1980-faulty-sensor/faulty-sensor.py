class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        i = 0 
        n = len(sensor1)
        while i<n and sensor1[i] == sensor2[i]:
            i+=1
        # print(i)
        if i >= n-1:
            return -1
        else:
            pos1 = False
            pos2 = False
            # print(sensor1[i:-2])
            # print(sensor2[i+1:])
            if sensor1[i:-1] == sensor2[i+1:]:
                pos1 = True
            if sensor2[i:-1] == sensor1[i+1:]:
                pos2 = True
            print(pos1)
            print(pos2)
            if pos1 and pos2:
                return -1
            else:
                return 1 if pos1 else 2