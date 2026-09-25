# The code here are used in the test scripts
# You do not need to use them in your code
################################################
def compare_pokedex(test, reference):
    """
    This function compares two lists of dicts.
    It returns True if they are identical.
    """
    if not is_valid_pokedex(test):
        return False
    
    if not is_valid_pokedex(reference):
        # sanity check
        raise RuntimeError('ERROR: Reference Pokedex is invalid!')
    
    if not len(test) == len(reference):
        print(f'ERROR: Pokedex length {len(test)} != reference length {len(reference)}')

    return test == reference
        
################################################        
def is_valid_pokedex(pokedex, no_output = False):
    """
    This function checks that the Pokedex:
    1. Is a list of dictionaries
    2. Each dictionary entry has type str, int, float, or None
    3. Importantly - there are no nested dictionaries/lists that require
       recursive inspection.
    """
    def is_valid_pokedex_core(pokedex):
        if not isinstance(pokedex, list):
            return 'ERROR: Pokedex is not a list.\n'

        if not all([isinstance(elem, dict) for elem in pokedex]):
            return 'ERROR: Pokedex elements are not all dictionaries.\n'

        # check that datatypes for the dictionary values are valid
        for ix, dct in enumerate(pokedex):
            for key, elem in dct.items():
                if not(type(elem) in [int, float, str, type(None)]):
                    err = f'ERROR: pokedex[{ix}]["{key}"] -'
                    err += ' type is not one of int, float, str, None\n'
                    # stop on the first error                
                    return err
        return ''
    
    err = is_valid_pokedex_core(pokedex)
    if err != '':
        if not no_output:
            print(err, end = '')
        return False
    return True

################################################
def print_pokedex(lst, limit = None, fp = None, tag = None):

    if not is_valid_pokedex(lst, no_output = True):
        # print the variable using default formatting
        print(str(lst))
        return False
    
    if tag is None:
       tag = 'unnamed'
        
    res = '['
    for ix, l in enumerate(lst):
        if limit is not None and ix == limit:
            break
        if ix != 0:
            res += ',\n'
        res += str(l)
    res += ']\n'
    if fp is not None:
        fp.write(f'{tag} = ' + res + '\n')
    else:
        print(res)
