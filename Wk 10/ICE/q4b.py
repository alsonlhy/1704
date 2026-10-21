# Read the file once, at the start
headlines = []
with open('news.txt') as reading:
    for line in reading:
        headlines.append(line.rstrip('\n'))


def find_matches(headlines, keyword):
    keyword = keyword.lower()
    matches = []
    for headline in headlines:
        if keyword in headline.lower():
            matches.append(headline)
    return matches


answer = input("Do you want to search our news database? [Y|N] :")

while answer == "Y" or answer == "y":
    keyword = input("Please enter a keyword or a keyphrase :")
    matches = find_matches(headlines, keyword)

    print()
    if matches == []:
        print("There is no matching headline!")
    else:
        print(f"There are {len(matches)} matching headlines:")
        number = 1
        for headline in matches:
            print(f"\t{number}. {headline}")
            number += 1

    print()
    answer = input("Do you want to search again? [Y|N] :")

print("Good-bye!")