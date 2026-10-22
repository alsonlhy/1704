def extract_functions(py_filename, output_filename):

    def_list = []
    count = 1

    with open(py_filename) as reading:
        with open(output_filename, 'w') as writing:

            for line in reading:

                line = line.rstrip('\n')
                if "def" in line:
                    writing.write(line[4:-1] + '\n')

                elif line[4:-1].isalpha():
                    writing.write(line[4:-1] + '\n')

                elif '    """' in line:

                    if line[7:-1] == "" or line[7:-1] == " ":
                        pass

                    else:
                        writing.write(line[7:-1] + '\n')


extract_functions('python_script.py', 'q6-output.txt')