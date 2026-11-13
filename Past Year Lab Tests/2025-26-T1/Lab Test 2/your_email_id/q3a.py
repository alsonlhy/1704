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

    with open (filename) as reading:

        town_dict = {}    
        for line in reading:
            line = line.rstrip("\n")
            columns = line.split("|")

            date = columns[0].split("-")
            year = int(date[0])
            month = int(date[1])
            day = int(date[2])

            city = columns[1]
            max_temp = float(columns[2])
            min_temp = float(columns[3])
            precipitation = float(columns[4])

            if city not in town_dict:
                town_dict[city] = [((year,month,day),max_temp, min_temp, precipitation)]

            else:
                existing_city = town_dict[city]
                existing_city.append(((year,month,day),max_temp, min_temp, precipitation))
    
    return town_dict
