def sum_of_neighbors(input_list):

    new_list = []



    for i in range(len(input_list)):
        num = input_list[i]
        if i > 0:
            num = num + input_list[i-1]
          
        if i < len(input_list) - 1:
            num = num + input_list[i+1]

            new_list.append(num)

    return new_list

print(sum_of_neighbors([56,-10,25,-32]))
