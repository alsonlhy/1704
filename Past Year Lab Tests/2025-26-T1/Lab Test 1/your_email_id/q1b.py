# Name:
# Email ID:

# def compute_plan_cost(plan, data_used):

#     cost = 0
#     if plan == "Lite":

#         if data_used <= 100:
#             cost = 10

#         else:
#             cost = 10 + (data_used - 100)*5

#     elif plan == "Standard":

#         if data_used <= 300:
#             cost = 20

#         else:
#             cost = 20 + (data_used - 300)*3

#     elif plan == "Pro":

#         if data_used <= 900:
#             cost = 50

#         else:
#             cost = 50 + (data_used - 900)*1

#     else:
#         return "Invalid plan selected"

#     return round(cost,2)
   









def compute_plan_cost(plan, data_used):

    cost = 0
    data_plan = {}
    data_plan["Lite"] = [10, 100, 5]
    data_plan["Standard"] = [20,300,3]
    data_plan["Pro"] = [50,900,1]

    if plan in data_plan:
        pricing = data_plan[plan]
        if data_used <= pricing[1]:
            cost = pricing[0]
        else:
            cost = pricing[0] + (data_used-pricing[1])*pricing[2]

    else:
        return "Invalid plan selected"

    return round(cost,2) 
    

