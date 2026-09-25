from q4c import get_who_won
from q4_utils import print_board

test_cases = [(0,3,['-----', '-----', 'x----', 'xo---', 'xo---'],'x'),
              (1,3,['-----', '-----', '-----', 'xo---', 'xo---'],None),
              (2,3,['xxo', 'oox', 'o-x'],'o'),
              (3,3,['xxo', 'oox', 'xxo'],'tie'),
              (4,3,['----', '---o', '-xo-', '-ox-'],'o')              
              ]

for ix,M,board,expected_result in test_cases:
    print()
    print('-' * 20)
    print()

    print(f"Test Case {ix}: get_who_won(M={M}, board = {board})")
    print('board, rendered as a 2D game board: ')
    print_board(board)
    
    result = get_who_won(M, board)
    print()
    
    print('Expected: ' + str(expected_result))
    print('Actual:   ' + str(result))
    print()
    
    print('Expected type of returned value: ' + str(type(expected_result)))
    print('Actual type of returned value:   ' + str(type(result)))
