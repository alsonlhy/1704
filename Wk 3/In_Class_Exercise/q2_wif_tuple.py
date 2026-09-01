def get_day_of_week(num):
    days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

    if num > 6:
        return "Number should be at most 6"
    elif num < 0:
        return "Number should be at least 0"
    return days[num]

get_num = int(input("Enter a number indicating the day of a week [0 to 6]: "))

date = get_day_of_week(get_num)

print(date)