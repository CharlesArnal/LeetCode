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
        counter = 0
        while len(to_be_checked) != 0:
            counter+=1
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
        neighbors = []
        if pos[0]>0:
            neighbors += [(pos[0]-1,pos[1])]
        if pos[0]<len(grid)-1:
            neighbors += [(pos[0]+1,pos[1])]
        if pos[1]>0:
            neighbors += [(pos[0],pos[1]-1)]
        if pos[1]<len(grid[0])-1:
            neighbors += [(pos[0],pos[1]+1)]
        for neighbor in neighbors:
            if grid[neighbor[0]][neighbor[1]] == "1":
                ones.add(neighbor)
        # print(f"---\n pos {pos}")
        # print(f"grid \n{np.array(grid)}")
        # print(f"ones {ones}")
        return ones


# print("\n---- Test")
# my_sol = Solution()
# sol = my_sol.numIslands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]])
# print(f"sol {sol}")
