from q1 import get_hashtags

print('Test Case 1')
print('Expected:', ['#smukitty', '#smucat', '#Meow', '#TeamGrumpy', '#GrumpyCat', '#Meow', '#grumpycat'])
result = get_hashtags(["#smukitty #smucat #Meow If you see me around school please approach me slowly cos I am very shy and get scared easily", "The Official Instagram for Grumpy Cat. #TeamGrumpy #GrumpyCat", "#Meow Definitely not a #grumpycat"])
print('Actual:  ', result)
print()

print('Test Case 2')
print('Expected:', [])
result = get_hashtags(["I'm writing a book. I've got the page numbers done.", "When nothing is going right, go left."])
print('Actual:  ', result)
print()

print('Test Case 3')
print('Expected:', ['#SCIS', '#Classof2022', '#Computing', '#SCIS'])
result = get_hashtags(["SMU #SCIS congratulates the #Classof2022 graduates for their accomplishments", "#Computing at #SCIS"])
print('Actual:  ', result)
print()

print('Test Case 4')
print('Expected:', [])
result = get_hashtags(["A balanced diet means a cupcake in each hand.", "I'm never wrong. Just different levels of right."])
print('Actual:  ', result)
print()