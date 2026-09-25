from q3a import load_pokedex
from q3b import select_fields
from poke_utils import compare_pokedex, print_pokedex
# Test cases are stored in pokedex_q3b_ref.py as
# list of tuples of (query, result)
from pokedex_q3b_ref import q3b_test, q3b_test_full

def run_test_case(num, tag, actual, expected, print_data = True):
    if not print_data:
        print(f'Test Case {num}: Output suppressed unless there is an error.')    
    print(f'Test Case {num}: {tag}')
    result = compare_pokedex(actual, expected)    
    if print_data or not result:
        print('Expected:')
        print_pokedex(expected)
        print()

        print('Actual:')
        print_pokedex(actual)

    print(f'Test Case {num}: {"PASS" if result else "FAIL"}')
    print('-' * 40)
    print()
    return result

def main():
    print('Testing on pokedex_abridged.txt')
    pokedex = load_pokedex('pokedex_abridged.txt')
    passed = True
    for ix, (q, expected) in enumerate(q3b_test):
        actual = select_fields(pokedex, q)
        passed &= run_test_case(ix+1, q, actual, expected)

    if passed:
        print('Testing on pokedex.txt')
        pokedex = load_pokedex('pokedex.txt')
        for ix, (q, expected) in enumerate(q3b_test_full):
            actual = select_fields(pokedex, q)
            passed &= run_test_case(ix+1, q, actual, expected)
    else:
        print('Not testing on pokedex.txt since prior tests failed.')
        
    if not passed:
        print('FAIL: At least one test case failed.')
    else:
        print('PASS: All test cases passed.')
        
if __name__ == "__main__":
    main()
