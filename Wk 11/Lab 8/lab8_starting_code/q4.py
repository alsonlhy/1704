## Q4 Students and Schools
# write your code below

def get_students_by_school(dictionary):

    new_dict = {}

    for key in dictionary:

        new_key = dictionary[key]
        new_value = key

        if new_key not in new_dict:
            new_dict[new_key] = [new_value]

        else: 
            existing = new_dict[new_key]
            existing.append(new_value)

    return new_dict
