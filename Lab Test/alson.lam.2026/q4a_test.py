
from q4a import rotate

def render_puzzle(puzzle, N):
    """ Print a puzzle.
        Arguments:
            puzzle (str): The puzzle, a row-major string of upper-case letters
            N      (int): The number of rows or columns, where N > 0
        Returns: None
    """
    if puzzle is None:
        return ''

    st = ''
    for i in range(N):
        st += '\t  '
        for j in range(N):
            st += f'{puzzle[i*N + j]:2s} '
        st += '\n'
    return st


def main():        
    test_cases = [('ABCDEFGHIJKLMNOP', 4, '2U', 'ABGDEFKHIJOLMNCP'),
                  ('ABCDEFGHIJKLMNOP', 4, '1R', 'ABCDHEFGIJKLMNOP'),
                  ('ABCDEFGHIJKLMNOPQRSTUVWXY', 5, '4D', 'ABCDYFGHIEKLMNJPQRSOUVWXT')
                  ]

    for ix, (pzl, N, move, expected) in enumerate(test_cases):
        print(f"\nTest Case {ix+1}: rotate('{pzl}', {N}, '{move}')")
        print("-------------------------------------------")
        print('Input:   ')
        print(render_puzzle(pzl, N))
        
        result = rotate(pzl, N, move)
        
        print(f"Expected: '{expected}'")
        print(render_puzzle(expected, N))        
        print(f"Actual:   ", end = '')
        
        if result is not None:
            print(f"'{result}'")
        else:
            print(result)            
        print(render_puzzle(result, N))

if __name__ == '__main__':
    main()
