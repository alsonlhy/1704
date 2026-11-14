# Name:
# Email ID:
    
def get_counts(pokemon_cards):

    electric_count = 0
    fighting_count = 0
    fire_count = 0
    ground_count = 0
    normal_count = 0
    water_count = 0

    for pokemon in pokemon_cards:
        category = pokemon[1]

        if category == "electric":
            electric_count += 1
        elif category == "fighting":
            fighting_count += 1
        elif category == "fire":
            fire_count += 1
        elif category == "ground":
            ground_count += 1
        elif category == "normal":
            normal_count += 1
        elif category == "water":
            water_count += 1
    
    return (electric_count, fighting_count, fire_count, ground_count,normal_count,water_count)



