from q1a import count_problematic_trips

test_cases = [
    #  trips                                                            num    expected
    ([('B10', 45, 2), ('B20', 30, 15), ('B30', 15, 5), ('B40', 48, 12)], 3),
    ([('B1', 40, 7), ('B2', 41, 9)], 1),
    ([('B11', 17, 10), ('B21', 26, 11)], 2),
    ([('B100', 39, 8), ('B20', 22, 7)], 0),
    ([], 0)
]

for ix, (trips, expected_count) in enumerate(test_cases):
    print(f"\nTest Case {ix+1}: count_problematic_trips({trips})")
    print("-------------------------------------------")
    
    result = count_problematic_trips(trips)

    print('Expected type of returned value: ' + str(type(expected_count)))
    print('Actual type of returned value:   ' + str(type(result)))
    print('Expected:', expected_count)
    print('Actual:  ', result)
    
