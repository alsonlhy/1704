# Name:
# Email ID:

def compute_plan_cost(plan, data_used):
    # Modify the code below.
    # Define the base fee, quota, and extra rate for each plan
    if plan == 'Lite':
        base_fee = 10
        quota = 100
        extra_rate = 5
    elif plan == 'Standard':
        base_fee = 20
        quota = 300
        extra_rate = 3
    elif plan == 'Pro':
        base_fee = 50
        quota = 900
        extra_rate = 1
    else:
        return 'Invalid plan selected'
    
    if data_used > quota:
        extra_data = data_used - quota
        total_cost = base_fee + extra_data * extra_rate
    else:
        total_cost = base_fee
    
    return round(total_cost, 2)
