# Name: Alson Lam
# Email ID: alson.lam.2026

def get_suitable_rooms(rooms, num_students):
    """
    Creates a list of suitable study rooms

    Args:
        rooms (list[tuple]): A list of tuples representing study rooms. Each tuple
        contains 4 elements: (room_name, capacity, has_projector, is_available)
    
    Returns:
        list[str]: a list of study room names satisfying the criteria

    """
    suitable_rm = []

    for tup in rooms:
        room_name = tup[0]
        cap = tup[1]
        has_proj = tup[2]
        is_avail = tup[3]

        if cap >= num_students and has_proj == True and is_avail == True:
            suitable_rm.append(room_name)


    return suitable_rm
        
