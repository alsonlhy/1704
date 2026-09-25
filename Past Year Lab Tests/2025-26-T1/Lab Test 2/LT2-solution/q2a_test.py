from q2a import decode_potter
from pprint import pprint
fnames = ['sentences-1.txt', 'sentences-2.txt']
expected = [
            ['Finished yer exams',
             '',
             '"Report him!"',
             'Has anyone seen a toad'],
            ["Neville's lips twitched in a weak smile as he unwrapped "
             'the frog',
             '"But Snape tried to kill me!"',
             'Potatoes, Harry?"',
             'Dumbledore sighed',
             '',
             'Hagrid lived in a small wooden house on the edge of the '
             'forbidden forest',
             '']
            ]

def run_test(ix, fname, exp):
    print(f"\nTest Case {ix+1}: decode_potter({fname})")
    print("-------------------------------------------")
    
    result = decode_potter(fname)

    print("Expected type of returned value: <class 'list'>")
    print('Actual type of returned value:   ' + str(type(result)))
    print()
    print('Expected:')
    pprint(exp)
    print()
    print('Actual:')
    pprint(result)
    print('\nIs the returned list as expected?', exp == result)
    print()

    
# Run test case 1
test_ix = 0
run_test(test_ix, fnames[test_ix], expected[test_ix])

# Run test case 2
test_ix = 1
run_test(test_ix, fnames[test_ix], expected[test_ix])

