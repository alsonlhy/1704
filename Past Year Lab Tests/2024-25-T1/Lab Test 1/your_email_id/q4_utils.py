# DO NOT MODIFY THIS CODE #

def print_board(board):
    if board is None or not isinstance(board, list):
        return
    cols = '  '
    # create a line with column indices
    for i in range(len(board)):
        cols = cols + str(i) + ' '
    print(cols)
    for row_ix, row in enumerate(board):
        # add a space between spaces in the print out
        print(row_ix, ' '.join(list(row)))

        
