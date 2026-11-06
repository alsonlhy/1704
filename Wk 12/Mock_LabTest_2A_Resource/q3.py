def process_numbers(input_filename, output_filename):
    total_groups = 0
    max_average = None

    with open(input_filename) as reading:
        with open(output_filename, 'w') as writing:
            for line in reading:
                line = line.strip()
                groups = line.split("#")

                averages = ""
                for group in groups:
                    numbers = group.split()

                    total = 0
                    for number in numbers:
                        total += float(number)

                    average = round(total / len(numbers), 1)

                    if max_average is None or average > max_average:
                        max_average = average

                    if averages != "":
                        averages += "#"
                    averages += str(average)

                total_groups += len(groups)
                writing.write(f"{len(groups)}: {averages}\n")

            writing.write(f"Total number of groups: {total_groups}\n")
            writing.write(f"Maximum average: {max_average}\n")