# Name:
# Email ID:

def process_patient_data(patients):

    total_age = 0
    patient_num = len(patients)

    male_count = 0
    female_count = 0
    discharged_count = 0
    uniq_ailments = []

    for tup in patients:

        total_age += tup[1]

        if tup[2] == "Male":
            male_count += 1

        elif tup[2] == "Female": 
            female_count += 1

        if tup[4]:
            discharged_count += 1

        for types in tup[3]:

            if types not in uniq_ailments:
                uniq_ailments.append(types)
        

    avg_age = total_age / patient_num
    
    return (round(avg_age, 2), male_count, female_count, discharged_count, uniq_ailments)

    

