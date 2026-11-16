# Mock Lab Test 2D — COR-IS1704 (final practice paper)

**25 marks · 1 hour 30 minutes**

Written for revision in the style of the 2023–26 Lab Test 2 papers. Not an official paper.

## Instructions

1. Work in the `your_email_id` folder. Rename the folder to your email ID, but **do not rename any `.py` file**.
2. Write each function in the file named in the question. Use the matching `qXX_test.py` to test it. The marker uses different test cases, so do not hard-code answers.
3. A file that does not run scores 0. If something is unfinished, comment it out or put `pass` under it before time is up.
4. Your functions must **return** the result. Do not `print` it.
5. Start the timer before you open Question 1. Look at `solutions/` only after you finish.

---

## Question 1  [8 marks]

### Part A (Difficulty *)  — `q1a.py`

A fitness app stores a user's daily step counts as a list of integers, one per day, in date order.

Implement `get_longest_streak(steps, goal)`.

- Return the length of the **longest run of consecutive days** on which the step count was **at least** `goal`.
- Return `0` if no day reaches the goal.
- Return `None` if `steps` is empty.

```python
steps = [8000, 12000, 10500, 3000, 11000, 10000, 10000, 2000]
get_longest_streak(steps, 10000)   # 3   (11000, 10000, 10000)
get_longest_streak(steps, 15000)   # 0
get_longest_streak([], 5000)       # None
```

### Part B (Difficulty **)  — `q1b.py`

Implement `compress(s)`. Replace every run of the same character in `s` with that character followed by the length of the run. If the run has length 1, write the character **without** a number.

- Upper and lower case are **different** characters.
- A run may be longer than 9.
- Return `''` if `s` is empty.

```python
compress('aaabccdddd')     # 'a3bc2d4'
compress('abc')            # 'abc'
compress('zzzzzzzzzzzz')   # 'z12'
compress('aAa')            # 'aAa'
```

---

## Question 2  [6 marks]

A library logs loans in a text file. The **first line is a header**. Each following line is `MEMBER,BOOK,BORROWED,RETURNED`:

```
MEMBER,BOOK,BORROWED,RETURNED
M01,The Hobbit,2026-11-01,2026-11-08
M02,Dune,2026-11-01,-
M01,Emma,2026-11-03,-
M03,Dune,2026-11-04,2026-11-05
M02,Ulysses,2026-11-06,2026-11-20
M01,Dracula,2026-11-07,-
```

`RETURNED` is `-` if the book has not been returned yet. Book titles never contain commas. The file may contain only the header.

### Part A (Difficulty *)  — `q2a.py`

Implement `get_unreturned(filename)`. Return a list of tuples `(member, book)` for every loan that has not been returned, in file order. Return `[]` if there are none.

```python
get_unreturned('loans-1.txt')
# [('M02', 'Dune'), ('M01', 'Emma'), ('M01', 'Dracula')]
```

### Part B (Difficulty **)  — `q2b.py`

Implement `get_member_summary(filename)`. Return a dictionary `{member: (num_loans, num_unreturned)}` with members in the order they first appear in the file. Return `{}` if there are no loans.

```python
get_member_summary('loans-1.txt')
# {'M01': (3, 2), 'M02': (2, 1), 'M03': (1, 0)}
```

---

## Question 3  [5 marks]

A car park records every entry and exit in a log file, in time order, as `HH:MM,ACTION,PLATE` where `ACTION` is `IN` or `OUT`:

```
08:00,IN,SGA1234A
08:05,IN,SKB88C
08:12,OUT,SKB88C
09:00,IN,SKB88C
09:31,OUT,SGA1234A
10:30,OUT,SKB88C
11:00,IN,SLM7X
11:00,OUT,FBX999Z
12:00,IN,SGA1234A
12:30,OUT,SGA1234A
```

Rules:

