def checkmate (board):
    rows = board.strip().split("\n")
    def enemy (board):
        enemy =[]
        n = 1
        for i in range (len(rows)):
            for j in range (len(rows[i])):
                pieceat = [rows[i][j],[i,j]]
                piece = rows[i][j]
                if rows[i][j] != "K" and rows[i][j] != ".":
                    if rows[i][j] == "Q" or rows[i][j] == "B" or rows[i][j] == "R" or rows[i][j] == "P":
                        enemy.append(pieceat)
                        
        return enemy

    def king_check(board):
    # Find king
        kingcount = 0
        kingrow = -1
        kingcolu = -1
        for i in range (len(rows)):
            for j in range (len(rows[i])):
                if rows[i][j] == "K":
                    kingrow = i
                    kingcolu = j
                    kingcount +=1
        kingpos = [kingrow,kingcolu]
        return [kingpos,kingcount]


    
    def game (board):
        king_position = king_check(board)[0]
        kingcount = king_check(board)[1]
        enemy_position = enemy(board)
        Pawncapture = 0
        Rookcapture = 0
        Queencapture = 0
        Bishopcapture = 0
        for i in enemy_position:
            if i[0] == 'P':
                if i[1][0] <= king_position[0]:
                    Pawncapture = 0
                else :
                    if abs(i[1][0] - king_position[0]) == 1 and abs(i[1][1] - king_position[1]) == 1:
                        Pawncapture = 1
                    
            elif i[0] == 'R':
                if i[1][0] == king_position[0] or i[1][1] == king_position[1]:
                    Rookcapture = 1  
            elif i[0] == 'B':
                if abs(i[1][0] - king_position[0]) == abs(i[1][1] - king_position[1]):
                        Bishopcapture = 1 
            elif i[0] == 'Q':
                if i[1][0] == king_position[0] or i[1][1] == king_position[1]:
                    Queencapture = 1 
                elif abs(i[1][0] - king_position[0]) == abs(i[1][1] - king_position[1]):
                    Queencapture = 1
        rows_mem = []
        for i in range(len(rows)):
            rows_mem.append(len(rows[i]))
        r = all(ele == rows_mem[0] for ele in rows_mem)
    
        if rows_mem == [0] or rows_mem == []:
            return "Board not found!"
        elif len(rows) != rows_mem[0]:
            return "ERROR"
        elif not r:
            return "ERROR"
      
        elif kingcount > 1 or kingcount < 1:
            return "ERROR"
        
        elif Pawncapture+Rookcapture+Queencapture+Bishopcapture >= 1:
            return "SUCCESS"
        elif Pawncapture+Rookcapture+Queencapture+Bishopcapture < 1:
            return "FAIL"
            
    return game(board)
