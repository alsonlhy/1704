# Name:
# Email ID:
from q4_utils import print_board

def get_board_state_gravity(N, game):
    # Replace the code below with your implementation.
    # Create an empty board.
    #   A list of N strings
    #   Each string has N "-" characters        
    board = ["-"*N]*N

    # The number of moves in the string is always
    # a multiple of 2
    num_moves = len(game)//2
    for i in range(num_moves):
        # Extract the ith move
        move = game[2*i:2*i+2]
        col_ix = int(move[0])
        player = move[1]
        # Find LAST cell in this column that is empty
        # There are many ways to do this.
        # This code assumes we won't try to put a piece into
        # a column that is already full
        rix = -1
        for row_ix in range(N):
            if rix == -1 and board[row_ix][col_ix] != '-':
                rix = row_ix - 1
                
        row = board[rix] # Extract the row to update
        # String slicing to update the string
        board[rix] = row[0:col_ix] + player + row[col_ix+1:]     
   
    return board

    
