# Name:
# Email ID:

def get_best_avg(pokemon_cards, metric):

    if metric == "hp":
        id = 2

    elif metric == "attack":
        id = 3

    elif metric == "defense":
        id = 4

    categories = ['electric', 'fighting', 'fire', 'ground', 'normal', 'water']
    best_category = ''
    best_avg = -1

    for cat in categories:
        total = 0
        count = 0

        for pokemon in pokemon_cards:
            if pokemon[1] == cat:
                total += pokemon[id]
                count += 1

        avg = round(total/count,2)

        if avg > best_avg:
            best_avg = avg
            best_category = cat
              


    return (best_category,best_avg)


# def get_best_avg(pokemon_cards, metric):



#     return None