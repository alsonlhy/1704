# Name:
# Email ID:

def read_data(filename):
    transactions = {}
    with open(filename) as f:
        data = f.read()
    
    for line in data.strip().split('\n'):
        parts = line.split('|')
        tx_id = parts[0]
        
        inputs = []
        for p in parts:
            if p.startswith("IN"):
                inputs.append(p[3:])

        outputs = []
        for p in parts:
            if p.startswith("OUT"):
                outputs.append(p[4:])

        transactions[tx_id] = (inputs, outputs)
    return transactions

def get_invalid_transactions(filename):
    transactions = read_data(filename)
    
    valid_outputs = []
    invalid_transactions = []
    
    for key in transactions:
        tx_id = key
        inputs = transactions[key][0]
        outputs = transactions[key][1]
        valid = True
        is_coinbase = False

        # check inputs validity
        for input in inputs:
            if input.startswith('COINBASE'):
                valid_outputs.append(outputs[0]) # only 1 output
                is_coinbase = True
            else:
                # check inputs not enough given the existing valid outputs
                count_outputs = valid_outputs.count(input)
                count_inputs = inputs.count(input)
                if count_outputs < count_inputs:
                    valid = False
                    if tx_id not in invalid_transactions:
                        invalid_transactions.append(tx_id)
                    break
        
        # remove the spent outputs one by one
        # add new valid outputs which are not coinbase (coinbase outputs already added)
        if valid and not is_coinbase:
            for input in inputs:
                for i in range(len(valid_outputs)):
                    if valid_outputs[i] == input:
                        valid_outputs = valid_outputs[:i] + valid_outputs[i+1:]
                        break
            for output in outputs:
                valid_outputs.append(output)
    return invalid_transactions