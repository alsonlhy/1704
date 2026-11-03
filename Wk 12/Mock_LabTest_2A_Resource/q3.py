def process_numbers(input_filename, output_filename):

    with open(input_filename) as reading:
        with open(output_filename, 'w') as writing: 

            for line in reading: 
                line = line.rstrip("\n")
                groups = line.split("#")

                count = 0
                for group in groups: 

                    count += 1
                    number = group.split(" ")
                    

    print(groups)
    print(number)



                # writing.write(f"{count}: {avg}# \n")



process_numbers("numbers.txt", "output.txt")
