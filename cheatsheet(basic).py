# =====================================================================
#  COR-IS1704 LAB TEST - SHORT CHEAT SHEET
#  Only the patterns that keep coming back in LT1/LT2 (2023-2026).
#  COPY the function into your qXX.py and rename it. Never import this file.
#  Lines with  # <--  are the ones you normally change.
# =====================================================================


# ---------------------------------------------------------------------
# 1. ROUNDING (cost marks every year)
# ---------------------------------------------------------------------
#   int(41602.9)     -> 41602   "round DOWN to nearest dollar"
#   round(3.567, 2)  -> 3.57    "round to 2 decimal places"
#   round(62.5)      -> 62      .5 goes to the EVEN number
#   f"{x:.2f}"       -> '3.50'  only for printing


# ---------------------------------------------------------------------
# 2. PRIME (no sympy)
# ---------------------------------------------------------------------
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
# primes in a range:  [n for n in range(a, b + 1) if is_prime(n)]


# ---------------------------------------------------------------------
# 3. TIERED PRICE / RULE TABLE  (LT1 Q1 every year: parking, plans, tax)
# ---------------------------------------------------------------------
def plan_cost(plan, used):
    PLANS = {'Lite': (10, 100, 5),          # <-- name: (fee, quota, rate over quota)
             'Standard': (20, 300, 3),
             'Pro': (50, 900, 1)}
    if plan not in PLANS:
        return 'Invalid plan selected'      # <-- message
    fee, quota, rate = PLANS[plan]
    if used <= quota:
        return fee
    return round(fee + (used - quota) * rate, 2)


def band(value, bands, default):
    """bands = [(limit, answer), ...] checked in order; first match wins.
    'not exceeding X' -> ascending limits with <=   (PARF %: band(yrs, [(5,.75),(6,.7)...], None))
    'at least X'      -> use >= and descending limits"""
    for limit, answer in bands:
        if value <= limit:                  # <-- <= / < / >= / >
            return answer
    return default


# ---------------------------------------------------------------------
# 4. STRING LOOPS
# ---------------------------------------------------------------------
def count_chars(s, chars='aeiouAEIOU'):     # <-- vowels / '0123456789' / specials
    count = 0
    for ch in s:
        if ch in chars:
            count += 1
    return count
# other tests: ch.isdigit()  ch.isalpha()  ch.isupper()  ch.islower()  ch.isalnum()


def pick_chars(s):
    """Digits at even indexes: 'SMU-1-2-3-4' -> '1234'"""
    out = ''
    for i in range(0, len(s), 2):           # <-- start/step
        if s[i].isdigit():                  # <-- condition
            out += s[i]
    return out


def split_many(text, seps='!?,.:;'):
    """'apple;banana:cherry' -> ['apple', 'banana', 'cherry']"""
    for sep in seps:
        text = text.replace(sep, ' ')
    return text.split()


def alternate(s1, s2):
    """'abcde','123' -> 'a1b2c3ed' (leftover reversed; drop [::-1] if not)"""
    out = ''
    n = min(len(s1), len(s2))
    for i in range(n):
        out += s1[i] + s2[i]
    return out + (s1[n:] + s2[n:])[::-1]


def replace_at(s, i, ch):
    """Strings can't be changed in place: replace_at('---', 1, 'x') -> '-x-'"""
    return s[:i] + ch + s[i + 1:]


# ---------------------------------------------------------------------
# 5. LIST OF TUPLES (Q2/Q3 every year)
# ---------------------------------------------------------------------
def stats(records):
    """records like (name, age, gender, [ailments], discharged).
    Shows: filter, sum/avg, count, max with tie rule, unique-in-order."""
    if records == []:
        return None                         # <-- whatever empty case asks
    total = 0
    count_male = 0
    best = records[0]
    unique = []
    for rec in records:
        total += rec[1]                     # <-- field to sum
        if rec[2] == 'Male':                # <-- condition to count
            count_male += 1
        if rec[1] > best[1]:                # > keeps FIRST on tie, >= takes LAST
            best = rec
        for item in rec[3]:                 # unique items, first-seen order
            if item not in unique:
                unique.append(item)
    avg = round(total / len(records), 2)
    return (avg, count_male, best[0], unique)


def counts_no_dict(records, cat_index, cats):
    """Per-category counts when dicts are BANNED. Fixed order of cats."""
    counts = [0] * len(cats)
    for rec in records:
        for i in range(len(cats)):
            if rec[cat_index] == cats[i]:
                counts[i] += 1
    return tuple(counts)
