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

            action = columns[0].strip()
            card = columns[1].strip()
            amt = float(columns[2].strip())

            if card not in card_dict:
                card_dict[card] = 0.0

            

            if action == "TOPUP":
                card_dict[card] = round(card_dict[card] + amt, 2)

            elif action == "PAY":
                if card_dict[card] >= amt:
                    card_dict[card] = round(card_dict[card] - amt, 2)
                
    
    return card_dict
