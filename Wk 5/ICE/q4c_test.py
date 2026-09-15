from q4c import concatenate_emails

print()
print('-' * 20)
print()

my_list1 = ["tommy.goh@scis.smu.edu.sg","alan_wong@gmail.com"]
print(concatenate_emails(my_list1))
my_list2 = []
print(concatenate_emails(my_list2))
my_list3 = ["COR-IS1704", "a @ b", "jerry.lee@scis.smu.edu.sg", "@@@", "alan_wong@gmail.com", "Python", "george_tan@yahoo.com"]
print(concatenate_emails(my_list3))

print()
print('-' * 20)
print()
