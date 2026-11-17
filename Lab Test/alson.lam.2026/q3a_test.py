from q3a import bike_usage

test_cases = [
    ('bike_trips.txt', {'B07': [3, 72], 'B03': [2, 45], 'B11': [2, 40], 'B05': [1, 20]})
]

for ix, (fname, expected) in enumerate(test_cases):
    print(f"\nTest Case {ix+1}: bike_usage('{fname}')")
    print("-------------------------------------------")
    result = bike_usage(fname)
    print('Expected:', expected)
    print('Actual:  ', result)

