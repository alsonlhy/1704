## Q5a Word Counts
# write your code below

def count_words_in_file(filename):

    cloud_dict = {}
    with open (filename) as reading:



        for line in reading: 
            line = line.rstrip("\n")
            words = line.lower().split()

            

            for word in words:
                if word not in cloud_dict:
                    cloud_dict[word] = 1

                else:
                    
                    cloud_dict[word] += 1

    return cloud_dict
            

