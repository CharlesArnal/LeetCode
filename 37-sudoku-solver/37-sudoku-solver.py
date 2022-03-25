import copy

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        hypotheses = []
        initial_undetermined_entries = [[i,j] for i in range(9) for j in range(9) if board[i][j]=="."]
        valid, solved_board = self.solve(board,initial_undetermined_entries)
        for i in range(9):
            for j in range(9):
                board[i][j] = solved_board[i][j]
        
        
        
    def solve(self,old_board,received_undetermined_entries):
        # returns whether there is a valid option with those hypotheses, and the corresponding board (if there is)
        local_board = copy.deepcopy(old_board)
        undetermined_entries = received_undetermined_entries
        update = True
        while(update):
            valid, new_undetermined_entries  = self.update_undetermined_entries_board(local_board, undetermined_entries)
            if not valid:
                return False, 0
            if undetermined_entries == new_undetermined_entries:
                update = False
            else:
                undetermined_entries = new_undetermined_entries
                
        if undetermined_entries == []:
            return True, local_board
        else:
            (i,j) = undetermined_entries[0]
            #undetermined_entries.pop(0)
            possible_values = self.set_possible_values(local_board,i,j)
            for value in possible_values:
                local_board[i][j] = value
                valid, new_board = self.solve(local_board,undetermined_entries)
                if valid:
                    return True, new_board
            return False, 0
        
    def update_undetermined_entries_board(self,board,undetermined_entries):
        new_undetermined_entries = []
        for indices in undetermined_entries:
            i,j = indices[0], indices[1]
            if board[i][j] ==".":
                    my_set = self.set_possible_values(board,i,j)
                    if len(my_set) == 0:
                        return False, 0
                    if len(my_set)== 1:
                        (unique_element,) = my_set
                        board[i][j]= unique_element
                    else:
                        new_undetermined_entries.append([i,j])
        return True, new_undetermined_entries
        
        
    def set_possible_values(self,board,i,j):
        return set.intersection(self.set_box(board,floor(i/3),floor(j/3)),self.set_row(board,i),self.set_column(board,j))
        
    def set_box(self,board,k,n):
        return {str(s) for s in range(1,10) if str(s) not in { entry  for line in board[3*k:3*k+3] for entry in line[3*n:3*n+3]} }
    
    def set_row(self,board,k):
        return {str(i) for i in range(1,10) if str(i) not in board[k]}
    
    def set_column(self,board,k):
        return {str(j)  for j in range(1,10) if str(j) not in {board[i][k] for i in range(9)}}
        

        
        

my_board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
my_sol = Solution()
#print("test")
my_sol.solveSudoku(my_board)

        