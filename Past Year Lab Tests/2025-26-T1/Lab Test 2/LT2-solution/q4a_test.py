from q4a import help_frog_against_snakes

map_1 = 'A00**0*00B'
map_2 = 'A0000B'
map_3 = 'A000*****B'

case_1_list = [[2, 3, 2, 2], [1, 1, 3, 2, 2], [2, 3, 3, 1], [1, 1, 3, 3, 1], [2, 3, 2, 1, 1], [1, 1, 3, 2, 1, 1]]
case_2_list = [[2, 3], [1, 1, 3], [3, 2], [1, 2, 2], [2, 1, 2], [1, 1, 1, 2], [1, 3, 1], [2, 2, 1], [1, 1, 2, 1], [3, 1, 1], [1, 2, 1, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
case_3_list = []

test_cases = [(map_1, (len(case_1_list), case_1_list)),
              (map_2, (len(case_2_list), case_2_list)),
              (map_3, (len(case_3_list), case_3_list))]

for ix, (test_map, expected) in enumerate(test_cases):
    print()
    print('-' * 30)
    print(f'Test Case {ix+1}: help_frog_against_snakes(\"{test_map}\")')
    ret = help_frog_against_snakes(test_map)
    print("Expected type of returned value: <class 'int'>, <class 'list'>")
    if ret is None:
        print('Actual type of returned value:   ' + str(type(None)))
    else:
        (total, seqs) = ret
        print('Expected:', expected)
        print('Actual:  ', ret)

        flag = True
        for item in seqs:
            if item not in expected[1]:
                flag=False
            for item in expected[1]:
                if item not in seqs:
                    flag=False
        if flag==True and seqs!=expected[1]:
            print('OK with different order')
        elif flag==True:
            print('OK with same order')
        else:
            print('Not equal!!')
    print()
