def to_minutes(hhmm):
    h, m = hhmm.split(':')
    return int(h) * 60 + int(m)

def get_exam_clashes(student_file, exam_file):
    exams = {}
    with open(exam_file) as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            course, day, start, end = line.split(',')
            exams[course] = (day, to_minutes(start), to_minutes(end))

    result = {}
    with open(student_file) as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            student, course_text = line.split(':')
            courses = course_text.split(',')
            pairs = []
            for i in range(len(courses)):
                for j in range(i + 1, len(courses)):
                    d1, s1, e1 = exams[courses[i]]
                    d2, s2, e2 = exams[courses[j]]
                    if d1 == d2 and s1 < e2 and s2 < e1:
                        pairs.append((courses[i], courses[j]))
            if pairs != []:
                result[student] = pairs
    return result