# best average per category: keep sums=[0]*n and counts=[0]*n the same way,
# then loop i, avg = sums[i]/counts[i] (skip counts[i]==0), track the max.


# ---------------------------------------------------------------------
# 6. FILES (every LT2)
# ---------------------------------------------------------------------
def read_file(filename):
    """Template: returns list of typed tuples."""
    records = []
    with open(filename) as f:
        # f.readline()                      # <-- uncomment if there is a header
        for line in f:
            line = line.rstrip('\n')
            if line == '':
                continue
            cols = line.split(',')          # <-- ',' '\t' '|' '!' '**'
            name = cols[0]
            qty = int(cols[1])                              # <-- types
            price = float(cols[2].strip().lstrip('$'))      # '$12.50' -> 12.5
            records.append((name, qty, price))
    return records


def file_to_dict_of_lists(filename):
    """{key: [rows...]} in file order - e.g. city -> its weather records."""
    result = {}
    with open(filename) as f:
        for line in f:
            cols = line.rstrip('\n').split('|')             # <--
            key = cols[1]                                   # <--
            if key not in result:
                result[key] = []
            result[key].append((cols[0], float(cols[2])))   # <--
    return result


def count_and_avg(filename, name, event):
    """Rows matching conditions -> (count, average); (0, 0) if none."""
    total = 0
    count = 0
    with open(filename) as f:
        for line in f:
            cols = line.rstrip('\n').split(',')
            if cols[0] == name and cols[1] == event:        # <-- conditions
                total += int(cols[2])
                count += 1
    if count == 0:
        return (0, 0)
    return (count, round(total / count))


def to_value(text):
    """Auto type: '' -> None, '12' -> 12, '0.7' -> 0.7, else str (header-file questions)."""
    if text == '':
        return None
    if text.isdigit():
        return int(text)
    if text.count('.') == 1 and text.replace('.', '').isdigit():
        return float(text)
    return text
# header -> dict:  keys = f.readline().rstrip('\n').split(',')
#                  for each line: d = {}; for i in range(len(keys)): d[keys[i]] = to_value(cols[i])


# ---------------------------------------------------------------------
# 7. DICT COUNT + DATES
# ---------------------------------------------------------------------
def frequency(items):
    counts = {}
    for x in items:
        if x not in counts:
            counts[x] = 0
        counts[x] += 1
    return counts


def in_range(date_text, start, end):
    """'2023-10-01' vs (y, m, d) tuples. Tuples compare correctly - don't check y/m/d separately."""
    y, m, d = date_text.split('-')
    return start <= (int(y), int(m), int(d)) <= end


# ---------------------------------------------------------------------
# quick self-check: python cheatsheet.py
# ---------------------------------------------------------------------
if __name__ == '__main__':
    assert [n for n in range(20) if is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19]
    assert plan_cost('Standard', 333.33) == 119.99 and plan_cost('Basic', 1) == 'Invalid plan selected'
    assert int(9370 * band(578 / 365, [(5, .75), (6, .70), (7, .65), (8, .60), (9, .55), (10, .50)], 0)) == 7027
    assert count_chars('Has anyone seen Morbo?') == 8
    assert pick_chars('SMU-1-2-3-4') == '1234'
    assert split_many('Hello!world?Python,rocks') == ['Hello', 'world', 'Python', 'rocks']
    assert alternate('abcde', '123') == 'a1b2c3ed' and alternate('', 'abc') == 'cba'
    assert replace_at('---', 1, 'x') == '-x-'
    p = [("John", 45, "Male", ["Diabetes"], True), ("Jane", 38, "Female", ["Hypertension", "Asthma"], False),
         ("Sam", 60, "Male", ["Asthma"], True), ("Anna", 29, "Female", ["Allergy"], True)]
    assert stats(p) == (43.0, 2, 'Sam', ['Diabetes', 'Hypertension', 'Asthma', 'Allergy'])
    assert counts_no_dict([('P', 'electric'), ('C', 'fire')], 1,
                          ['electric', 'fighting', 'fire', 'ground', 'normal', 'water']) == (1, 0, 1, 0, 0, 0)
    assert to_value('') is None and to_value('12') == 12 and to_value('0.7') == 0.7 and to_value('a') == 'a'
    assert frequency('abca') == {'a': 2, 'b': 1, 'c': 1}
    assert in_range('2023-10-20', (2023, 10, 3), (2023, 11, 15))
    print('all checks passed')
