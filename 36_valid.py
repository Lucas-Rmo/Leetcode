class Solution(object):
    def isValidSudoku(self, board):

        
        column1 = [board[0][0],board[1][0],board[2][0],
                   board[3][0],board[4][0],board[5][0],
                   board[6][0],board[7][0],board[8][0]
                   ]
        
        column2 = [board[0][1],board[1][1],board[2][1],
                   board[3][1],board[4][1],board[5][1],
                   board[6][1],board[7][1],board[8][1]
                   ]
        
        column3 = [board[0][2],board[1][2],board[2][2],
                   board[3][2],board[4][2],board[5][2],
                   board[6][2],board[7][2],board[8][2]
                   ]
        
        column4 = [board[0][3],board[1][3],board[2][3],
                   board[3][3],board[4][3],board[5][3],
                   board[6][3],board[7][3],board[8][3]
                   ]
        
        column5 = [board[0][4],board[1][4],board[2][4],
                   board[3][4],board[4][4],board[5][4],
                   board[6][4],board[7][4],board[8][4]
                   ]
        
        column6 = [board[0][5],board[1][5],board[2][5],
                   board[3][5],board[4][5],board[5][5],
                   board[6][5],board[7][5],board[8][5]
                   ]
        
        column7 = [board[0][6],board[1][6],board[2][6],
                   board[3][6],board[4][6],board[5][6],
                   board[6][6],board[7][6],board[8][6]
                   ]
        
        column8 = [board[0][7],board[1][7],board[2][7],
                   board[3][7],board[4][7],board[5][7],
                   board[6][7],board[7][7],board[8][7]
                   ]
        
        column9 = [board[0][8],board[1][8],board[2][8],
                   board[3][8],board[4][8],board[5][8],
                   board[6][8],board[7][8],board[8][8]
                   ]
        
        box1 = [board[0][0],board[0][1],board[0][2],
                board[1][0],board[1][1],board[1][2],
                board[2][0],board[2][1],board[2][2]]
        
        box2 = [board[0][3],board[0][4],board[0][5],
                board[1][3],board[1][4],board[1][5],
                board[2][3],board[2][4],board[2][5]]
        
        box3 = [board[0][6],board[0][7],board[0][8],
                board[1][6],board[1][7],board[1][8],
                board[2][6],board[2][7],board[2][8]]
        
        box4 = [board[3][0],board[3][1],board[3][2],
                board[4][0],board[4][1],board[4][2],
                board[5][0],board[5][1],board[5][2]]
        
        box5 = [board[3][3],board[3][4],board[3][5],
                board[4][3],board[4][4],board[4][5],
                board[5][3],board[5][4],board[5][5]]
        
        box6 = [board[3][6],board[3][7],board[3][8],
                board[4][6],board[4][7],board[4][8],
                board[5][6],board[5][7],board[5][8]] 
        
        box7 = [board[6][0],board[6][1],board[6][2],
                board[7][0],board[7][1],board[7][2],
                board[8][0],board[8][1],board[8][2]]
        
        box8 = [board[6][3],board[6][4],board[6][5],
                board[7][3],board[7][4],board[7][5],
                board[8][3],board[8][4],board[8][5]]
        
        box9 = [board[6][6],board[6][7],board[6][8],
                board[7][6],board[7][7],board[7][8],
                board[8][6],board[8][7],board[8][8]]


        rows = [board[0],board[1],board[2],
                board[3],board[4],board[5],
                board[6],board[7],board[8]
                ]
        
        columns = [column1,column2,column3,column4,column5,
                   column6,column7,column8,column9]
        
        boxes = [box1,box2,box3,box4,box5,box6,box7,box8,box9]

        repeat = []

        for row in rows:
            repeat.clear()
            for value in row:
                print(value)
                if value in repeat and value !=".":
                    return False
                else:
                    repeat.append(value)
        repeat.clear()

        for column in columns:
            repeat.clear()
            for value in column:
                if value in repeat and value !=".":
                    return False
                else:
                    repeat.append(value)
        repeat.clear()

        for box in boxes:
            repeat.clear()
            for value in box:
                if value in repeat and value !=".":
                    return False
                else:
                    repeat.append(value)
        repeat.clear()
        return True
    

solution = Solution()
print(solution.isValidSudoku(
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))