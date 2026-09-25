
from q4b import help_frog_against_snakes_2

map_lines_1 = ['A00*',
               '00*0',
               '**0B']

map_lines_2 = ['A***',
               '*000',
               '*000',
               '*00B']
map_lines_3 = ['A00',
               '000',
               '00B'] 

case_1_list = [[(1, 'd'), (3, 'r'), (1, 'd')], [(1, 'r'), (1, 'd'), (2, 'r'), (1, 'd')], [(1, 'd'), (1, 'r'), (2, 'r'), (1, 'd')], [(2, 'r'), (2, 'd'), (1, 'r')], [(1, 'r'), (1, 'r'), (2, 'd'), (1, 'r')]]
case_2_list = []
case_3_list = [[(2, 'r'), (2, 'd')], [(1, 'r'), (1, 'r'), (2, 'd')], [(2, 'r'), (1, 'd'), (1, 'd')], [(1, 'r'), (1, 'r'), (1, 'd'), (1, 'd')], [(1, 'd'), (2, 'r'), (1, 'd')], [(1, 'r'), (1, 'd'), (1, 'r'), (1, 'd')], [(1, 'd'), (1, 'r'), (1, 'r'), (1, 'd')], [(2, 'd'), (2, 'r')], [(1, 'd'), (1, 'd'), (2, 'r')], [(1, 'r'), (2, 'd'), (1, 'r')], [(1, 'r'), (1, 'd'), (1, 'd'), (1, 'r')], [(1, 'd'), (1, 'r'), (1, 'd'), (1, 'r')], [(2, 'd'), (1, 'r'), (1, 'r')], [(1, 'd'), (1, 'd'), (1, 'r'), (1, 'r')]]

test_cases = [(map_lines_1, (len(case_1_list), case_1_list)),
              (map_lines_2, (len(case_2_list), case_2_list)),
              (map_lines_3, (len(case_3_list), case_3_list))]

for ix, (test_map, expected) in enumerate(test_cases):
    print()
    print('-' * 30)
    print(f'Test Case {ix+1}: help_frog_against_snakes_2({test_map})')
    
    ret = help_frog_against_snakes_2(test_map)
    print("Expected type of returned value: <class 'int'>, <class 'list'>")
    if ret is None:
        print('Actual type of returned value:   ' + str(type(None)))
    else:
        (total, seqs) = ret
        print('Actual type of returned value:   ' + str(type(total))+ ', '+str(type(seqs)))

        print('Expected:', expected)
        print('Actual:  ', ret)

        flag = True
        for item in seqs:
            if item not in expected[1]:
                flag=False
        for item in expected[1]:
            if item not in seqs:
                flag=False
        if flag==True and seqs != expected[1]:
            print('OK with different order')
        elif flag==True:
            print('OK with same order')
        else:
            print('Not equal!!')
    print()
