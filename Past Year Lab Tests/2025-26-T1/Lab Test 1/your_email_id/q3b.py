# Name:
# Email ID:

def get_pokemon_info(pokemon_cards):

    strongest_attack = 0
    strongest_def = 0
    total_hp = 0
    count = 0  

    for pokemon in pokemon_cards:
        name = pokemon[0]
        hp = pokemon[2]
        attack = pokemon[3]
        defense = pokemon[4]

        count += 1
        total_hp += hp

        if attack > strongest_attack:
            strongest_attack = attack
            strongest_a_poke = name

        if defense > strongest_def:
            strongest_def = defense
            strongest_d_poke = name

    avg_hp = round(total_hp/count,2)


    return (avg_hp, strongest_a_poke, strongest_d_poke)




