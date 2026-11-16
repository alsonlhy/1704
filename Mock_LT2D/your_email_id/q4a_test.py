from q4a import get_exam_clashes

if __name__ == '__main__':
    print('Test cases for Q4A')
    print('-' * 20)
    print('Test case 1: get_exam_clashes("students-1.txt", "exams-1.txt")')
    print('Expected:', {'Ann': [('IS111', 'IS112'), ('IS112', 'COR1100')], 'Cal': [('COR1100', 'IS112')]})
    print('Actual:  ', get_exam_clashes('students-1.txt', 'exams-1.txt'))
    print()
    print('Test case 2: get_exam_clashes("students-2.txt", "exams-1.txt")')
    print('Expected:', {})
    print('Actual:  ', get_exam_clashes('students-2.txt', 'exams-1.txt'))
    print()
