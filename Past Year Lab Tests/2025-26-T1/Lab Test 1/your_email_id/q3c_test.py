from q3c import get_best_avg

def test_case_with_args(i, func, *args, expected):
    print()
    print('-' * 20)
    print()
    print(f"Test Case {i}: {func.__name__}{args}")
    print()
    result = func(*args)
    print('Expected: ', expected)
    print('Actual:   ', result)
    print("Expected type of returned value: <class 'tuple'>")
    print('Actual type of returned value:   ' + str(type(result)))
    

test_pokemon_cards1 = [
    ("Arcanine", "fire", 91, 110, 80),
    ("Pikachu", "electric", 35, 55, 40),
    ("Machop", "fighting", 70, 80, 50),
    ("Charmander", "fire", 69, 52, 43),
    ("Charizard", "fire", 78, 84, 78),
    ("Diglett", "ground", 10, 56, 25),
    ("Eevee", "normal", 55, 55, 52),
    ("Squirtle", "water", 44, 48, 68),
    ("Raichu", "electric", 60, 90, 55)
]

test_pokemon_cards2 = [
    ("Pikachu", "electric", 35, 55, 40),
    ("Raichu", "electric", 60, 90, 55),
    ("Machop", "fighting", 70, 80, 50),
    ("Hitmonlee", "fighting", 50, 120, 53),
    ("Charmander", "fire", 39, 52, 43),
    ("Charizard", "fire", 78, 84, 78),
    ("Diglett", "ground", 10, 56, 25),
    ("Onix", "ground", 35, 45, 160),
    ("Eevee", "normal", 55, 55, 52),
    ("Snorlax", "normal", 160, 110, 65),
    ("Squirtle", "water", 44, 48, 66),
    ("Blastoise", "water", 79, 83, 100)
]

expected = ('fire', 79.33)
test_case_with_args(1, get_best_avg, test_pokemon_cards1, "hp", expected=expected)
expected = ('fire', 82.0)
test_case_with_args(2, get_best_avg, test_pokemon_cards1, "attack", expected=expected)
expected = ('water', 68.0)
test_case_with_args(3, get_best_avg, test_pokemon_cards1, "defense", expected=expected)

expected = ('normal', 107.5)
test_case_with_args(4, get_best_avg, test_pokemon_cards2, "hp", expected=expected)
expected = ('fighting', 100.0)
test_case_with_args(5, get_best_avg, test_pokemon_cards2, "attack", expected=expected)
expected = ('ground', 92.5)
test_case_with_args(6, get_best_avg, test_pokemon_cards2, "defense", expected=expected)

