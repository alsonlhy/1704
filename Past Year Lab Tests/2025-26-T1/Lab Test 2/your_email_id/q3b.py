# q3b.py
# Name: 
# Email ID: 
from q3a import read_weather_data

def analyze_weather_patterns(filename, start_date, end_date):
    """
    Analyzes weather data for a specific period to calculate average max 
    temperature and total precipitation.

    Args:
        filename (str): The name of the file containing weather data.
        start_date (tuple): A tuple (year, month, day) for the start of the period.
        end_date (tuple): A tuple (year, month, day) for the end of the period.

    Returns:
        dict: A dictionary where keys are city names and values are tuples:
              (number_of_records, avg_max_temp, total_precipitation).
    """
    stat_dict = {}
    city_dict = read_weather_data(filename)

    for city, records in city_dict.items():
        count = 0
        total_temp = 0
        total_precip = 0

        for record in records:
            date = record[0]
            max_temp = record[1]
            precip = record[3]

            if start_date <= date <= end_date:

                count += 1
                total_temp += max_temp
                total_precip += precip

        if count > 0:
            avg_max_temp = round(total_temp / count, 1)
            total_precip = round(total_precip,1)
            stat_dict[city] = (count, avg_max_temp, total_precip)

    return stat_dict

# analyze_weather_patterns('weather_logs.txt', (2023, 10, 3), (2023, 11, 15))

