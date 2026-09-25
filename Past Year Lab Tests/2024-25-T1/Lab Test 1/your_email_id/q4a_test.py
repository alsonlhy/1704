from q4a import get_board_state    
from q4_utils import print_board

test_cases = [(0,3,'11x20o22x10o00x',['x--', 'ox-', 'o-x']),
              (1,4,'21o01x11o30x33o20x10o',['-x--', 'oo--', 'xo--', 'x--o']),
              (2,5,'02x14o42x11o24x44o22x31o32x',['--x--', '-o--o', '--x-x', '-ox--', '--x-o']),
              (3,5,'32x44o03x10o30x',['---x-', 'o----', '-----', 'x-x--', '----o']),
              (4,3,'01o00x',['xo-', '---', '---']),
              (5,5,'10o00x31o30x12o32x14o42x22o13x33o04x11o',['x---x', 'oooxo', '--o--', 'xoxo-', '--x--']),
              ]

for ix,N,game,expected_result in test_cases:
    print()
    print('-' * 20)
    print()

    print(f"Test Case {ix}: get_board_state(N={N}, game = '{game}')")
    result = get_board_state(N, game)
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
