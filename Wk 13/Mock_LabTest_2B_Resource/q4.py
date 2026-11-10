def get_document_pair(filename):

    extracted = []
    with open (filename) as reading:

        for line in reading:
            line = line.rstrip("\n")
            columns = line.split("\t")

            id = columns[0]
            words = columns[1].split(" ")
            extracted.append([id, words])


    uniq_word = []
    for lst in extracted:
        words = lst[1]

        for word in words:

            if word not in uniq_word:
                uniq_word.append(word)

    return uniq_word


print(get_document_pair("documents.txt"))

