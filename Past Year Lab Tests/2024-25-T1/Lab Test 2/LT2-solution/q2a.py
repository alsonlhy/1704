# Name:
# Email ID:

def get_entry_count(filename, swimmer_name = None):
    # Replace the code below with your implementation.
    num_entries = 0
    tot_num_lines = 0
    
    with open(filename, 'r') as my_file:
        for line in my_file:
            tot_num_lines += 1
            columns = line .split(',')
            if swimmer_name == columns[0]:
                num_entries += 1
    if num_entries != 0:
        return num_entries
    
    return tot_num_lines
	
