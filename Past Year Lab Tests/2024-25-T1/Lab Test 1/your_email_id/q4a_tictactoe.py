# Name:
# Email ID:

from q4_utils import print_board

def get_board_state(N, game):
    # Create an empty board.
    #   A list of N strings
    #   Each string has N "-" characters    
    board = ["-"*N]*N
    
    # The number of moves in the string is always
    # a multiple of 3
    num_moves = len(game)//3
    for i in range(num_moves):
        # Extract the ith move
        move = game[3*i:3*i+3]
        row_ix = int(move[0])
        col_ix = int(move[1])
        player = move[2]
        
        # Update the board
        row = board[row_ix] # extract the row to update
        # String slicing to update the string
        board[row_ix] = row[0:col_ix] + player + row[col_ix+1:]     
    return board  
    
