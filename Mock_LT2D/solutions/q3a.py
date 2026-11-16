def to_minutes(hhmm):
    h, m = hhmm.split(':')
    return int(h) * 60 + int(m)

def stay_fee(minutes):
    if minutes <= 10:
        return 0.0
    blocks = (minutes + 29) // 30             # "30 minutes or part thereof"
    return blocks * 0.60

def get_fees(filename):
    inside = {}                               # plate -> entry time
    fees = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            time, action, plate = line.split(',')
            t = to_minutes(time)
            if action == 'IN':
                inside[plate] = t
            elif plate in inside:             # OUT with no IN is ignored
                minutes = t - inside.pop(plate)
                fees[plate] = round(fees.get(plate, 0.0) + stay_fee(minutes), 2)
    return fees
