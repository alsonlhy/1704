# Name:
# Email ID:

def select_fields(pokedex, query):    
    # Replace the code below with your implementation.
    
    output_fields = query.strip().split()
    # Sanity check - this should not happen and students are not
    # expected to handle this condition
    if (len(output_fields) == 0) or (output_fields[0] != 'select'):
        raise ValueError('Select statement does not start with keyword')
    
    # Assume "where" is the first string
    output_fields = output_fields[1:]    
    
    # If no output fields specified, return the original database
    if output_fields == []:
        return pokedex
    
    output = []
    # Iterate through list of dicts
    for pokemon in pokedex:
        dct = {}        
        for k1 in output_fields:
            # Copy selected fields into new dictionary
            # If key not in dictionary, ignore it            
            if k1 in pokemon:           
                dct[k1] = pokemon[k1]
        # Do not insert empty dictionaries into result                
        if len(dct):                   
            output.append(dct)
    return output


