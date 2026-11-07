# Name:
# Email ID:

def load_pokedex(filename):
    pokedex = []

    with open(filename) as fp:
        header = fp.readline().strip()
        field_names = header.split(",")

        for line in fp:
            line = line.strip()
            values = line.split(",")

            record = {}
            for i in range(len(field_names)):
                value = values[i]

                if value == "":
                    value = None
                elif value.isdigit():
                    value = int(value)
                elif value.count(".") == 1 and value.replace(".", "").isdigit():
                    value = float(value)
                # otherwise it stays as a string

                record[field_names[i]] = value

            pokedex.append(record)

    return pokedex