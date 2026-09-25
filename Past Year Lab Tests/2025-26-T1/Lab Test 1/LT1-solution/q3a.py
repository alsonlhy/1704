# Name:
# Email ID:
    
def get_counts(pokemon_cards):
    # Modify the code below.
    categories = ["electric", "fighting", "fire", "ground", "normal", "water"]
    counts = [0, 0, 0, 0, 0, 0]
    for card in pokemon_cards:
        for i in range(len(categories)):
            if card[1] == categories[i]:
                counts[i] += 1
    return tuple(counts)




