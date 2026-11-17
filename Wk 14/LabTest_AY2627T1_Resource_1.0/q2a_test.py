from q2a import classify_messages

test_cases = [
        (['', 'URGENT: Meeting now', 'Where is GSR2?',
          'Please come to the meeting today', 'Meeting starts at 2 PM'], 
         [('', 'E'), ('URGENT: Meeting now', 'U'), ('Where is GSR2?', 'Q'),
          ('Please come to the meeting today', 'L'), ('Meeting starts at 2 PM', 'N')]
        ),
    
        (['URGENT: Can everyone attend the project meeting?'],
         [('URGENT: Can everyone attend the project meeting?', 'U')]
        ),
    
        (["URGENT-MESSAGE: Come now!"],
         [("URGENT-MESSAGE: Come now!", 'N')]
        ),
    
        (["URGENT-MESSAGE: Come now!!"],
         [("URGENT-MESSAGE: Come now!!", 'L')]
        ),
    
        (['Can everyone attend the meeting now?'],
         [('Can everyone attend the meeting now?', 'Q')]
        ),
    
        ([],
         []
        )
    ]


def run_test(ix, messages, classified_messages):
    print(f"\nTest Case {ix+1}: classified_messages('{messages}')")
    print("-------------------------------------------")
    
    result = classify_messages(messages)

    print('Expected type of returned value: ' + str(type(classified_messages)))
    print('Actual type of returned value:   ' + str(type(result)))
    print('Expected:', classified_messages)
    print('Actual:  ', result)
    
for ix, (messages, classified_messages) in enumerate(test_cases):
    run_test(ix, messages, classified_messages)
    
