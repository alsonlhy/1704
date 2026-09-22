# Name:
# Email ID:

def merge_list(list1,list2):

    new_list = []
    len1, len2 = len(list1), len(list2)
    max_len = max(len1, len2)

    for i in range(max_len):
        if i < len1:
            new_list.append(list1[i])

        if i < len2:
            new_list.append(list2[i])


    
    return new_list