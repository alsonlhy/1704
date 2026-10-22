def extract_functions(py_filename, output_filename):

    in_docstr = False
    count = 0

    with open(py_filename) as reading:
        with open(output_filename, 'w') as writing:

            for line in reading:

                line = line.rstrip('\n')

                if not in_docstr and line.startswith("def "):
                    count += 1
                    writing.write(f"{count}. {line[4:-1]}\n")

                elif in_docstr or line.startswith('    """'):
                    text = line.replace('"""', '')
                    if text.strip() != "":
                        writing.write(text + "\n")

                    if line.count('"""') % 2 == 1: 
                        in_docstr = not in_docstr

                    if not in_docstr:
                        writing.write('\n')


extract_functions('python_script.py', 'q6-output.txt')

