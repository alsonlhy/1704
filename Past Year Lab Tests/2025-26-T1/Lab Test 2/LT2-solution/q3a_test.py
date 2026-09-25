
from q3a import read_weather_data

def run_test_case(tc_num, filename, expected_output, expected_type):
    print('*'*40)
    print(f'Test Case {tc_num}: read_weather_data("{filename}")')
    print()
    print(f'Expected: {expected_output}')
    result = read_weather_data(filename)
    print(f'Actual:   {result}')
    print()
    print(f'Expected return type : {expected_type}')
    print(f"Actual return type   : {type(result)}")
    print()
    print(f'Is the returned dictionary the same as expected? {expected_output == result}')

expected_output = {
    'Rivertown': [((2023, 10, 1), 25.5, 15.1, 0.0), ((2023, 10, 2), 24.9, 14.0, 5.5)], 
    'Sunnyvale': [((2023, 11, 15), 19.9, 8.5, 10.2), ((2023, 10, 1), 28.1, 16.3, 0.0), ((2023, 11, 16), 18.5, 7.9, 12.1), ((2023, 10, 2), 27.5, 15.8, 2.1)]
}
run_test_case(1, 'weather_logs.txt', expected_output, "<class 'dict'>")
