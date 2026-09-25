
from q3b import analyze_weather_patterns

def run_test_case(tc_num, filename, start, end, expected_output, expected_type):
    print('*'*40)
    print(f'Test Case {tc_num}: analyze_weather_patterns("{filename}", {start}, {end})')
    print()
    print(f'Expected: {expected_output}')
    result = analyze_weather_patterns(filename, start, end)
    print(f'Actual:   {result}')
    print()
    print(f'Expected return type : {expected_type}')
    print(f"Actual return type   : {type(result)}")
    print()
    print(f'Is the returned dictionary the same as expected? {expected_output == result}')

# Test Case 1: Analyzing the month of November
expected_output = {'Sunnyvale': (2, 19.2, 22.3)}
run_test_case(1, 'weather_logs.txt', (2023, 11, 1), (2023, 11, 30), expected_output, "<class 'dict'>")

# Test Case 2: Analyzing the month of October
expected_output = {'Rivertown': (2, 25.2, 5.5), 'Sunnyvale': (2, 27.8, 2.1)}
run_test_case(2, 'weather_logs.txt', (2023, 10, 1), (2023, 10, 31), expected_output, "<class 'dict'>")

# Test Case 3: Analyzing a single day
expected_output = {'Rivertown': (1, 25.5, 0.0), 'Sunnyvale': (1, 28.1, 0.0)}
run_test_case(3, 'weather_logs.txt', (2023, 10, 1), (2023, 10, 1), expected_output, "<class 'dict'>")

# Test Case 4: Analyzing the entire date range in the file
expected_output = {'Rivertown': (2, 25.2, 5.5), 'Sunnyvale': (4, 23.5, 24.4)}
run_test_case(4, 'weather_logs.txt', (2023, 1, 1), (2023, 12, 31), expected_output, "<class 'dict'>")

# Test Case 5: Analyzing a date range that spans months
expected_output = {'Sunnyvale': (1, 19.9, 10.2)}
run_test_case(5, 'weather_logs.txt', (2023, 10, 3), (2023, 11, 15), expected_output, "<class 'dict'>")
