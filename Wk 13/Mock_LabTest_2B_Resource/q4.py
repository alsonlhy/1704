def get_document_pair(filename):

    extracted_dict = {}
    with open (filename) as reading:

        for line in reading:
            line = line.rstrip("\n")
            columns = line.split("\t")

            id = columns[0]
            words = set(columns[1].split(" "))

            extracted_dict[id] = words

    doc_id = list(extracted_dict.keys())

        # for i in range(0, len(id)-1):
        #     for j in range(i+1, len(id)):




    print(doc_id)


get_document_pair('documents.txt')



