
def parse_data(lines:list):
    
    # first line are the numbers
    numbers = [int(x) for x in lines[0].strip().split(",")]
      
    boards = []
    board = []
    for line in lines[2::]:
        
        if line.strip() == "":
            boards.append(board)
            board = []
        else:
            board.append([int(x) for x in line.strip().split()])
              
    boards.append(board)
      
    return (numbers, boards)


def remove_number_from_board(board, number):
    for row_counter, row in enumerate(board):
        for column_counter, value in enumerate(row):
            if value == number:
                board[row_counter][column_counter] = None
                
    return board

def check_for_winning_board(board):

    for row in board:        
        if row == [None] * len(row):
            return True
            
    for col_index in range(len(board[0])):
        
        col_total = 0
        for row_index in range(len(board)):
            if board[row_index][col_index] != None:
                break
            else:
                col_total += 1
            
        if col_total == len(board[0]):
            return True
        
    return False

def calulate_score(board, number):
    
    running_total = 0
    
    for row in board:
        for col in row:
            if col != None:
                running_total += col
                
    return running_total * number
     
                     
with open ("data/day4.txt") as f:
    numbers, boards = parse_data(f.readlines())
    

for number in numbers:   
    for counter, board in enumerate(boards):
        updated_board = remove_number_from_board(board,number)
        
        if check_for_winning_board(updated_board):
            print("WINNER!")
            winning_board = updated_board
            score = calulate_score(winning_board, number)
            print(score)
            exit()
        else:
            boards[counter] = updated_board
