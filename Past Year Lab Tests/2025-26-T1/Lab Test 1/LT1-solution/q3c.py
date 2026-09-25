# Name:
# Email ID:

def get_best_avg(pokemon_cards, metric):
    # Modify the code below.
    types = ["electric", "fighting", "fire", "ground", "normal", "water"]
    
    if metric == "hp":
        metric_index = 2
    elif metric == "attack":
        metric_index = 3
    elif metric == "defense":
        metric_index = 4

    sums = [0, 0, 0, 0, 0, 0]
    counts = [0, 0, 0, 0, 0, 0]
    for card in pokemon_cards:
        for i in range(len(types)):
            if card[1] == types[i]:
                sums[i] += card[metric_index]
                counts[i] += 1
    averages = [0, 0, 0, 0, 0, 0]
    for i in range(len(types)):
        if counts[i] > 0:
            averages[i] = sums[i] / counts[i]

    max_avg = averages[0]
    best_type_name = types[0]
    for i in range(len(types)):
        if averages[i] > max_avg:
            max_avg = averages[i]
            best_type_name = types[i]
    return (best_type_name, round(max_avg, 2))