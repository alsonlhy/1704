from q4b import get_board_state_gravity    
from q4_utils import print_board

test_cases = [(0,4,'0x1o1x1o0x2o',['----', '-o--', 'xx--', 'xoo-']),
              (1,5,'0o4x4o1x2o0x1o4x1o1x4o1x2o0x3o0x3o',['-x---', 'xx--o', 'xo--x', 'xoooo', 'oxoox']),
              (2,4,'0o0x3o2x1o2x1o',['----', '----', 'xox-', 'ooxo']),
              (3,5,'0x2o1x0o0x0o4x1o2x4o1x4o2x',['-----', 'o----', 'xxx-o', 'oox-o', 'xxo-x']),
              (4,3,'1o1x',['---', '-x-', '-o-']),
              (5,3,'',['---', '---', '---']),
              ]

for ix,N,game,expected_result in test_cases:
    print()
    print('-' * 20)
    print()

    print(f"Test Case {ix}: get_board_state_gravity(N={N}, game = '{game}')")
    result = get_board_state_gravity(N, game)
    print()
    
    print('Expected: ' + str(expected_result))
    print('Actual:   ' + str(result))
    print()

    print('Expected, rendered as a 2D game board: ')
    print_board(expected_result)
    print()
    if isinstance(result, list):
        print('Actual, rendered as a 2D game board: ')
        print_board(result)
        print()
    
    print('Expected type of returned value: ' + str(type(expected_result)))
    print('Actual type of returned value:   ' + str(type(result)))
