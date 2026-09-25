def sort_strings(string_list):

    string_list.sort(key=len)


    return string_list

        

    
def sort_strings2(string_list):

    new_list = []

    for string in string_list:
        added = False

        for i in range(len(new_list)):

            if len(string) < len(new_list[i]):
                new_list = new_list[:i] + [string] + new_list[i:]
                added = True
                break

        if not added:
            new_list.append(string)

    return new_list









print(sort_strings(['abc', 'a', 'xy', '12', 'x']))
print(sort_strings2(['abc', 'a', 'xy', '12', 'x']))
