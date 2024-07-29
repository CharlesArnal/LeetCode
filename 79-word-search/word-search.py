class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return True
        else:
            for i, row in enumerate(board):
                for j, entry in enumerate(row):
                    if entry==word[0]:
                        character = board[i][j]
                        board[i][j] = ""
                        if self.exist_from_position(board,word[1:],(i,j)):
                            return True
                        board[i][j] = character
            return False


    def exist_from_position(self, board, word, position):
        # print("inside call")
        # print(position)
        # print(board)
        # print(word)
        if word == "":
            return True
        else:
            adjacent_positions = []
            if position[0]>0:
                adjacent_positions += [[-1,0]]
            if position[0]<len(board)-1:
                adjacent_positions += [[1,0]]
            if position[1]>0:
                adjacent_positions += [[0,-1]]
            if position[1]<len(board[0])-1:
                adjacent_positions += [[0,1]]
            for neighbour in adjacent_positions:
                # print(f"neighbour {neighbour[0]} {neighbour[1]}")
                if board[position[0]+neighbour[0]][position[1]+neighbour[1]] == word[0]:
                    character = board[position[0]+neighbour[0]][position[1]+neighbour[1]]
                    board[position[0]+neighbour[0]][position[1]+neighbour[1]] = ""
                    if self.exist_from_position(board,word[1:],(position[0]+neighbour[0],position[1]+neighbour[1])):
                        return True
                    board[position[0]+neighbour[0]][position[1]+neighbour[1]] = character

            return False
            

        
    