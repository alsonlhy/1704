from q3b import station_balance

test_cases = [
    ('bike_trips.txt', '08:00', '09:00',
     {'MBS': (2, 1, -1), 'SMU': (2, 1, -1), 'Stadium': (1, 1, 0)}),

    ('bike_trips.txt', '09:00', '10:00',
     {'MBS': (2, 2, 0), 'Stadium': (1, 0, -1), 'SMU': (1, 1, 0)}),

    ('bike_trips.txt', '10:00', '10:15',
     {'Stadium': (0, 1, 1), 'MBS': (0, 1, 1)}),

    ('bike_trips.txt', '11:00', '12:00',
     {}),
]

for ix, (fname, window_start, window_end, expected) in enumerate(test_cases):
    print(f"\nTest Case {ix+1}: station_balance('{fname}', '{window_start}', '{window_end}')")
    print("-------------------------------------------")
    result = station_balance(fname, window_start, window_end)
    print('Expected:', expected)
    print('Actual:  ', result)

