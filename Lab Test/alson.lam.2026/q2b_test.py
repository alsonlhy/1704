from q2b import verify_tags
 
test_cases = [
              # Test Case 1: Mixed batch, order preserved:
              #   TBRTB246E - valid
              #   GGHGH081O - 2 distinct letters only
              #   WXYZQ600O - parity wrong only
              #   AAAAA053E - both checks fail (1 distinct letter AND wrong parity)
              (['TBRTB246E', 'GGHGH081O', 'WXYZQ600O', 'AAAAA053E'],
              [('TBRTB', 246, True), ('GGHGH', 81, False), ('WXYZQ', 600, False), ('AAAAA', 53, False)]),
 
              # Test Case 2: Empty list
              ([],
               [])
              ]
 
def run_test(ix, tags, exp):
    print(f"\nTest Case {ix+1}: verify_tags({tags})")
    print("-------------------------------------------")
 
    result = verify_tags(tags)
 
    print('Expected type of returned value: ' + str(type(exp)))
    print('Actual type of returned value:   ' + str(type(result)))
    print('Expected:', exp)
    print('Actual:  ', result)
 
for ix, (tags, expected) in enumerate(test_cases):
    run_test(ix, tags, expected)