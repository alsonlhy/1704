combos = (
    (1,80,300,0.1), 
    (2,200,500,2), 
    (3,300,1000,3), 
    (4,400,1500,4), 
    (5,800,2000,10)
    )


print("Please tell us your monthly usage requirements.\n")

calls = int(input("What's the minimum outgoing calls (in mins) you need? "))
sms = int(input("What's the minimum number of SMS/MMS you need? "))
data = float(input("What's the minimum amount of data (in GB) you need? "))

found_plan = None

for num, max_call, max_sms, max_data in combos:

    if calls < max_call and sms < max_sms and data < max_data:
        plan = num
        print(f"We recommend plan {num}")
        break

    else:
        print(f"Sorry! We don't have any plan that satisfies your requirements")
