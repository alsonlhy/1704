# Name:
# Email ID:

def get_pokemon_info(pokemon_cards):  
    # Modify the code below.
    max_attack = 0
    max_defense = 0
    strongest_attacker = None
    strongest_defender = None
    sum_hp = 0
    for name, type, hp, attack, defense in pokemon_cards:
        # sum hp
        sum_hp += hp
        # max attacker
        if attack >= max_attack:
            max_attack = attack
            strongest_attacker = name
        # max defender
        if defense >= max_defense:
            max_defense = defense
            strongest_defender = name
    
    avg = round(sum_hp / len(pokemon_cards),2)

    return (avg, strongest_attacker, strongest_defender)



