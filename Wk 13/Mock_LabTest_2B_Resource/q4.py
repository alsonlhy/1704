def get_document_pair(filename):

    extracted_dict = {}
    with open (filename) as reading:

        for line in reading:
            line = line.rstrip("\n")
            columns = line.split("\t")

            id = columns[0]
            raw_words = columns[1].split(" ")

            unique_words = []
            for word in raw_words:
                if word not in unique_words:
                    unique_words.append(word)

            extracted_dict[id] = unique_words

    doc_id = list(extracted_dict.keys())

    max_common = -1
    best_pair = ("", "")

    for i in range(0, len(doc_id)-1):
        for j in range(i+1, len(doc_id)):
            id1 = doc_id[i]
            id2 = doc_id[j]

            words1 = extracted_dict[id1]
            words2 = extracted_dict[id2]

            common_count = 0
            for word in words1:
                if word in words2:
                    common_count += 1


            if common_count > max_common:
                max_common = common_count
                best_pair = (id1, id2)

    return (best_pair[0], best_pair[1], max_common)



