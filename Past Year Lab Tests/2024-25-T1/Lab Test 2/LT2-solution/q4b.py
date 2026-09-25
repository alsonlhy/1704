# Name:
# Email ID:

from itertools import combinations
from q4a import read_data

def same_elements(tup1, tup2):
    # check if two tuples have the same elements (can be in different order)
    # (4, 4, 2, 2) is the same as (2, 4, 2, 4)
    # (4, 1, 1, 1) and (4, 4, 1, 1) are not the same
    if len(tup1) != len(tup2):
        return False
    for item in tup1:
        if tup1.count(item) != tup2.count(item):
            return False
    return True

def get_coins(filename, address, target):
    unspent_outputs = []
    transactions = read_data(filename)
    for key in transactions:
        inputs = transactions[key][0]
        outputs = transactions[key][1]

        # get all outputs for the given address
        for output in outputs:
            addr, value = output.split(':')
            value = int(value)
            if addr == address:
                unspent_outputs.append((address, value))
        
        # remove the spent outputs
        for input in inputs:
            addr, value = input.split(':')
            value = int(value)
            for i in range(len(unspent_outputs)):
                if unspent_outputs[i] == (addr, value):
                    unspent_outputs = unspent_outputs[:i] + unspent_outputs[i+1:]
                    break
        
    closest_combinations = []
    min_diff = float('inf')
    unspent_values = [value for _, value in unspent_outputs]
    # print(unspent_values)

    for r in range(1, len(unspent_values) + 1):
        for combo in combinations(unspent_values, r):
            total_value = sum(value for value in combo)
            if total_value >= target:
                diff = total_value - target
                if diff < min_diff:
                    min_diff = diff
                    closest_combinations = [combo]
                elif diff == min_diff:
                    existed = False
                    for c in closest_combinations:
                        if same_elements(combo, c):
                            existed = True
                            break
                    if not existed:
                        closest_combinations.append(tuple(combo))

    return closest_combinations