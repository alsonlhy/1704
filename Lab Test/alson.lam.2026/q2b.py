# Name: Alson Lam   
# Email ID: alson.lam.2026
 
def verify_tags(tags):
    """
    Verify a list of warehouse tags.
 
    Each tag is a 9-character string in the format:
        <parcel_id><weight_code><parity_char>
    where:
        parcel_id   - 5 uppercase letters identifying the parcel
        weight_code - 3 digits representing the weight in grams
        parity_char - 'E' if the weight is even, 'O' if the weight is odd
 
    A tag is valid only if both conditions hold:
        1. parity_char correctly matches the parity of the weight.
        2. parcel_id contains at least 3 distinct letters.
 
    Args:
        tags (list[str]): A list of tag strings. May be empty.
    Returns:
        list[tuple(str, int, bool)]: A list of (parcel_id, weight, is_valid)
             tuples, one per tag, in the same order as tags.
    """

    new_list = []

    for tag in tags:
        parcel_id = tag[0:5]
        weight_code = int(tag[5:8])
        parity_char = tag[-1]

        id_pass = False
        parity_pass = False
        is_valid = False
        uniq_char = 0
        uniq_ch = ''

        for ch in parcel_id:
            if ch not in uniq_ch:
                uniq_char += 1
                uniq_ch += ch

        if uniq_char >= 3:
            id_pass = True

        if parity_char == "O" and weight_code % 2 !=0:
            parity_pass = True

        elif parity_char == "E" and weight_code %2 == 0:
            parity_pass = True

        if id_pass and parity_pass:
            is_valid = True

            

        new_list.append((parcel_id, weight_code, is_valid ))

        

    return new_list

