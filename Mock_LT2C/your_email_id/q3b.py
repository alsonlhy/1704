# Name:
# Email ID:


def get_rejected(filename):
    """
    Return {card: [(line_number, amount), ...]} for rejected payments.
    """
    rejected_dict = {}

    card_dict = {}
    count = 0
    with open (filename) as reading:

        for line in reading:
            count += 1
            line = line.rstrip("\n")
            columns = line.split(",")

            action = columns[0]
            card = columns[1]
            amt = float(columns[2])

            if card not in card_dict:
                card_dict[card] = 0.0

            

            if action == "TOPUP":
                card_dict[card] += amt

            elif action == "PAY":
                if card_dict[card] >= amt:
                    card_dict[card] -= amt

                else:
                    if card not in rejected_dict:
                        rejected_dict[card] = [(count,amt)]
                    else:
                        rejected_dict[card].append((count,amt))
                        
                
    return rejected_dict
