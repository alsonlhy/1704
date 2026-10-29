import q5a

file = 'spam_sms.txt'
cloud_dict = q5a.count_words_in_file(file)

top_list = []
max_freq = 0

cloud_list = list(cloud_dict.items())

sorted_cloud = sorted(cloud_dict.items(), key=lambda item: item[1])

print(sorted_cloud[:-11:-1])