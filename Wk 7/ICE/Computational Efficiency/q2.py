def student_search(students, criteria, criteria_indices):

    matched_students = []

    for student in students:

        is_match = True

        for i in range(len(criteria)):

            target_val = criteria[i]
            student_val = student[criteria_indices[i]]

            if type(student_val) == str and type(target_val) == str:
                if student_val.lower() != target_val.lower():

                    is_match = False
                    break

            elif student_val != target_val:
                        is_match = False
                        break

            if is_match:
                matched_students.append(student)

    return matched_students

students = [
    ["Alice", 20, "A"],
    ["Bob", 22, "B"],
    ["Charlie", 20, "A"],
    ["David", 23, "C"]
]
criteria = ["A", 20]
criteria_indices = [2, 1]  # Indices corresponding to grade and age
print(student_search(students, criteria, criteria_indices))
