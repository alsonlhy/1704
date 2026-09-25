# q3b.py
# Name: 
# Email ID: 

from q3a import read_weather_data

def is_valid_date(a_date, start_date, end_date):
    year, month, day = a_date
    start_year, start_month, start_day = start_date
    end_year, end_month, end_day = end_date

    if start_year <= year <= end_year:
        if start_month <= month <= end_month:
            if start_day <= day <= end_day:
                return True
    return False
    

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
    
    dict_to_return = {}

    data_dict = read_weather_data(filename)
    for city in data_dict:
        sum_temp = 0
        tot_precipitation = 0
        counter = 0
        city_list = data_dict[city]
        for city_data in city_list:
            
            a_date = city_data[0]
            if is_valid_date(a_date, start_date, end_date):
                # handle max_temp
                max_data_temp = city_data[1]
                sum_temp += max_data_temp
                # handle precipitation
                data_precipitation = city_data[3]
                tot_precipitation += data_precipitation
                # increment counter
                counter += 1
        if counter > 0:   
            avg_max_temp = sum_temp / counter     
            dict_to_return[city] = (counter, round(avg_max_temp,1), round(tot_precipitation,1))

    return dict_to_return
