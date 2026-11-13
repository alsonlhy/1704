# Mock LT2C - Q3 Part B (solution)

def get_rejected(filename):
    balances = {}
    rejected = {}
    line_no = 0
    with open(filename) as f:
        for line in f:
            line_no += 1                   # count EVERY line, accepted or not
            line = line.rstrip('\n')
            if line == '':
                continue
            action, card, amount = line.split(',')
            amount = float(amount)
            if card not in balances:
                balances[card] = 0.0
            if action == 'TOPUP':
                balances[card] = round(balances[card] + amount, 2)
            elif amount <= balances[card]:
                balances[card] = round(balances[card] - amount, 2)
            else:
                if card not in rejected:
                    rejected[card] = []
                rejected[card].append((line_no, amount))
    return rejected
