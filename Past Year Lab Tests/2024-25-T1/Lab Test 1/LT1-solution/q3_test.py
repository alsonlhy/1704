from q3 import process_patient_data

def test_case(i, data, expected):
    print()
    print('-' * 20)
    print()
    print(f"Test Case {i}: process_patient_data({patients})")
    print()
    result = process_patient_data(patients)
    print('Expected: ', expected)
    print('Actual:   ', result)
    
patients = [
    ("John Doe", 45, "Male", ["Diabetes"], True),
    ("Jane Smith", 38, "Female", ["Hypertension", "Asthma"], False),
    ("Sam Brown", 60, "Male", ["Asthma"], True),
    ("Anna White", 29, "Female", ["Allergy"], True)
]
expected = (43.0, 2, 2, 3, ["Diabetes", "Hypertension", "Asthma", "Allergy"])
test_case(1, patients, expected)

patients = [ ("Alice Blue", 40, "Female", ["Asthma"], True),
             ("Bob Green", 55, "Male", ["Diabetes"], True),
             ("Sam Lee", 30, "Male", ["Diabetes", "Hypertension", "Asthma"], True) ]
expected = (41.67, 2, 1, 3, ["Asthma", "Diabetes", "Hypertension"])
test_case(2, patients, expected)

patients = [
    ("Alice Blue", 40, "Not Specified", [], True),
    ("Bob Green", 55, "Not Specified", [], True),
    ("Sam Lee", 30, "Male", ["Asthma"], False)
]
expected = (41.67, 1, 0, 2, ["Asthma"])
test_case(3, patients, expected)
