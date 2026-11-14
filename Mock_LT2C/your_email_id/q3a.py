# Name:
# Email ID:

def get_balances(filename):
    """
    Return {card: final balance} after processing every line.
    """
    card_dict = {}
    with open (filename) as reading:

        for line in reading:
            line = line.rstrip("\n")
            columns = line.split(",")

            action = columns[0]
            card = columns[1]
            amt = float(columns[2])

            if card not in card_dict:
                card_dict[card] = 0.0

            

            elif action == "TOPUP":
                card_dict[card] += amt

            elif action == "PAY":
                if card_dict[card] >= amt:
                    card_dict[card] -= amt
                
    
    return card_dict
