# Name:
# Email ID:

from q4_utils import print_board

def extract_strings(board, row_step = 0, flip = 1):
    # There are many ways to do this.

    strings = []
    for ix in range(len(board)):        
        stringA = stringB = ""        
        for jx in range(len(board)):
            # If row_step = 1 index diagonally into the board
            kx = ix + row_step*jx 
            # Protect against indexing errors. Not all diagonals are length N
            if not 0 <= kx < len(board):
                break
            # Flip allows us to index a string forwards or backwards
            # This is how we are able to extract all diagonals
            stringA += board[kx][::flip][jx]
            stringB += board[jx][::flip][kx]

        strings.append(stringA)
        strings.append(stringB)
    return strings

def check_M_in_row(M, strings, player):
    test_string = player * M
    for string in strings:
        if test_string in string:
            return True
    return False

def get_who_won(M, board):
    strings = extract_strings(board, row_step = 0)   # horizontal/vertical
    strings += extract_strings(board, row_step = 1)  # diagonal 1
    strings += extract_strings(board, row_step = 1, flip = -1) # diagonal 2
    x_wins = check_M_in_row(M, strings, 'x')
    o_wins = check_M_in_row(M, strings, 'o')
    # sanity check 
    if x_wins and o_wins:
        raise ValueError('X and O both win??')
    
    num_empty = ''.join(board).count('-')
    if x_wins:
        who_won_game = "x"
    elif o_wins:
        who_won_game = "o"
    elif not x_wins and not o_wins and num_empty == 0:
        who_won_game = "tie"
    else:
        who_won_game = None
        
    return who_won_game