# q3a.py
# Name: 
# Email ID:

def read_weather_data(filename):
    """
    Reads weather data from a file and organizes it into a dictionary.

    Args:
        filename (str): The name of the file to read.

    Returns:
        dict: A dictionary where keys are city names and values are lists of 
              weather record tuples. Each tuple is in the format:
              ((year, month, day), max_temp, min_temp, precipitation).
    """
    # Modify the code below.
    dict_to_return = {}
    
    with open(filename, 'r') as my_file:
        for line in my_file:
            line = line.rstrip('\n')
            a_date, city, max_temp_str, min_temp_str, precipitation_str = line.split('|')
            max_temp, min_temp, precipitation = float(max_temp_str), float(min_temp_str), float(precipitation_str)
            year_str, month_str, day_str = a_date.split("-")
            year, month, day = int(year_str), int(month_str), int(day_str)

            if city not in dict_to_return:
                dict_to_return[city] =  [ ( (year, month, day), max_temp, min_temp, precipitation ) ]
            else:
                dict_to_return[city].append( ( (year, month, day), max_temp, min_temp, precipitation) )

    return dict_to_return
