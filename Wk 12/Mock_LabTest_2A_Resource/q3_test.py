from q3 import process_numbers

if __name__ == "__main__":
    print("Test Case for Q3")
    print()
    print("Expected: ")
    print("4: 20.0#250.0#-10.0#2.0\n3: 2000.0#40.0#5.0\nTotal number of groups: 7\nMaximum average: 2000.0\n")
    print('Actual:   ') 
    process_numbers("numbers.txt", "output.txt")
    try:
        with open('output.txt', 'r') as f:
            print(f.read())
    except:
        print('Unable to read output.txt')