- A **stay** is an `IN` followed later by an `OUT` for the same plate. A plate can have several stays.
- An `OUT` for a plate that is not currently inside is **ignored** (e.g. `FBX999Z`).
- A plate that is still inside at the end of the file has no completed stay for that visit (e.g. `SLM7X`).
- Fee for one stay: if the stay is **10 minutes or less**, it is free. Otherwise, charge **$0.60 for every 30 minutes or part thereof** of the **whole** stay. For example, 31 minutes is 2 blocks ($1.20), and 60 minutes is 2 blocks ($1.20).
- All times are on the same day. The file may be empty.

### Part A (Difficulty **)  — `q3a.py`

Implement `get_fees(filename)`. Return a dictionary `{plate: total_fee}` for every plate with **at least one completed stay** (even if all its stays were free). `total_fee` is a float rounded to 2 decimal places. Plates appear in the order of **their first completed stay**. Return `{}` if there are no completed stays.

```python
get_fees('carpark-1.txt')   # {'SKB88C': 1.8, 'SGA1234A': 3.0}
```

(SKB88C: 7 min free, then 90 min = 3 blocks. SGA1234A: 91 min = 4 blocks, then 30 min = 1 block.)

### Part B (Difficulty \*\*/\*\*\*)  — `q3b.py`

Implement `get_longest_stay(filename)`. Return a tuple `(plate, minutes)` for the longest single completed stay. If several stays are equally long, return the one that **ended earliest** in the file. Return `None` if there are no completed stays.

```python
get_longest_stay('carpark-1.txt')   # ('SGA1234A', 91)
get_longest_stay('carpark-3.txt')   # ('A1', 80)
```

---

## Question 4  [6 marks]

### Part A (Difficulty ***)  — `q4a.py`

An exam file lists one exam per line as `COURSE,DAY,START,END` (24-hour `HH:MM`):

```
IS111,MON,09:00,11:00
IS112,MON,10:30,12:30
IS113,MON,13:00,15:00
COR1100,MON,11:00,13:00
IS114,TUE,09:00,11:00
COR2100,WED,09:00,12:00
```

A student file lists one student per line as `STUDENT:COURSE,COURSE,...`:

```
Ann:IS111,IS112,COR1100
Ben:IS113,IS114
Cal:COR1100,IS112,IS113,COR2100
Dee:IS111
```

An exam runs from `START` up to but **not including** `END`. Two of a student's exams **clash** if they are on the **same day** and their times overlap. Every course a student takes has exactly one exam in the exam file. Either file may be empty.

Implement `get_exam_clashes(student_file, exam_file)`. Return a dictionary `{student: [(course_a, course_b), ...]}`:

- Include only students with at least one clash, in the order they appear in the student file.
- `course_a` comes before `course_b` in **that student's** list of courses. Order the pairs by the position of `course_a`, then `course_b`, in that list.
- Return `{}` if no student has a clash.

```python
get_exam_clashes('students-1.txt', 'exams-1.txt')
# {'Ann': [('IS111', 'IS112'), ('IS112', 'COR1100')], 'Cal': [('COR1100', 'IS112')]}
```

(IS111 ends at 11:00 when COR1100 starts, so they do not clash.)

### Part B (Difficulty ***)  — `q4b.py`

A career fair runs workshops. Each line of a workshop file is `ID,START,END,POINTS`:

```
W1,09:00,10:00,5
W2,09:30,11:00,8
W3,10:00,11:00,4
W4,11:00,12:30,6
W5,12:00,13:00,7
W6,10:45,11:15,3
```

A workshop runs from `START` up to but **not including** `END`. A student earns `POINTS` for each workshop attended and cannot attend two workshops that overlap. All workshops are on the same day. The file has at most 12 workshops and may be empty.

Implement `get_best_workshops(filename)`. Return a tuple `(total_points, ids)`:

- `total_points` (int): the largest total points the student can earn.
- `ids` (list): the IDs of the chosen workshops, **sorted alphabetically**.
- If several choices give the same total, choose the one with the **fewest workshops**. If still tied, choose the one whose sorted `ids` list is smallest (compare the lists with `<`).
- Return `(0, [])` for an empty file.

```python
get_best_workshops('workshops-1.txt')   # (16, ['W1', 'W3', 'W5'])
get_best_workshops('workshops-2.txt')   # (15, ['D'])
```

**— END OF PAPER —**
