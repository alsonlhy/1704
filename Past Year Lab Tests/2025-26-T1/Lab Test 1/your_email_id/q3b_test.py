from q3b import get_pokemon_info

def test_case(i, func, data, expected):
    print()
    print('-' * 20)
    print()
    print(f"Test Case {i}: {func.__name__}({data})")
    print()
    result = func(data)
    print('Expected: ', expected)
    print('Actual:   ', result)
    print("Expected type of returned value: <class 'tuple'>")
    print('Actual type of returned value:   ' + str(type(result)))

test_pokemon_cards1 = [
    ("Pikachu", "electric", 35, 55, 40),
    ("Machop", "fighting", 70, 80, 50),
    ("Charmander", "fire", 39, 52, 43),
    ("Diglett", "ground", 10, 56, 25),
    ("Eevee", "normal", 55, 55, 52),
    ("Squirtle", "water", 44, 48, 66),
    ("Raichu", "electric", 60, 90, 55)
]

test_pokemon_cards2 = [
    ("Zapdos", "electric", 90, 100, 85),
    ("Hitmonchan", "fighting", 70, 76, 79),
    ("Arcanine", "fire", 90, 110, 80),
    ("Golem", "ground", 80, 120, 130),
    ("Pidgeotto", "normal", 63, 60, 55),
    ("Vaporeon", "water", 130, 65, 60),
    ("Electabuzz", "electric", 65, 83, 57)
]

test_pokemon_cards3 = [
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

expected = (44.71, 'Raichu', 'Squirtle')
test_case(1, get_pokemon_info, test_pokemon_cards1, expected)
expected = (84.0, 'Golem', 'Golem')
test_case(2, get_pokemon_info, test_pokemon_cards2, expected)
expected = (59.58, 'Hitmonlee', 'Onix')
test_case(3, get_pokemon_info, test_pokemon_cards3, expected)

