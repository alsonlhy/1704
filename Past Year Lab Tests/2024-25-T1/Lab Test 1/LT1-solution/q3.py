# Name:
# Email ID:

def process_patient_data(patients):
    # Replace the code below with your implementation.
    tot_age = 0
    num_males = 0
    num_females = 0
    num_discharged = 0
    unique_ailments = []
    
    for patient in patients:
        age = patient[1]
        gender = patient[2]
        ailments_list = patient[3]
        is_discharged = patient[4]
        # alternatively
        # name, age, gender, ailments_list, is_discharged = patient
        
        tot_age += age
        
        if gender == "Male":
            num_males += 1
        elif gender == "Female":
            num_females += 1
         
        if is_discharged:
            num_discharged +=1

        for ailment in ailments_list:
            if ailment not in unique_ailments:
                unique_ailments.append(ailment)
                    
    avg_age = round(tot_age / len(patients), 2)
    return (avg_age, num_males, num_females, num_discharged, unique_ailments)

    
