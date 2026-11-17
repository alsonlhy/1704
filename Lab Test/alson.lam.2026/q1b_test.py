from q1b import get_suitable_rooms

test_cases = [
    # rooms and number of students                                                                                 expected_list
    (([('GSR1', 4, True, True), ('GSR2', 8, True, False), ('GSR3', 6, True, True), ('GSR4', 10, False, True)], 5) , ['GSR3']), 
    (([('GSR1', 6, False, True), ('GSR2', 6, True, True), ('GSR3', 10, False, True)], 6), ['GSR2']),
    (([('GSR10', 8, True, True), ('GSR20', 12, True, True), ('GSR30', 15, True, False)], 7), ['GSR10', 'GSR20']),
    (([('GSR1', 5, True, True), ('GSR2', 6, False, True), ('GSR3', 7, True, True)], 8), []),
    (([], 5), [])
]

for ix, ((rooms, num_students), expected_list) in enumerate(test_cases):
    print(f"\nTest Case {ix+1}: get_suitable_rooms({rooms}, {num_students})")
    print("-------------------------------")
    
    result = get_suitable_rooms(rooms, num_students)

    print('Expected type of returned value: ' + str(type(expected_list)))
    print('Actual type of returned value:   ' + str(type(result)))
    print('Expected:', expected_list)
    print('Actual:  ', result)
    
