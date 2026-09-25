import sys
from q3a import load_pokedex
from poke_utils import compare_pokedex, print_pokedex
from pokedex_q3a_ref import pokedex_ref_full

ref_pokedex_abridged = [{'pokedex_number': 1, 'name': 'Bulbasaur', 'type_2': 'Poison', 'height_m': 0.7}, {'pokedex_number': 2, 'name': 'Ivysaur', 'type_2': 'Poison', 'height_m': 1.1}, {'pokedex_number': 3, 'name': 'Venusaur', 'type_2': 'Poison', 'height_m': 2.1}, {'pokedex_number': 3, 'name': 'Mega Venusaur', 'type_2': 'Poison', 'height_m': 2.4}, {'pokedex_number': 4, 'name': 'Charmander', 'type_2': None, 'height_m': 0.6}, {'pokedex_number': 5, 'name': 'Charmeleon', 'type_2': None, 'height_m': 1.1}, {'pokedex_number': 6, 'name': 'Charizard', 'type_2': 'Flying', 'height_m': 1.7}, {'pokedex_number': 6, 'name': 'Mega Charizard X', 'type_2': 'Dragon', 'height_m': 1.7}, {'pokedex_number': 6, 'name': 'Mega Charizard Y', 'type_2': 'Flying', 'height_m': 1.7}, {'pokedex_number': 7, 'name': 'Squirtle', 'type_2': None, 'height_m': 0.5}, {'pokedex_number': 8, 'name': 'Wartortle', 'type_2': None, 'height_m': 1.1}]

def run_test_case(num, tag, actual, expected, print_data = True):
    print(f'Test Case {num}: {tag}')
    result = compare_pokedex(actual, expected)    
    if print_data or not result:
        print('Expected:')
        print_pokedex(expected)
        print()

        print('Actual:')
        print_pokedex(actual)
        print()

    print(f'Test Case {num}: {"PASS" if result else "FAIL"}')
    print()
    print('-' * 40)
    print()
    return result

def main():
    pokedex = load_pokedex('pokedex_abridged.txt')
    passed = run_test_case(1, 'pokedex_abridged.txt', pokedex, ref_pokedex_abridged)
    if passed:
        # Complete pokedex is serialized in pokedex_ref.py
        pokedex = load_pokedex('pokedex.txt')
        passed &= run_test_case(2, 'pokedex.txt', pokedex, pokedex_ref_full)
    else:
        print('Not testing on pokedex.txt since prior test failed.')

    if not passed:
        print('FAIL: At least one test case failed.')
    else:
        print('PASS: All test cases passed.')    

if __name__ == "__main__":
    main()
