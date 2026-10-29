import q5a

file = 'spam_sms.txt'
cloud_dict = q5a.count_words_in_file(file)

for key in cloud_dict:

    if len(key) >= 4 and cloud_dict[key] > 50:
        print(f"{key} : {cloud_dict[key]}")