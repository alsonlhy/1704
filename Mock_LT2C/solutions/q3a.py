# Mock LT2C - Q3 Part A (solution)

def get_balances(filename):
    balances = {}
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            if line == '':
                continue
            action, card, amount = line.split(',')
            amount = float(amount)
            if card not in balances:
                balances[card] = 0.0       # a card appears the first time it is mentioned
            if action == 'TOPUP':
                balances[card] = round(balances[card] + amount, 2)
            elif amount <= balances[card]:  # PAY only if there is enough
                balances[card] = round(balances[card] - amount, 2)
            # otherwise the payment is rejected and the balance stays the same
    return balances
