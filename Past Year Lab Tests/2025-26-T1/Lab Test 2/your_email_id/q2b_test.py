from q2b import decode_potter_checksum
from pprint import pprint

fnames = ['sentences-3.txt', 'sentences-4.txt']
expected = [
            [("  Morbo's lips twitched in a weak smile as he unwrapped the frog", 18, False),
             ('"But  Lrrr tried to kill me!"', 6, False), ('Potatoes, Harry?"', 5, True),
             (' Morbodore sighed', 6, True),
             ('', 0, True),
             ('MORBO WILL DESTROY YOU! wooden house on the edge of the forbidden forest', 24, True),
             ('', 0, True)],            
            [('Never mess with Morbo!!, Harry', 7, True),
             ('Professor Lrrrrrrrrr sniffed angrily', 7, False),
             ('Harry saw the Ape-Man looked very worried', 13, False),
             ('Has anyone seen Morbo?', 8, False),
             ('The toadless boy was back, but this time he had a girl with him', 17, True)]
            ]

def run_test(ix, fname, exp):
    print(f"\nTest Case {ix+1}: decode_potter_checksum({fname})")
    print("-------------------------------------------")

    result = decode_potter_checksum(fname)
    
    print("Expected type of returned value: <class 'list'>")
    print('Actual type of returned value:   ' + str(type(result)))
    print()
    print('Expected:')
    pprint(exp, width = 100)
    print()
    print('Actual:')
    pprint(result, width = 100)
    print('\nIs the returned list as expected?', exp == result)
    print()
    
# Run test case 1
test_ix = 0
run_test(test_ix, fnames[test_ix], expected[test_ix])

# Run test case 2
test_ix = 1
run_test(test_ix, fnames[test_ix], expected[test_ix])
