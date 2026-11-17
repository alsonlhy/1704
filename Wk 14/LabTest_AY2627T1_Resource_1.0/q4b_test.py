
from q4b import torus

def main():
    test_cases = [('ABGDEFKHIJOLMNCP', 4, [('ABGDEFKHIJOLMNCP', '2D'), ('ABCDEFGHIJKLMNOP', '')]),
                  ('BCDA', 2, [('BCDA', '0L'), ('CBDA', '1L'), ('CBAD', '0U'), ('ABCD', '')]),
                  ('AGCDFJHEINKLMBOP', 4,
                   [('AGCDFJHEINKLMBOP', '1D'),
                    ('ABCDFGHEIJKLMNOP', '1R'),
                    ('ABCDEFGHIJKLMNOP', '')]),                 
                  ('EMCDIFBHPGKLAJNO', 4,
                   [('EMCDIFBHPGKLAJNO', '1L'),
                    ('EMCDFBHIPGKLAJNO', '1U'),
                    ('EBCDFGHIPJKLAMNO', '1R'),
                    ('EBCDIFGHPJKLAMNO', '0D'),
                    ('ABCDEFGHIJKLPMNO', '3L'),
                    ('ABCDEFGHIJKLMNOP', '')])
                  ]
    
    for ix, (pzl, N, expected) in enumerate(test_cases):
        print(f"\nTest Case {ix+1}: torus('{pzl}', {N})")
        print("-------------------------------------------")
        
        result = torus(pzl, N)
        
        print('Expected:', expected)
        print('Actual:  ', result)

if __name__ == '__main__':
    main()
