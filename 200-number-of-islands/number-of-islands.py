import numpy as np
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        # print("Start")
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =="1":
                    num+= 1
                    #print(f"grid \n{np.array(grid)}")
                    self.erase_connected_component(grid,(i,j))
                    
        return num

    def erase_connected_component(self, grid, pos):
        #print(f"pos {pos}")
        to_be_checked = {pos}
        while len(to_be_checked) != 0:
            # print(f"grid inside loop iteration {counter} \n{grid}")
            # print(f" to be checked {to_be_checked}")
            cur = to_be_checked.pop()
            # print(f"cur {cur}")
            ones = self.ones_in_neighbors(grid, cur)
            # print(f"ones {ones}")
            to_be_checked = to_be_checked | ones
            grid[cur[0]][cur[1]] = "-1"
            

    def ones_in_neighbors(self, grid, pos):
        ones = set()
        if pos[0]>0 and grid[pos[0]-1][pos[1]] == "1":
            ones.add((pos[0]-1,pos[1]))
        if pos[0]<len(grid)-1 and grid[pos[0]+1][pos[1]] == "1":
            ones.add((pos[0]+1,pos[1]))
        if pos[1]>0 and grid[pos[0]][pos[1]-1] == "1":
            ones.add((pos[0],pos[1]-1))
        if pos[1]<len(grid[0])-1 and grid[pos[0]][pos[1]+1] == "1":
            ones.add((pos[0],pos[1] +1))       
        return ones


# print("\n---- Test")
# my_sol = Solution()
# sol = my_sol.numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]])
# print(f"sol {sol}")
