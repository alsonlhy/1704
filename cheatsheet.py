# =============================================================================
#  COR-IS1704 LAB TEST CHEAT SHEET
#  Built from: LT1 + LT2 papers (2023-24, 2024-25, 2025-26), Wk 12 mock LT2A,
#              Wk 2-12 ICE / labs, Quiz 4 practice.
#
#  HOW TO USE IN THE TEST
#  1. COPY the function you need INTO your qXX.py. Do NOT `import cheatsheet`
#     - only qXX.py is submitted, so the grader will not have this file.
#  2. Rename the function / parameters to exactly what the paper asks for.
#  3. Lines marked  # <-- TWEAK  are the ones you will usually change.
#  4. No external libraries used (no sympy, no itertools, no math needed).
#
#  RUN THIS FILE (python cheatsheet.py) to re-check every function still works.
#
#  INDEX (Ctrl+F the section tag)
#   [S1]  Numbers: primes, factors, digits, gcd, fibonacci, leap years, rounding
#   [S2]  Tiered / banded pricing: parking, tax brackets, plans, rebates, lookups
#   [S3]  Strings: counting, filtering chars, ciphers, merging, splitting, parsing
#   [S4]  Lists & tuples: filter, sum, average, best/worst with ties, unique,
#         per-category stats WITHOUT dict, sorting, matrix, pairs, swaps
#   [S5]  Files: read with any separator/header, auto type conversion, $ prices,
#         count / average matching rows, write / filter to output file
#   [S6]  Dictionaries: frequency count, group into lists, invert, top-N
#   [S7]  Dates & times: 'YYYY-MM-DD', date-range check, 'HH:MM' <-> minutes
#   [S8]  Simulations: stock & order fulfilment, coin wallets, game boards
#   [S9]  Hard Q4 patterns: all jump sequences (1D/2D), subsets, min allocation
#   [S10] Input loops & output formatting templates
# =============================================================================


# =============================================================================
# [S1] NUMBERS
# =============================================================================

def is_prime(n):
    """True if n is prime. Use when sympy is banned.
    is_prime(7) -> True, is_prime(1) -> False, is_prime(9) -> False"""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def primes_between(start, end):
    """All primes from start to end (both inclusive).
    primes_between(10, 30) -> [11, 13, 17, 19, 23, 29]"""
    result = []
    for n in range(start, end + 1):
        if is_prime(n):
            result.append(n)
    return result


def first_n_primes(n):
    """first_n_primes(5) -> [2, 3, 5, 7, 11]"""
    result = []
    candidate = 2
    while len(result) < n:
        if is_prime(candidate):
            result.append(candidate)
        candidate += 1
    return result


def prime_dict(num_list):
    """{number: True/False} for each number (Lab 8 Q2).
    prime_dict([2, 4, 5]) -> {2: True, 4: False, 5: True}"""
    result = {}
    for num in num_list:
        result[num] = is_prime(num)
    return result


def join_primes(num_list, sep):
    """Primes in the list joined by sep (Wk 5 get_prime_numbers).
    join_primes([4, 5, 6, 7, 11], '-') -> '5-7-11'"""
    parts = []
    for num in num_list:
        if is_prime(num):
            parts.append(str(num))
    return sep.join(parts)


def factors(n):
    """All positive factors of n in ascending order. factors(12) -> [1, 2, 3, 4, 6, 12]"""
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


def prime_factors(n):
    """prime_factors(60) -> [2, 2, 3, 5]"""
    result = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            result.append(d)
            n = n // d
        d += 1
    if n > 1:
        result.append(n)
    return result


def gcd(a, b):
    """Greatest common divisor (Euclid). gcd(12, 18) -> 6"""
    while b != 0:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    """Lowest common multiple. lcm(4, 6) -> 12"""
    return abs(a * b) // gcd(a, b)


def is_perfect_number(n):
    """Sum of proper factors equals n. is_perfect_number(28) -> True"""
    return n > 1 and sum(factors(n)) - n == n


def digit_sum(n):
    """digit_sum(1234) -> 10 (works for negatives too)"""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


def num_digits(n):
    """num_digits(146) -> 3, num_digits(0) -> 1"""
    return len(str(abs(n)))


def reverse_int(n):
    """reverse_int(1230) -> 321, reverse_int(-45) -> -54"""
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])


def is_palindrome_number(n):
    """is_palindrome_number(12321) -> True"""
    return str(n) == str(n)[::-1]


def is_armstrong(n):
    """Sum of each digit ** (number of digits) equals n. is_armstrong(153) -> True"""
    s = str(n)
    total = 0
    for ch in s:
        total += int(ch) ** len(s)
    return total == n


def fibonacci_list(n):
    """First n Fibonacci numbers starting 1, 1. fibonacci_list(7) -> [1, 1, 2, 3, 5, 8, 13]
    TWEAK: start with a, b = 0, 1 if the paper starts from 0."""
    result = []
    a, b = 1, 1                                   # <-- TWEAK starting values
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def factorial(n):
    """factorial(5) -> 120"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_leap_year(year):
    """is_leap_year(2000) -> True, is_leap_year(1900) -> False"""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def days_in_month(month, year=2023):
    """days_in_month(2, 2024) -> 29"""
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


def sum_of_multiples(num_list, n):
    """Sum of numbers in the list divisible by n. sum_of_multiples([3, 4, 6, 9], 3) -> 18"""
    total = 0
    for num in num_list:
        if num % n == 0:
            total += num
    return total


def replace_multiples(m, n):
    """Wk 4 Q2 pattern: multiples of 15 -> '#', of 3 -> '-', of 5 -> '*'.
    replace_multiples(4, 6) -> [4, '*', '-']"""
    result = []
    for i in range(m, n + 1):
        if i % 15 == 0:                           # check the COMBINED case first
            result.append('#')
        elif i % 3 == 0:
            result.append('-')
        elif i % 5 == 0:
            result.append('*')
        else:
            result.append(i)
    return result


def ceil_div(a, b):
    """Round UP a / b without math.ceil. ceil_div(7, 2) -> 4, ceil_div(8, 2) -> 4
    Used for 'charged per started 400 m block' type questions (Wk 3 taxi fare)."""
    return -(-a // b)


# ROUNDING REMINDERS (these have cost marks before)
#   int(41602.9)      -> 41602   'round DOWN to nearest dollar' (positive numbers)
#   round(3.567, 2)   -> 3.57    'round to 2 decimal places'
#   round(62.5)       -> 62      Python rounds .5 to the EVEN number! (LT2 2024 relied on this)
#   round(63.5)       -> 64
#   f"{x:.2f}"        -> string with exactly 2 d.p. (for printing; round() can give 10.5 not 10.50)


# =============================================================================
# [S2] TIERED / BANDED PRICING  (almost every LT1 Q1)
# =============================================================================

def compute_parking(duration):
    """LT1 2023 Q1a. Free <= 10 min grace, $5 up to 60 min, then $0.10 per extra min.
    compute_parking(85) -> 7.5"""
    GRACE = 10                                    # <-- TWEAK
    FIRST_BLOCK = 60                              # <-- TWEAK
    FIRST_CHARGE = 5.0                            # <-- TWEAK
    RATE_AFTER = 0.10                             # <-- TWEAK
    if duration <= GRACE:
        return 0.0
    if duration <= FIRST_BLOCK:
        return FIRST_CHARGE
    return round(FIRST_CHARGE + (duration - FIRST_BLOCK) * RATE_AFTER, 2)


def plan_cost(plan, data_used):
    """LT1 2025 Q1b. Fixed fee + pro-rated charge on usage over quota; invalid key -> message.
    plan_cost('Standard', 333.33) -> 119.99"""
    PLANS = {                                     # <-- TWEAK: name: (fee, quota, extra rate)
        'Lite': (10, 100, 5),
        'Standard': (20, 300, 3),
        'Pro': (50, 900, 1),
    }
    if plan not in PLANS:
        return 'Invalid plan selected'            # <-- TWEAK message
    fee, quota, rate = PLANS[plan]
    if data_used <= quota:
        return fee
    return round(fee + (data_used - quota) * rate, 2)


TAX_BRACKETS = [  # (income above this, tax on everything up to it, rate on the excess)
    (20000, 0, 0.02),
    (30000, 200, 0.035),
    (40000, 550, 0.07),
    (80000, 3350, 0.115),
    (120000, 7950, 0.15),
    (160000, 13950, 0.18),
    (200000, 21150, 0.19),
    (240000, 28750, 0.195),
    (280000, 36550, 0.2),
    (320000, 44550, 0.22),
]


def progressive_tax(income, brackets=TAX_BRACKETS):
    """Wk 3/5 tax: find the highest threshold the income exceeds, then
    base + rate * (income - threshold). progressive_tax(35000) -> 375.0"""
    tax = 0
    for threshold, base, rate in brackets:
        if income > threshold:
            tax = base + rate * (income - threshold)
    return tax


def band_lookup_upper(value, bands, default=None):
    """'Not exceeding X' tables. bands = [(upper_limit_inclusive, result), ...] sorted ascending.
    PARF example: band_lookup_upper(578/365, [(5, 0.75), (6, 0.70), (7, 0.65), (8, 0.60),
                                              (9, 0.55), (10, 0.50)]) -> 0.75
    TWEAK: use `value < limit` if the paper says 'less than' (exclusive)."""
    for limit, result in bands:
        if value <= limit:                        # <-- TWEAK <= vs <
            return result
    return default


def band_lookup_lower(value, bands, default=None):
    """'At least X' tables. bands = [(lower_limit_inclusive, result), ...] sorted DESCENDING.
    Min-stock example: band_lookup_lower(0.09, [(0.5, 3), (0.2, 8)], 15) -> 15"""
    for limit, result in bands:
        if value >= limit:                        # <-- TWEAK >= vs >
            return result
    return default


def table_lookup(row_key, col_key, table, default=0.0):
    """2-D table (row x column) e.g. LT1 2023 S&CC rebate by flat type and month.
    table = {'1': {1: 0.5, 4: 1.0, 7: 1.0, 10: 1.0}, ...}
    Missing row/column -> default."""
    if row_key in table and col_key in table[row_key]:
        return table[row_key][col_key]
    return default


def compute_rebate(is_singaporean, flat_type, month):
    """LT1 2023 Q1b worked example of table_lookup."""
    if not is_singaporean:
        return 0.0
    A = {1: 0.5, 4: 1.0, 7: 1.0, 10: 1.0}
    B = {1: 0.5, 4: 1.0, 7: 0.5, 10: 0.5}
    C = {1: 0.5, 4: 0.5, 7: 0.5, 10: 0.5}
    D = {4: 0.5, 7: 0.5, 10: 0.5}
    table = {'1': A, '2': A, '3': B, '4': B, '5': C, 'E': D}
    return table_lookup(flat_type, month, table, 0.0)


def category_rule(category, quantity):
    """LT1 2024 Q1b pattern: per-category rule, unknown category -> message.
    Watch exact (case-sensitive) spelling of every category."""
    if category == 'Electronics' or category == 'Food':      # <-- TWEAK
        return True
    if category == 'Weapons':
        return False
    if category == 'Liquids':
        return quantity <= 100
    return 'Contact Staff'


def in_range(value, low, high, low_inclusive=True, high_inclusive=True):
    """Range check with explicit inclusive/exclusive ends (food-safety style questions).
    in_range(74.5, 60, 75, True, False) -> True"""
    above = value >= low if low_inclusive else value > low
    below = value <= high if high_inclusive else value < high
    return above and below


def bmr(weight, height, age, gender):
    """LT1 2025 Q2a formula pattern; int() drops decimals. bmr(68.0, 175.0, 30, 'M') -> 1628"""
    value = 10 * weight + 6.25 * height - 5 * age
    if gender == 'M':
        value += 5
    else:
        value -= 161
    return int(value)


# =============================================================================
# [S3] STRINGS
# =============================================================================

VOWELS = 'aeiouAEIOU'
PUNCTUATION = '!?,.:;'
SPECIAL_CHARS = ".,;:!?()[]{}-~&*\\/+=%$#@^_'\"<>"


def count_char_types(s):
    """Return (upper, lower, digits, others) counts - a tuple, so it works when dicts are banned.
    count_char_types('Ab1!') -> (1, 1, 1, 1)"""
    upper = lower = digits = others = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digits += 1
        else:
            others += 1
    return (upper, lower, digits, others)


def count_in_set(s, char_set):
    """How many characters of s are in char_set. count_in_set('Harry', VOWELS) -> 1
    Non-digits: len(s) - count_in_set(s, '0123456789')"""
    count = 0
    for ch in s:
        if ch in char_set:
            count += 1
    return count


def count_non_digits_each(str_list):
    """LT1 2023 Q2b. count_non_digits_each(['abc', '1-2']) -> [3, 1]"""
    result = []
    for s in str_list:
        count = 0
        for ch in s:
            if not ch.isdigit():
                count += 1
        result.append(count)
    return result


def digits_at_even_index(s):
    """LT1 2023 Q2a. digits_at_even_index('SMU-1-2-3-4') -> '1234'
    TWEAK: range(1, len(s), 2) for odd indexes; ch.isalpha() for letters."""
    result = ''
    for i in range(0, len(s), 2):                 # <-- TWEAK start/step
        if s[i].isdigit():                        # <-- TWEAK condition
            result += s[i]
    return result


def classify_chars(s):
    """Map each char: upper -> 'L', lower -> 'l', digit -> 'd', other -> 's' (Wk 7 review)."""
    out = ''
    for ch in s:
        if ch.isupper():
            out += 'L'
        elif ch.islower():
            out += 'l'
        elif ch.isdigit():
            out += 'd'
        else:
            out += 's'
    return out


def index_of_last_letter(s):
    """Mock LT2A Q1a. Index of the last alphabetic char, -1 if none. 'ab12' -> 1"""
    for i in range(len(s) - 1, -1, -1):
        if s[i].isalpha():
            return i
    return -1


def index_of_nth_letter(s, n):
    """Index of the n-th alphabetic char (1-based), -1 if fewer than n letters.
    Mock LT2A Q1b asked for 'second letter' - check whether it wants index or 1-based position.
    index_of_nth_letter('1a2b', 2) -> 3"""
    seen = 0
    for i in range(len(s)):
        if s[i].isalpha():
            seen += 1
            if seen == n:
                return i
    return -1


def alternate_and_reverse(s1, s2):
    """LT2 2024 Q1b. Alternate chars, leftover of the longer string appended REVERSED.
    alternate_and_reverse('abcde', '123') -> 'a1b2c3ed'"""
    result = ''
    shorter = min(len(s1), len(s2))
    for i in range(shorter):
        result += s1[i] + s2[i]
    leftover = s1[shorter:] + s2[shorter:]        # only one of these is non-empty
    return result + leftover[::-1]                # <-- TWEAK drop [::-1] if not reversed


def merge_alternate(list1, list2):
    """Alternate items from two lists; leftovers appended in order. Works on strings too
    if you ''.join() the result. merge_alternate([1, 3, 5, 7], [2, 4]) -> [1, 2, 3, 4, 5, 7]"""
    result = []
    for i in range(max(len(list1), len(list2))):
        if i < len(list1):
            result.append(list1[i])
        if i < len(list2):
            result.append(list2[i])
    return result


def caesar_shift(text, n):
    """Shift letters by n (keeps case, leaves others). caesar_shift('Abz', 1) -> 'Bca'
    Decrypt: caesar_shift(text, -n)."""
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    out = ''
    for ch in text:
        if ch in lower:
            out += lower[(lower.index(ch) + n) % 26]
        elif ch in upper:
            out += upper[(upper.index(ch) + n) % 26]
        else:
            out += ch
    return out


def substitute(msg, mapping):
    """Substitution cipher using a dict; chars not in mapping are kept (Lab 8 Q1).
    Decrypt: substitute(msg, invert_dict(mapping))."""
    out = ''
    for ch in msg:
        if ch in mapping:
            out += mapping[ch]
        else:
            out += ch
    return out


def vowel_rotate(msg):
    """Wk 4 lab: a->e, e->i, i->o, o->u, u->a."""
    return substitute(msg, {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'})


def run_length_encode(text, sep=' '):
    """Wk 7: 'aaabcc' -> 'a3 b1 c2'"""
    if text == '':
        return ''
    parts = []
    current = text[0]
    count = 1
    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            parts.append(current + str(count))
            current = ch
            count = 1
    parts.append(current + str(count))
    return sep.join(parts)


def reverse_each_word(text):
    """reverse_each_word('Hi there') -> 'iH ereht'"""
    words = text.split(' ')
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return ' '.join(words)


def is_palindrome(s, ignore_case=True, letters_only=False):
    """is_palindrome('Racecar') -> True"""
    if letters_only:
        cleaned = ''
        for ch in s:
            if ch.isalnum():
                cleaned += ch
        s = cleaned
    if ignore_case:
        s = s.lower()
    return s == s[::-1]


def is_pangram(s):
    """Every letter a-z appears at least once."""
    s = s.lower()                                 # note the () - a common bug is s.lower
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        if ch not in s:
            return False
    return True


def split_on_many(text, delimiters=PUNCTUATION):
    """Split on ANY of several delimiter characters (LT2 2025 Q1b extract_words).
    split_on_many('apple;banana:cherry') -> ['apple', 'banana', 'cherry']"""
    for d in delimiters:
        text = text.replace(d, ' ')
    return text.split()


def extract_between(text, start_tag, end_tag):
    """All substrings between start_tag and end_tag (Wk 12 extract_bold_texts).
    extract_between('a <b>x</b> c <b>y</b>', '<b>', '</b>') -> ['x', 'y']"""
    result = []
    parts = text.split(start_tag)
    for part in parts[1:]:
        if end_tag in part:
            result.append(part.split(end_tag)[0])
    return result


def parse_length_prefixed(line, width=3):
    """LT2 2025 Q2a. '<3-digit length><sentence><junk>' -> sentence.
    parse_length_prefixed('013"Report him!"uzy') -> '"Report him!"'"""
    length = int(line[:width])
    return line[width:width + length]


def split_text_and_checksum(sentence, width=2):
    """LT2 2025 Q2b. Last `width` chars are a padded number.
    split_text_and_checksum('Has anyone seen Morbo?09') -> ('Has anyone seen Morbo?', 9)"""
    return sentence[:-width], int(sentence[-width:])


def words_with_special_char(words, specials=SPECIAL_CHARS):
    """How many words contain at least one special char (LT2 2023 Q2a)."""
    count = 0
    for word in words:
        for ch in word:
            if ch in specials:
                count += 1
                break                             # count each word once
    return count


def count_shorter_than(str_list, n):
    """LT1 2024 Q2a. Strings STRICTLY shorter than n. TWEAK < to <= if 'at most'."""
    count = 0
    for s in str_list:
        if len(s) < n:                            # <-- TWEAK
            count += 1
    return count


def longest_string(str_list, tie='last'):
    """LT1 2024 Q2b. Returns (string, length) or None for empty list.
    tie='last' -> later one wins (uses >=); tie='first' -> earlier one wins (uses >)."""
    if str_list == []:
        return None
    best = str_list[0]
    for s in str_list[1:]:
        if (tie == 'last' and len(s) >= len(best)) or (tie == 'first' and len(s) > len(best)):
            best = s
    return (best, len(best))


def pad_or_truncate(msg, width, fill=' ', align='right'):
    """Wk 4 pad_message: right-align to width, or cut to width if too long."""
    if len(msg) >= width:
        return msg[:width]
    padding = fill * (width - len(msg))
    return padding + msg if align == 'right' else msg + padding


def pad_all_to_longest(str_list, fill):
    """Pad every string (on the right) to the length of the longest one (Wk 6 pad_strings)."""
    longest = 0
    for s in str_list:
        if len(s) > longest:
            longest = len(s)
    result = []
    for s in str_list:
        result.append(s + fill * (longest - len(s)))
    return result


def words_starting_with(text_list, prefix='#'):
    """All words beginning with prefix across a list of posts (Wk 6 get_hashtags)."""
    result = []
    for post in text_list:
        for word in post.split():
            if word.startswith(prefix):
                result.append(word)
    return result


def first_matching_digit_sum(str_list):
    """Wk 6: add the FIRST odd digit of each string (break after the first)."""
    total = 0
    for s in str_list:
        for ch in s:
            if ch.isdigit() and int(ch) % 2 == 1:     # <-- TWEAK condition
                total += int(ch)
                break
    return total


def numbers_in_string(s):
    """Pull every number (int or decimal) out of messy text (Wk 5 compute_avg_height).
    numbers_in_string('A:1.7m, B:1.65m') -> [1.7, 1.65]"""
    result = []
    current = ''
    for ch in s + ' ':                            # trailing space flushes the last number
        if ch.isdigit() or (ch == '.' and current != '' and '.' not in current):
            current += ch
        else:
            if current != '':
                result.append(float(current))
                current = ''
    return result


def email_id(address):
    """'jerry.lee@smu.edu.sg' -> 'jerry.lee'; '' if not exactly one '@'."""
    parts = address.split('@')
    return parts[0] if len(parts) == 2 else ''


def common_chars(s1, s2):
    """Unique chars appearing in both, in order of s1. common_chars('hello', 'world') -> 'lo'"""
    result = ''
    for ch in s1:
        if ch in s2 and ch not in result:
            result += ch
    return result


# =============================================================================
# [S4] LISTS & TUPLES
# =============================================================================

def filter_records(records, index, threshold, mode='<='):
    """Keep records whose records[i][index] compares with threshold. Does NOT modify input.
    filter_records([(9.9, 4), (11.2, 5)], 0, 10.0, '<=') -> [(9.9, 4)]"""
    result = []
    for rec in records:
        v = rec[index]
        if ((mode == '<=' and v <= threshold) or (mode == '<' and v < threshold) or
                (mode == '>=' and v >= threshold) or (mode == '>' and v > threshold) or
                (mode == '==' and v == threshold)):
            result.append(rec)
    return result


def sum_where(records, value_index, cond_index, limit):
    """LT2 2024 Q1a. Sum value where cond <= limit; None for empty list, 0 if none match."""
    if records == []:
        return None
    total = 0
    for rec in records:
        if rec[cond_index] <= limit:              # <-- TWEAK condition
            total += rec[value_index]
    return total


def first_plus_last_at_least(tup_list, num):
    """LT2 2025 Q1a. Tuples where first + last element >= num."""
    result = []
    for t in tup_list:
        if t[0] + t[-1] >= num:                   # <-- TWEAK
            result.append(t)
    return result


def average(nums, ndigits=2, empty_value=0.0):
    """Rounded average; guard against empty list."""
    if len(nums) == 0:
        return empty_value
    return round(sum(nums) / len(nums), ndigits)


def column(records, index):
    """Pull one field out of every record. column([('a', 1), ('b', 2)], 1) -> [1, 2]"""
    result = []
    for rec in records:
        result.append(rec[index])
    return result


def find_best(records, value_index, return_index=None, biggest=True, tie='first'):
    """Max/min record with explicit tie rule. Returns the whole record, or one field of it.
    tie='first' keeps the earliest (strict >), tie='last' takes the latest (>=).
    find_best(cars, 1, 0) -> name of the record with the largest field 1."""
    if records == []:
        return None
    best = records[0]
    for rec in records[1:]:
        a, b = rec[value_index], best[value_index]
        if biggest:
            better = a > b if tie == 'first' else a >= b
        else:
            better = a < b if tie == 'first' else a <= b
        if better:
            best = rec
    return best if return_index is None else best[return_index]


def best_by_function(items, score_function, tie='first'):
    """Like find_best but the score is COMPUTED (LT2 2023 Q1c highest deregistration value).
    best_by_function(cars, lambda c: compute_coe(c) + compute_parf(c))"""
    best = None
    best_score = None
    for item in items:
        score = score_function(item)
        if best is None or score > best_score or (tie == 'last' and score == best_score):
            best, best_score = item, score
    return best


def unique_in_order(items):
    """Remove duplicates, keep first-seen order. unique_in_order([3, 1, 3, 2]) -> [3, 1, 2]"""
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def unique_from_nested(records, list_index):
    """Unique items from a list-inside-each-tuple, first-seen order (LT1 2024 Q3 ailments)."""
    result = []
    for rec in records:
        for item in rec[list_index]:
            if item not in result:
                result.append(item)
    return result


def count_matching(records, index, value):
    """How many records have rec[index] == value."""
    count = 0
    for rec in records:
        if rec[index] == value:
            count += 1
    return count


def patient_stats(patients):
    """LT1 2024 Q3 worked example: (avg age, males, females, discharged, unique ailments)."""
    ages = column(patients, 1)
    return (round(sum(ages) / len(ages), 2),
            count_matching(patients, 2, 'Male'),
            count_matching(patients, 2, 'Female'),
            count_matching(patients, 4, True),
            unique_from_nested(patients, 3))


def counts_per_category(records, cat_index, categories):
    """NO-DICT version (LT1 2025 banned dicts). Counts in the fixed order of `categories`.
    counts_per_category(cards, 1, ['electric', 'fighting', 'fire', 'ground', 'normal', 'water'])
    -> (1, 0, 1, 0, 0, 0)"""
    counts = [0] * len(categories)
    for rec in records:
        for i in range(len(categories)):
            if rec[cat_index] == categories[i]:
                counts[i] += 1
    return tuple(counts)


def best_average_per_category(records, cat_index, value_index, categories, ndigits=2):
    """NO-DICT. Category with the highest average of value_index -> (category, rounded avg).
    LT1 2025 Q3c get_best_avg. Categories with no records are skipped."""
    sums = [0] * len(categories)
    counts = [0] * len(categories)
    for rec in records:
        for i in range(len(categories)):
            if rec[cat_index] == categories[i]:
                sums[i] += rec[value_index]
                counts[i] += 1
    best_cat = None
    best_avg = None
    for i in range(len(categories)):
        if counts[i] > 0:
            avg = sums[i] / counts[i]
            if best_avg is None or avg > best_avg:
                best_cat, best_avg = categories[i], avg
    return (best_cat, round(best_avg, ndigits))


def neighbour_sums(nums):
    """Each element + its left and right neighbours (Wk 5). [56, -10, 25, -32] -> [46, 71, -17, -7]"""
    result = []
    for i in range(len(nums)):
        total = nums[i]
        if i > 0:
            total += nums[i - 1]
        if i < len(nums) - 1:
            total += nums[i + 1]
        result.append(total)
    return result


def running_totals(nums):
    """Cumulative sums. [1, 2, 3] -> [1, 3, 6]"""
    result = []
    total = 0
    for n in nums:
        total += n
        result.append(total)
    return result


def adjacent_pairs(items, circular=False):
    """Pairs of neighbours. circular=True also pairs last with first (round table, LT1 2023 Q3b).
    adjacent_pairs(['A', 'B', 'C'], True) -> [('A', 'B'), ('B', 'C'), ('C', 'A')]"""
    pairs = []
    n = len(items)
    last = n if circular else n - 1
    for i in range(last):
        pairs.append((items[i], items[(i + 1) % n]))
    return pairs


def common_items(list1, list2):
    """Items in both lists (order of list1, no duplicates)."""
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result


def non_common_items(list1, list2):
    """Items in exactly one of the lists (Wk 5). (['a','b','c'], ['b','d']) -> ['a', 'c', 'd']"""
    result = []
    for item in list1:
        if item not in list2:
            result.append(item)
    for item in list2:
        if item not in list1:
            result.append(item)
    return result


def all_pairs(list1, list2):
    """Every combination (Wk 5). (['a', 'b'], [1, 2]) -> [('a', 1), ('a', 2), ('b', 1), ('b', 2)]"""
    result = []
    for a in list1:
        for b in list2:
            result.append((a, b))
    return result


def all_greater_than(nums, n):
    """True only if EVERY number > n (common bug: only checking the last one)."""
    for num in nums:
        if num <= n:
            return False
    return True


def larger_than_all(list1, list2):
    """Items in list1 bigger than EVERY item of list2 (Wk 5 get_larger_numbers)."""
    result = []
    for a in list1:
        bigger_than_every_one = True
        for b in list2:
            if a <= b:
                bigger_than_every_one = False
                break
        if bigger_than_every_one:
            result.append(a)
    return result


def span_ok(values, max_distinct_consecutive=2):
    """All values fall within N consecutive integers (LT1 2023 Q3a internship years).
    span_ok([2021, 2022, 2021]) -> True ; span_ok([2020, 2022]) -> False"""
    return max(values) - min(values) <= max_distinct_consecutive - 1


def max_count_ok(values, limit):
    """No value occurs more than `limit` times (at most 2 students per school)."""
    for v in values:
        if values.count(v) > limit:
            return False
    return True


def try_all_swaps(t1, t2, is_ok):
    """LT1 2023 Q3c. Swap one item of t1 with one of t2 until both satisfy is_ok.
    Returns (item1, item2, new_t1, new_t2) or None. Original lists are not modified."""
    for i in range(len(t1)):
        for j in range(len(t2)):
            new_t1 = t1[:i] + [t2[j]] + t1[i + 1:]
            new_t2 = t2[:j] + [t1[i]] + t2[j + 1:]
            if is_ok(new_t1) and is_ok(new_t2):
                return (t1[i], t2[j], new_t1, new_t2)
    return None


def chain_from_pairs(pairs):
    """Rebuild a queue from (in_front, behind) pairs (Wk 9 get_lineup)."""
    if pairs == []:
        return []
    behinds = column(pairs, 1)
    current = None
    for front, _ in pairs:
        if front not in behinds:
            current = front
            break
    line = []
    while current is not None:
        line.append(current)
        nxt = None
        for front, behind in pairs:
            if front == current:
                nxt = behind
                break
        current = nxt
    return line


def sort_records(records, index, descending=False):
    """New sorted list by one field (stable: ties keep original order).
    Multi-key: sorted(records, key=lambda r: (-r[1], r[0]))  -> field 1 desc, then field 0 asc."""
    return sorted(records, key=lambda r: r[index], reverse=descending)


def insertion_sort_by(records, index):
    """Manual stable sort IN PLACE (if sorted() is banned). Ascending by records[i][index]."""
    for i in range(1, len(records)):
        key = records[i]
        j = i - 1
        while j >= 0 and key[index] < records[j][index]:
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = key
    return records


def bubble_sort(nums):
    """Classic bubble sort, in place, ascending."""
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def top_n(nums, n, largest=True):
    """top_n([5, 1, 9, 3], 2) -> [9, 5]"""
    return sorted(nums, reverse=largest)[:n]


def transpose(matrix):
    """Works for NON-square matrices too. [[1, 2, 3], [4, 5, 6]] -> [[1, 4], [2, 5], [3, 6]]"""
    result = []
    for c in range(len(matrix[0])):
        row = []
        for r in range(len(matrix)):
            row.append(matrix[r][c])
        result.append(row)
    return result


def negate_and_reverse(nums):
    """Mock LT2A Q2: flip the sign of each number, then reverse the list."""
    result = []
    for n in nums:
        result.append(-n if n != 0 else n)
    return result[::-1]


# =============================================================================
# [S5] FILES
# =============================================================================
# Core pattern - memorise this:
#     with open(filename) as f:
#         header = f.readline()            # ONLY if the file has a header line
#         for line in f:
#             line = line.rstrip('\n')
#             cols = line.split(',')       # <-- the separator: ',', '\t', '|', '!', '**', '::', '$'
# Writing:   with open(out, 'w') as f:  f.write(text + '\n')   (write() never adds '\n' itself)
# Empty file: the for-loop simply runs 0 times - return {} / [] naturally.

def money_to_float(text):
    """'$1,200.00' / '1200.00' / ' $5 ' -> float. Use int(...) if the paper says integer."""
    return float(text.strip().lstrip('$').replace(',', ''))


def smart_convert(text):
    """'' -> None, '12' -> 12, '0.7' -> 0.7, anything else stays str (LT2 2023 Q3a).
    Handles a leading minus sign as well."""
    if text == '':
        return None
    body = text[1:] if text[0] in '+-' else text
    if body.isdigit():
        return int(text)
    if body.count('.') == 1 and body.replace('.', '').isdigit():
        return float(text)
    return text


def read_lines(filename):
    """Every line without the newline."""
    lines = []
    with open(filename) as f:
        for line in f:
            lines.append(line.rstrip('\n'))
    return lines


def read_rows(filename, sep=',', has_header=False):
    """List of lists of strings. read_rows('tours.txt', '!', True)"""
    rows = []
    with open(filename) as f:
        if has_header:
            f.readline()
        for line in f:
            line = line.rstrip('\n')
            if line == '':
                continue                          # skip blank lines safely
            rows.append(line.split(sep))
    return rows


def read_typed(filename, sep, types, has_header=False):
    """List of TUPLES with each column converted. types: one converter per column.
    read_typed('tours.txt', '!', [str, int, float], True)
      -> [('River Walk', 12, 18.5), ...]
    Use money_to_float for '$' columns, smart_convert if unsure."""
    records = []
    for cols in read_rows(filename, sep, has_header):
        rec = []
        for i in range(len(types)):
            rec.append(types[i](cols[i]))
        records.append(tuple(rec))
    return records


def read_header_dicts(filename, sep=','):
    """Header line gives the keys -> list of dicts, values auto-converted (LT2 2023 load_pokedex)."""
    result = []
    with open(filename) as f:
        keys = f.readline().rstrip('\n').split(sep)
        for line in f:
            cols = line.rstrip('\n').split(sep)
            record = {}
            for i in range(len(keys)):
                record[keys[i]] = smart_convert(cols[i])
            result.append(record)
    return result


def select_fields(records, fields):
    """Keep only some keys of each dict; skip dicts that end up empty (LT2 2023 Q3b).
    fields == [] -> return everything."""
    if fields == []:
        return records
    result = []
    for rec in records:
        new = {}
        for k in fields:
            if k in rec:
                new[k] = rec[k]
        if new:
            result.append(new)
    return result


def count_rows(filename, sep=',', col=0, value=None):
    """LT2 2024 Q2a pattern with an OPTIONAL parameter (default None):
    value None -> count all rows, else rows where cols[col] == value."""
    count = 0
    for cols in read_rows(filename, sep):
        if value is None or cols[col] == value:
            count += 1
    return count


def count_and_average(filename, sep, match, value_col):
    """LT2 2024 Q2b. match = {col_index: required_text, ...}.
    Returns (count, round(average)) or (0, 0) if nothing matches.
    count_and_average('swim.csv', ',', {0: 'Michael Phelps', 1: '50m doggy paddle'}, 2) -> (2, 62)"""
    total = 0
    count = 0
    for cols in read_rows(filename, sep):
        ok = True
        for c in match:
            if cols[c] != match[c]:
                ok = False
        if ok:
            total += int(cols[value_col])         # <-- TWEAK int/float
            count += 1
    if count == 0:
        return (0, 0)
    return (count, round(total / count))          # <-- TWEAK round(..., 2) if needed


def report_with_total(filename, prefix):
    """LT2 2023 Q2b loan report: rows whose col 1 starts with prefix, as typed tuples,
    then ('Total Loan Amount', total) appended - unless nothing matched (then [])."""
    result = []
    total = 0
    for cols in read_rows(filename, ','):
        if cols[1][:len(prefix)] == prefix:       # <-- TWEAK which column / test
            amount = int(money_to_float(cols[3]))
            result.append((cols[0], cols[1], cols[2], amount))
            total += amount
    if result:
        result.append(('Total Loan Amount', total))
    return result


def sum_file_numbers(filename):
    """One number per line -> total (Wk 10 sum_up)."""
    total = 0.0
    for line in read_lines(filename):
        if line != '':
            total += float(line)
    return total


def count_words_in_file(filename, lowercase=True):
    """{word: count} for the whole file (Lab 8 Q5a)."""
    counts = {}
    with open(filename) as f:
        for line in f:
            if lowercase:
                line = line.lower()
            for word in line.split():
                counts[word] = counts.get(word, 0) + 1
    return counts


def special_word_count_file(filename):
    """LT2 2023 Q2a: words (split on single spaces) containing a special char."""
    total = 0
    for line in read_lines(filename):
        total += words_with_special_char(line.split(' '))
    return total


def read_matrix(filename, sep=' '):
    """Each line -> list of floats (Lab 7 Q5a)."""
    matrix = []
    for cols in read_rows(filename, sep):
        row = []
        for c in cols:
            row.append(float(c))
        matrix.append(row)
    return matrix


def write_lines(filename, lines):
    """Write each string on its own line."""
    with open(filename, 'w') as f:
        for line in lines:
            f.write(str(line) + '\n')


def filter_file(in_name, out_name, sep, col, threshold):
    """Copy rows where float(col, '$' removed) > threshold into another file (Lab 7 Q4a)."""
    with open(in_name) as fin, open(out_name, 'w') as fout:
        for line in fin:
            line = line.rstrip('\n')
            cols = line.split(sep)
            if money_to_float(cols[col]) > threshold:     # <-- TWEAK condition
                fout.write(line + '\n')


def group_averages_file(in_name, out_name):
    """Mock LT2A Q3. Each line: groups separated by '#', numbers by spaces.
    Writes '<num groups>: avg#avg...' per line, then totals."""
    total_groups = 0
    max_avg = None
    with open(in_name) as fin, open(out_name, 'w') as fout:
        for line in fin:
            groups = line.strip().split('#')
            avgs = []
            for g in groups:
                nums = g.split()
                avg = round(sum(float(x) for x in nums) / len(nums), 1)
                avgs.append(str(avg))
                if max_avg is None or avg > max_avg:
                    max_avg = avg
            total_groups += len(groups)
            fout.write(f"{len(groups)}: {'#'.join(avgs)}\n")
        fout.write(f"Total number of groups: {total_groups}\n")
        fout.write(f"Maximum average: {max_avg}\n")


# =============================================================================
# [S6] DICTIONARIES
# =============================================================================

def frequency(items):
    """{item: count}, first-seen order. frequency('abca') -> {'a': 2, 'b': 1, 'c': 1}"""
    counts = {}
    for item in items:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1
    return counts


def group_by(records, key_index, keep_key=False):
    """{key: [records...]} in file/list order (LT2 2025 Q3a weather, Lab 8 facilities).
    keep_key=False drops the key field from each stored tuple."""
    groups = {}
    for rec in records:
        key = rec[key_index]
        if keep_key:
            value = rec
        else:
            value = tuple(rec[:key_index]) + tuple(rec[key_index + 1:])
        if key not in groups:
            groups[key] = []
        groups[key].append(value)
    return groups


def dict_from_file(filename, sep, key_col, value_col, has_header=False):
    """{cols[key_col]: cols[value_col]} - later duplicates overwrite earlier ones."""
    result = {}
    for cols in read_rows(filename, sep, has_header):
        result[cols[key_col]] = cols[value_col]
    return result


def dict_of_lists_from_file(filename, sep, key_col, value_col):
    """{key: [all values for that key]} e.g. one person, many phone numbers (Wk 11 Q5)."""
    result = {}
    for cols in read_rows(filename, sep):
        key = cols[key_col]
        if key not in result:
            result[key] = []
        result[key].append(cols[value_col])
    return result


def invert_dict(d):
    """{v: k}. If values repeat, the LAST key wins - use invert_to_lists then."""
    result = {}
    for k in d:
        result[d[k]] = k
    return result


def invert_to_lists(d):
    """{value: [keys...]} e.g. {student: school} -> {school: [students]} (Lab 8 Q4)."""
    result = {}
    for k in d:
        v = d[k]
        if v not in result:
            result[v] = []
        result[v].append(k)
    return result


def dict_from_alternating(items):
    """['Ann', 'a@x', 'Bob', 'b@x'] -> {'Ann': 'a@x', 'Bob': 'b@x'} (Wk 12 Q1b)."""
    result = {}
    for i in range(0, len(items) - 1, 2):
        result[items[i]] = items[i + 1]
    return result


def set_and_return_old(d, key, value):
    """Update d[key]; return the previous value, or None if the key was new (Wk 12 Q1c)."""
    old = d.get(key)
    d[key] = value
    return old


def parse_key_value_pairs(line, pair_sep='\t', kv_sep=':'):
    """'id:1\tname:Ann\tage:30' -> {'id': '1', 'name': 'Ann', 'age': '30'} (Lab 8 Q6)."""
    result = {}
    for pair in line.split(pair_sep):
        k, v = pair.split(kv_sep, 1)
        result[k] = v
    return result


def top_n_by_value(d, n, largest=True):
    """[(key, value), ...] of the n biggest values (Lab 8 Q5c word cloud)."""
    return sorted(d.items(), key=lambda kv: kv[1], reverse=largest)[:n]


def keys_where(d, condition_min_value):
    """Keys whose value >= threshold, in dict order."""
    result = []
    for k in d:
        if d[k] >= condition_min_value:           # <-- TWEAK
            result.append(k)
    return result


# =============================================================================
# [S7] DATES & TIMES
# =============================================================================

def parse_date(text, sep='-'):
    """'2023-10-01' -> (2023, 10, 1). For 'DD/MM/YYYY' use sep='/' and reverse: [::-1]"""
    parts = text.split(sep)
    return (int(parts[0]), int(parts[1]), int(parts[2]))


def in_date_range(date, start, end):
    """(y, m, d) tuples compare correctly field by field - this is all you need.
    in_date_range((2023, 10, 20), (2023, 10, 3), (2023, 11, 15)) -> True
    WARNING: do NOT check year, month and day ranges separately - that wrongly
    rejects (2023, 10, 20) above because 20 > 15 (the official LT2 2025 Q3b solution has this bug)."""
    return start <= date <= end


def hhmm_to_minutes(text):
    """'09:30' -> 570"""
    h, m = text.split(':')
    return int(h) * 60 + int(m)


def minutes_to_hhmm(minutes):
    """570 -> '09:30'"""
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def weather_stats(filename, start, end):
    """LT2 2025 Q3a+b combined: {city: (count, avg max temp 1dp, total rain 1dp)} for records in range."""
    by_city = {}
    for cols in read_rows(filename, '|'):
        rec = (parse_date(cols[0]), float(cols[2]), float(cols[3]), float(cols[4]))
        by_city.setdefault(cols[1], []).append(rec)
    result = {}
    for city in by_city:
        count, temp_sum, rain_sum = 0, 0.0, 0.0
        for date, max_t, _min_t, rain in by_city[city]:
            if in_date_range(date, start, end):
                count += 1
                temp_sum += max_t
                rain_sum += rain
        if count > 0:
            result[city] = (count, round(temp_sum / count, 1), round(rain_sum, 1))
    return result


# =============================================================================
# [S8] SIMULATIONS
# =============================================================================

def fulfil_orders(stock, orders):
    """LT2 2024 Q3b. stock = {product: qty} (gets reduced), orders = [(id, buyer, product, qty)].
    Returns {buyer: [(id, product, qty_ordered, qty_filled), ...]} in order.
    Products missing from stock get 0 filled."""
    result = {}
    for order_id, buyer, product, qty in orders:
        available = stock.get(product, 0)
        filled = min(qty, available)
        stock[product] = available - filled
        if buyer not in result:
            result[buyer] = []
        result[buyer].append((order_id, product, qty, filled))
    return result


def inventory_with_min_stock(filename):
    """LT2 2024 Q3a: name,cat,$price,$cost,qty -> {name: [qty, min_stock]} by profit-margin band."""
    result = {}
    for cols in read_rows(filename, ','):
        price, cost = money_to_float(cols[2]), money_to_float(cols[3])
        margin = (price - cost) / cost
        result[cols[0]] = [int(cols[4]), band_lookup_lower(margin, [(0.5, 3), (0.2, 8)], 15)]
    return result


def remove_items(pool, items):
    """Multiset removal: remove ALL of `items` from `pool` (list) only if every one is there
    (coin wallets, ThinkCoin LT2 2024 Q4). Returns True if removed, False (pool unchanged) otherwise."""
    for item in items:
        if pool.count(item) < items.count(item):
            return False
    for item in items:
        pool.remove(item)                         # removes the first occurrence only
    return True


def board_from_moves(n, game, move_len=3):
    """LT1 2024 Q4a. game like '11x20o22x' (row, col, player). Returns list of n strings.
    board_from_moves(3, '11x20o22x10o00x') -> ['x--', 'ox-', 'o-x']"""
    board = ['-' * n] * n
    for i in range(0, len(game), move_len):
        move = game[i:i + move_len]
        r, c, player = int(move[0]), int(move[1]), move[2]
        board[r] = board[r][:c] + player + board[r][c + 1:]
    return board


def drop_into_column(board, col, player):
    """Gravity version (Connect-4 style, LT1 2024 Q4b): piece lands in the LOWEST empty row.
    Modifies board (list of strings) and returns it."""
    for r in range(len(board) - 1, -1, -1):
        if board[r][col] == '-':
            board[r] = board[r][:col] + player + board[r][col + 1:]
            break
    return board


def has_k_in_a_row(board, k, player):
    """Any horizontal, vertical or diagonal run of k `player` marks (LT1 2024 Q4c)."""
    rows = len(board)
    cols = len(board[0])
    for r in range(rows):
        for c in range(cols):
            for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
                count = 0
                rr, cc = r, c
                while 0 <= rr < rows and 0 <= cc < cols and board[rr][cc] == player:
                    count += 1
                    if count == k:
                        return True
                    rr += dr
                    cc += dc
    return False


def who_won(k, board):
    """'x' / 'o' / 'tie' (board full, nobody won) / None (game still on)."""
    if has_k_in_a_row(board, k, 'x'):
        return 'x'
    if has_k_in_a_row(board, k, 'o'):
        return 'o'
    if '-' not in ''.join(board):
        return 'tie'
    return None


def grid_neighbours(grid, r, c, diagonals=False):
    """Coordinates of in-bounds neighbours of (r, c)."""
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if diagonals:
        steps += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    result = []
    for dr, dc in steps:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            result.append((nr, nc))
    return result


# =============================================================================
# [S9] HARD Q4 PATTERNS (*** questions)
# =============================================================================

def all_jump_sequences_1d(map_str, jumps=(1, 2, 3), blocked='*'):
    """LT2 2025 Q4a. map_str = 'A00**0*00B'. Returns (count, list of jump lists).
    Idea: ways[i] = every jump list that lands safely on position i; build left to right."""
    inner = map_str[1:-1]
    goal = len(inner) + 1                         # position of 'B'
    ways = []
    for _ in range(goal + 1):
        ways.append([])
    ways[0] = [[]]                                # standing on 'A' with no jumps yet
    for pos in range(goal + 1):
        for seq in ways[pos]:
            for j in jumps:
                nxt = pos + j
                if nxt <= goal and (nxt == goal or inner[nxt - 1] != blocked):
                    ways[nxt].append(seq + [j])
    return (len(ways[goal]), ways[goal])


def all_jump_sequences_2d(grid, jumps=(1, 2, 3), blocked='*'):
    """LT2 2025 Q4b. grid = ['A00*', '00*0', '**0B']; moves right ('r') or down ('d').
    Returns (count, list of [(steps, dir), ...])."""
    rows, cols = len(grid), len(grid[0])
    ways = []
    for r in range(rows):
        ways.append([])
        for c in range(cols):
            ways[r].append([])
    ways[0][0] = [[]]
    for r in range(rows):
        for c in range(cols):
            for seq in ways[r][c]:
                for j in jumps:
                    if c + j < cols and grid[r][c + j] != blocked:
                        ways[r][c + j].append(seq + [(j, 'r')])
                    if r + j < rows and grid[r + j][c] != blocked:
                        ways[r + j][c].append(seq + [(j, 'd')])
    end = ways[rows - 1][cols - 1]
    return (len(end), end)


def count_grid_paths(grid, blocked='*'):
    """Number of right/down single-step paths from top-left to bottom-right (count only - fast)."""
    rows, cols = len(grid), len(grid[0])
    ways = [[0] * cols for _ in range(rows)]
    ways[0][0] = 1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == blocked:
                ways[r][c] = 0
                continue
            if r > 0:
                ways[r][c] += ways[r - 1][c]
            if c > 0:
                ways[r][c] += ways[r][c - 1]
    return ways[rows - 1][cols - 1]


def combinations_of(items, r):
    """All r-length combinations in the same order as itertools.combinations (no import needed).
    combinations_of([1, 2, 3], 2) -> [(1, 2), (1, 3), (2, 3)]"""
    if r == 0:
        return [()]
    result = []
    for i in range(len(items) - r + 1):
        for rest in combinations_of(items[i + 1:], r - 1):
            result.append((items[i],) + rest)
    return result


def all_subsets(items):
    """Every non-empty subset, smallest first."""
    result = []
    for r in range(1, len(items) + 1):
        result += combinations_of(items, r)
    return result


def closest_subsets_at_least(values, target):
    """LT2 2024 Q4b idea: subsets whose sum >= target with the SMALLEST overshoot.
    Duplicate value-combinations are listed once. closest_subsets_at_least([5, 5, 1, 2], 9) -> [(5, 5)]"""
    best = []
    best_diff = None
    for combo in all_subsets(values):
        total = sum(combo)
        if total >= target:
            diff = total - target
            if best_diff is None or diff < best_diff:
                best_diff, best = diff, [combo]
            elif diff == best_diff and sorted(combo) not in [sorted(b) for b in best]:
                best.append(combo)
    return best


def min_allocation_1d(rating):
    """LT1 2025 Q4a (the 'candy' problem): >= 1 each, higher rating than a neighbour -> strictly more.
    Two passes: left-to-right, then right-to-left. [0, 3, 3, 5] -> [1, 2, 1, 2]"""
    n = len(rating)
    bonus = [1] * n
    for i in range(1, n):
        if rating[i] > rating[i - 1]:
            bonus[i] = bonus[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if rating[i] > rating[i + 1] and bonus[i] <= bonus[i + 1]:
            bonus[i] = bonus[i + 1] + 1
    return bonus


def min_allocation_grid(grid):
    """LT1 2025 Q4b. Same rules on a grid (up/down/left/right neighbours).
    Keep fixing violations until nothing changes - always ends at the minimum."""
    rows, cols = len(grid), len(grid[0])
    bonus = []
    for r in range(rows):
        bonus.append([1] * cols)
    changed = True
    while changed:
        changed = False
        for r in range(rows):
            for c in range(cols):
                for nr, nc in grid_neighbours(grid, r, c):
                    if grid[r][c] > grid[nr][nc] and bonus[r][c] <= bonus[nr][nc]:
                        bonus[r][c] = bonus[nr][nc] + 1
                        changed = True
    return bonus


# =============================================================================
# [S10] INPUT LOOPS & OUTPUT FORMATTING
# =============================================================================

def ask_until_valid(prompt, is_valid, error_msg='Invalid input!'):
    """Keep asking until is_valid(answer) is True (Wk 9 while-loop pattern)."""
    answer = input(prompt)
    while not is_valid(answer):
        print(error_msg)
        answer = input(prompt)
    return answer


def yes_no_loop_template():
    """Menu loop skeleton - copy and fill in the body."""
    again = input('Do you want to search? [Y|N] ')
    while again in ('Y', 'y'):
        # ... do one round of work here ...
        again = input('Do you want to search again? [Y|N] ')
    print('Good-bye!')


def numbered_join(items, sep='-'):
    """LT2-style numbered string: [('Apple', 1164), ('Pear', 1320)] -> '1-Apple(1164)-2-Pear(1320)'"""
    parts = []
    for i in range(len(items)):
        name, value = items[i]
        parts.append(f"{i + 1}{sep}{name}({value})")        # <-- TWEAK the format
    return sep.join(parts)


def triangle_lines(ch, rows):
    """Centred triangle (Wk 7). triangle_lines('*', 3) -> ['  *', ' ***', '*****']"""
    lines = []
    for i in range(rows):
        lines.append(' ' * (rows - i - 1) + ch * (2 * i + 1))
    return lines


def frame_lines(ch, rows, cols):
    """Hollow rectangle. frame_lines('#', 3, 4) -> ['####', '#  #', '####']"""
    if rows == 1:
        return [ch * cols]
    lines = [ch * cols]
    for _ in range(rows - 2):
        lines.append(ch + ' ' * (cols - 2) + ch if cols > 1 else ch)
    lines.append(ch * cols)
    return lines


def diamond_lines(n, ch='*'):
    """Hollow diamond with side n (Wk 7). Print with: for line in diamond_lines(4): print(line)"""
    lines = []
    for r in range(2 * n - 1):
        i = r if r < n else 2 * n - 2 - r
        line = ' ' * (n - 1 - i) + ch
        if i > 0:
            line += ' ' * (2 * i - 1) + ch
        lines.append(line)
    return lines


# f-string formatting reminders
#   f"{x:.2f}"     -> '3.50'      2 decimal places
#   f"${x:,.2f}"   -> '$1,234.50' thousands separator
#   f"{n:03d}"     -> '007'       zero-padded
#   f"{s:<10}|"    -> left-align in 10 chars;  f"{s:>10}" right;  f"{s:^10}" centre
#   print(a, b, sep='', end='')   control spaces / newline


# =============================================================================
# SELF-TEST (uses examples from the past papers). Run: python cheatsheet.py
# =============================================================================
if __name__ == '__main__':
    import os
    import tempfile

    def check(label, got, expected):
        status = 'ok ' if got == expected else 'FAIL'
        if got != expected:
            print(f'{status} {label}\n     got:      {got}\n     expected: {expected}')
        return got == expected

    def make_file(folder, name, text):
        path = os.path.join(folder, name)
        with open(path, 'w') as f:
            f.write(text)
        return path

    results = []
    t = results.append

    # [S1]
    t(check('is_prime', [n for n in range(20) if is_prime(n)], [2, 3, 5, 7, 11, 13, 17, 19]))
    t(check('primes_between', primes_between(10, 30), [11, 13, 17, 19, 23, 29]))
    t(check('first_n_primes', first_n_primes(5), [2, 3, 5, 7, 11]))
    t(check('join_primes', join_primes([4, 5, 6, 7, 11], '-'), '5-7-11'))
    t(check('factors', factors(12), [1, 2, 3, 4, 6, 12]))
    t(check('prime_factors', prime_factors(60), [2, 2, 3, 5]))
    t(check('gcd/lcm', (gcd(12, 18), lcm(4, 6)), (6, 12)))
    t(check('perfect', is_perfect_number(28), True))
    t(check('digits', (digit_sum(1234), num_digits(146), reverse_int(-45)), (10, 3, -54)))
    t(check('armstrong', is_armstrong(153), True))
    t(check('fibonacci', fibonacci_list(7), [1, 1, 2, 3, 5, 8, 13]))
    t(check('leap', [is_leap_year(y) for y in (2000, 1900, 2024, 2023)], [True, False, True, False]))
    t(check('ceil_div', (ceil_div(7, 2), ceil_div(8, 2)), (4, 4)))
    t(check('replace_multiples', replace_multiples(4, 6), [4, '*', '-']))

    # [S2]
    t(check('parking', [compute_parking(d) for d in (10, 30, 60, 70, 85, 310)],
            [0.0, 5.0, 5.0, 6.0, 7.5, 30.0]))
    t(check('plan_cost', [plan_cost('Lite', 50.5), plan_cost('Lite', 100.1),
                          plan_cost('Standard', 333.33), plan_cost('Pro', 999.991),
                          plan_cost('Basic', 1.0)],
            [10, 10.5, 119.99, 149.99, 'Invalid plan selected']))
    t(check('progressive_tax', (progressive_tax(15000), progressive_tax(35000)), (0, 375.0)))
    parf = [(5, 0.75), (6, 0.70), (7, 0.65), (8, 0.60), (9, 0.55), (10, 0.50)]
    t(check('PARF', [int(arf * band_lookup_upper(days / 365, parf)) for days, arf in
                     ((578, 9370), (3074, 20546), (3403, 50320), (3285, 71269))],
            [7027, 11300, 25160, 39197]))
    t(check('COE', int(49430 * (3650 - 578) / 3650), 41602))
    t(check('rebate', [compute_rebate(True, '1', 7), compute_rebate(True, '1', 8),
                       compute_rebate(False, '1', 10), compute_rebate(True, '3', 7),
                       compute_rebate(True, 'E', 1)], [1.0, 0.0, 0.0, 0.5, 0.0]))
    t(check('category_rule', [category_rule('Liquids', 120), category_rule('Food', 2),
                              category_rule('Tools', 1)], [False, True, 'Contact Staff']))
    food = [in_range(tmp, 75, 100) or (in_range(tmp, 60, 75, True, False) and held >= 2)
            for tmp, held in ((101.0, 2), (100.0, 0), (74.5, 1), (74.5, 2), (58.0, 10))]
    t(check('food safe', food, [False, True, False, True, False]))
    t(check('bmr', (bmr(68.0, 175.0, 30, 'M'), bmr(55.0, 160.0, 25, 'F')), (1628, 1264)))

    # [S3]
    t(check('count_char_types', count_char_types('Ab1!'), (1, 1, 1, 1)))
    t(check('non digits', count_non_digits_each(['1-2-3-4-5-6', '32!*-4*5*6-', '2023-24-T1-SMU-SCIS']),
            [5, 6, 12]))
    t(check('even idx', [digits_at_even_index(s) for s in
                         ('123456', 'SMU-1-2-3-4', '32!*-4*5(0)36', '2023SMU-SCIS1', 'SCIS-1', '')],
            ['135', '1234', '36', '221', '', '']))
    t(check('alt_rev', [alternate_and_reverse(a, b) for a, b in
                        (('', ''), ('', 'abcde'), ('xyz123', ''), ('abc', 'def'),
                         ('abcde', '123'), ('xyz', '78901'))],
            ['', 'edcba', '321zyx', 'adbecf', 'a1b2c3ed', 'x7y8z910']))
    t(check('caesar', (caesar_shift('Abz!', 1), caesar_shift('Bca!', -1)), ('Bca!', 'Abz!')))
    t(check('rle', run_length_encode('aaabcc'), 'a3 b1 c2'))
    t(check('reverse words', reverse_each_word('Hi there'), 'iH ereht'))
    t(check('split_on_many', [split_on_many(s) for s in ('Hello!world?Python,rocks', 'Go.Go!Go')],
            [['Hello', 'world', 'Python', 'rocks'], ['Go', 'Go', 'Go']]))
    t(check('extract_between', extract_between('a <b>x</b> c <b>y</b>', '<b>', '</b>'), ['x', 'y']))
    t(check('length prefixed', [parse_length_prefixed(s) for s in
                                ('018Finished yer examsMYSvkSjjmVcDUZuXEYxE', '000bnFZVgqsMkrv',
                                 '013"Report him!"uzyFrNeElcMCZwSCDPi')],
            ['Finished yer exams', '', '"Report him!"']))
    txt, chk = split_text_and_checksum(parse_length_prefixed('024Has anyone seen Morbo?09lNIz'))
    t(check('checksum', (txt, count_in_set(txt, VOWELS), count_in_set(txt, VOWELS) == chk),
            ('Has anyone seen Morbo?', 8, False)))
    t(check('special words', words_with_special_char(
        "Wow! There are 3 lazy Dogs! Hey, how much was this? It's just $10 dollars.".split(' ')), 7))
    t(check('shorter', [count_shorter_than(['abcd', '123', '**', '!@#$%^'], 4),
                        count_shorter_than([''], 1), count_shorter_than([], 1)], [2, 1, 0]))
    t(check('larger_than_all', larger_than_all([4, 6, 10], [1, 3, 5]), [6, 10]))
    t(check('longest', [longest_string(['grape', 'lime', 'pear']), longest_string(['grape', 'apple', 'pear']),
                        longest_string(['']), longest_string([])],
            [('grape', 5), ('apple', 5), ('', 0), None]))
    t(check('last letter', (index_of_last_letter('ab12'), index_of_last_letter('123')), (1, -1)))
    t(check('numbers_in_string', numbers_in_string('A:1.7m, B:1.65m'), [1.7, 1.65]))
    t(check('pad', (pad_or_truncate('hello', 8), pad_or_truncate('COR-IS1704 Lab 4', 8)),
            ('   hello', 'COR-IS17')))
    t(check('pangram', is_pangram('The quick brown fox jumps over the lazy dog'), True))

    # [S4]
    ship = [(9.9, 4), (11.25, 5), (10.0, 10), (18.70, 100)]
    t(check('sum_where', (sum_where(ship, 1, 0, 10.0), sum_where([(13.0, 4)], 1, 0, 10.0),
                          sum_where([], 1, 0, 10.0)), (14, 0, None)))
    b_list = [(1, 2, 3), (4, 5, 6, 0), (7, 8, 9, 10, 11, 12), (10, 4)]
    t(check('first+last', first_plus_last_at_least(b_list, 14), [(7, 8, 9, 10, 11, 12), (10, 4)]))
    patients = [("John Doe", 45, "Male", ["Diabetes"], True),
                ("Jane Smith", 38, "Female", ["Hypertension", "Asthma"], False),
                ("Sam Brown", 60, "Male", ["Asthma"], True),
                ("Anna White", 29, "Female", ["Allergy"], True)]
    t(check('patients', patient_stats(patients),
            (43.0, 2, 2, 3, ["Diabetes", "Hypertension", "Asthma", "Allergy"])))
    cards = [('Arcanine', 'fire', 91, 110, 80), ('Pikachu', 'electric', 35, 55, 40),
             ('Machop', 'fighting', 70, 80, 50), ('Charmander', 'fire', 69, 52, 43),
             ('Charizard', 'fire', 78, 84, 78), ('Diglett', 'ground', 10, 56, 25),
             ('Eevee', 'normal', 55, 55, 52), ('Squirtle', 'water', 44, 48, 68),
             ('Raichu', 'electric', 60, 90, 55)]
    cats = ['electric', 'fighting', 'fire', 'ground', 'normal', 'water']
    t(check('counts_per_category', counts_per_category(cards[1:2] + cards[3:4], 1, cats),
            (1, 0, 1, 0, 0, 0)))
    t(check('best avg', (best_average_per_category(cards, 1, 2, cats),
                         best_average_per_category(cards, 1, 4, cats)),
            (('fire', 79.33), ('water', 68.0))))
    two = [('Pikachu', 'electric', 35, 55, 40), ('Charmander', 'fire', 39, 52, 43)]
    t(check('pokemon info', (average(column(two, 2)), find_best(two, 3, 0), find_best(two, 4, 0)),
            (37.0, 'Pikachu', 'Charmander')))
    t(check('neighbour_sums', neighbour_sums([56, -10, 25, -32]), [46, 71, -17, -7]))
    t(check('merge_alternate', merge_alternate([1, 3, 5, 7], [2, 4]), [1, 2, 3, 4, 5, 7]))
    t(check('non_common', non_common_items(['a', 'b', 'c', 'd'], ['b', 'd', 'e', 'f']),
            ['a', 'c', 'e', 'f']))
    t(check('all_pairs', all_pairs(['a', 'b'], [1, 2]), [('a', 1), ('a', 2), ('b', 1), ('b', 2)]))
    t(check('span', (span_ok([2021, 2022, 2021]), span_ok([2020, 2022])), (True, False)))
    t(check('max_count', (max_count_ok(['scis', 'bus', 'scis'], 2),
                          max_count_ok(['scis'] * 3, 2)), (True, False)))
    t(check('adjacent circular', adjacent_pairs(['A', 'B', 'C'], True),
            [('A', 'B'), ('B', 'C'), ('C', 'A')]))
    t(check('chain', chain_from_pairs([('Mary', 'Jason'), ('John', 'Alan'), ('Jason', 'George'),
                                       ('Alan', 'Christie'), ('Christie', 'Mary')]),
            ['John', 'Alan', 'Christie', 'Mary', 'Jason', 'George']))
    t(check('transpose', transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]]))
    t(check('insertion sort', insertion_sort_by([('a', 3), ('b', 1), ('c', 3), ('d', 2)], 1),
            [('b', 1), ('d', 2), ('a', 3), ('c', 3)]))
    t(check('swaps', try_all_swaps([1, 9], [2, 3], lambda tbl: sum(tbl) <= 6),
            None))
    t(check('swaps found', try_all_swaps([1, 9], [2, 3], lambda tbl: sum(tbl) <= 12)[:2], (1, 2)))
    people = [('Apple', 85.0, 190.0, 22, 'M'), ('Orange', 55.0, 160.0, 25, 'F'),
              ('Pear', 60.0, 165.0, 30, 'F'), ('Durian', 90.0, 165.0, 45, 'M'),
              ('Grape', 65.0, 190.0, 45, 'M')]
    in_band = []
    for p in people:
        v = bmr(p[1], p[2], p[3], p[4])
        if 1264 <= v < 1932:
            in_band.append((p[0], v))
    t(check('numbered_join', numbered_join(in_band),
            '1-Orange(1264)-2-Pear(1320)-3-Durian(1711)-4-Grape(1617)'))

    # [S5] - [S8] with real sample files
    with tempfile.TemporaryDirectory() as d:
        tours = make_file(d, 'tours.txt', 'TOUR!PLACES!PRICE\nRiver Walk!12!18.50\n'
                          'Heritage Trail!8!24.00\nGarden Visit!15!16.00\nNight Tour!6!28.50\n')
        recs = read_typed(tours, '!', [str, int, float], True)
        suitable = [(n, p * 4) for n, places, p in recs if places >= 4 and p * 4 <= 80.0]
        t(check('tours', suitable, [('River Walk', 74.0), ('Garden Visit', 64.0)]))

        poke = make_file(d, 'poke.txt', 'pokedex_number,name,type_2,height_m\n'
                         '1,Bulbasaur,Poison,0.7\n4,Charmander,,0.6\n')
        dicts = read_header_dicts(poke)
        t(check('header dicts', dicts,
                [{'pokedex_number': 1, 'name': 'Bulbasaur', 'type_2': 'Poison', 'height_m': 0.7},
                 {'pokedex_number': 4, 'name': 'Charmander', 'type_2': None, 'height_m': 0.6}]))
        t(check('select_fields', select_fields(dicts, ['name', 'bogus']),
                [{'name': 'Bulbasaur'}, {'name': 'Charmander'}]))
        t(check('smart_convert', [smart_convert(x) for x in ('', '12', '0.7', '-3', 'a.b', '1.2.3')],
                [None, 12, 0.7, -3, 'a.b', '1.2.3']))

        swim = make_file(d, 'swim.csv', 'Michael Phelps,50m doggy paddle,60\nShanti Pereira,50m backstroke,42\n'
                         'Shanti Pereira,50m breaststroke,35\nMichael Phelps,50m doggy paddle,65\n')
        t(check('count_rows', (count_rows(swim), count_rows(swim, ',', 0, 'Shanti Pereira')), (4, 2)))
        t(check('count_and_average', [count_and_average(swim, ',', {0: n, 1: e}, 2) for n, e in
                                      (('Michael Phelps', '50m doggy paddle'),
                                       ('Shanti Pereira', '50m backstroke'),
                                       ('Shanti Pereira', '50m doggy paddle'))],
                [(2, 62), (1, 42), (0, 0)]))

        loans = make_file(d, 'loans.txt', 'S**11111,DBS000001,HOM-LOAN,$100000\n'
                          'S**11111,SCB000001,BIZ-LOAN,$100000\nS**11111,UOB000001,CAR-LOAN,$125000\n'
                          'T**11112,DBS000002,EDU-LOAN,$125000\nS**11115,SCB000002,CAR-LOAN,$100000\n')
        t(check('loan report', (report_with_total(loans, 'DBS'), report_with_total(loans, 'ABC')),
                ([('S**11111', 'DBS000001', 'HOM-LOAN', 100000), ('T**11112', 'DBS000002', 'EDU-LOAN', 125000),
                  ('Total Loan Amount', 225000)], [])))

        sample = make_file(d, 's1.txt', "Wow! There are 3 lazy Dogs!\nHey, how much was this? It's just $10 dollars.\n")
        t(check('special file', special_word_count_file(sample), 7))

        inv = make_file(d, 'inv.txt', 'Laptop,Electronics,$1200.00,$1100.00,25\nPhone,Electronics,800.00,$700.00,50\n'
                        'Chair,Furniture,$60.00,50.00,100\nSofa,Furniture,$960.00,$800.00,10\n'
                        'TV,Electronics,500.00,$400.00,30\nTable,Furniture,$140.00,100.00,20\n'
                        'Headphones,Electronics,$150.00,$100.00,60\nRefrigerator,Appliances,1200.00,$700.00,8\n'
                        'Microwave,Appliances,$200.00,$100.00,15\nLamp,Furniture,$40.00,$15.00,40\n')
        stock_info = inventory_with_min_stock(inv)
        t(check('min stock', stock_info,
                {'Laptop': [25, 15], 'Phone': [50, 15], 'Chair': [100, 8], 'Sofa': [10, 8], 'TV': [30, 8],
                 'Table': [20, 8], 'Headphones': [60, 3], 'Refrigerator': [8, 3], 'Microwave': [15, 3],
                 'Lamp': [40, 3]}))
        stock = {}
        for name in stock_info:
            stock[name] = stock_info[name][0]
        orders = [(1, 'Alice', 'Laptop', 20), (2, 'Bob', 'Phone', 50), (3, 'Carol', 'Chair', 10),
                  (4, 'David', 'TV', 30), (5, 'Alice', 'Headphones', 40), (6, 'Bob', 'Sofa', 10),
                  (7, 'Carol', 'Microwave', 20), (8, 'David', 'Table', 10)]
        t(check('orders', fulfil_orders(stock, orders),
                {'Alice': [(1, 'Laptop', 20, 20), (5, 'Headphones', 40, 40)],
                 'Bob': [(2, 'Phone', 50, 50), (6, 'Sofa', 10, 10)],
                 'Carol': [(3, 'Chair', 10, 10), (7, 'Microwave', 20, 15)],
                 'David': [(4, 'TV', 30, 30), (8, 'Table', 10, 10)]}))

        weather = make_file(d, 'w.txt', '2023-10-01|Rivertown|25.5|15.1|0.0\n2023-11-15|Sunnyvale|19.9|8.5|10.2\n'
                            '2023-10-01|Sunnyvale|28.1|16.3|0.0\n2023-10-02|Rivertown|24.9|14.0|5.5\n'
                            '2023-11-16|Sunnyvale|18.5|7.9|12.1\n2023-10-02|Sunnyvale|27.5|15.8|2.1\n')
        t(check('weather', [weather_stats(weather, (2023, 11, 15), (2023, 11, 16)),
                            weather_stats(weather, (2023, 10, 1), (2023, 10, 31)),
                            weather_stats(weather, (2023, 10, 3), (2023, 11, 15))],
                [{'Sunnyvale': (2, 19.2, 22.3)}, {'Rivertown': (2, 25.2, 5.5), 'Sunnyvale': (2, 27.8, 2.1)},
                 {'Sunnyvale': (1, 19.9, 10.2)}]))
        rows = []
        for cols in read_rows(weather, '|'):
            rows.append((cols[1], parse_date(cols[0]), float(cols[2])))
        t(check('group_by', group_by(rows, 0)['Rivertown'], [((2023, 10, 1), 25.5), ((2023, 10, 2), 24.9)]))

        nums = make_file(d, 'nums.txt', '1 2 3#4 5\n10\n')
        out = os.path.join(d, 'out.txt')
        group_averages_file(nums, out)
        t(check('mock q3', read_lines(out), ['2: 2.0#4.5', '1: 10.0', 'Total number of groups: 3',
                                             'Maximum average: 10.0']))

    # [S6] / [S7]
    t(check('frequency', frequency('abca'), {'a': 2, 'b': 1, 'c': 1}))
    t(check('invert_to_lists', invert_to_lists({'Ann': 'SCIS', 'Bob': 'LKCSB', 'Cat': 'SCIS'}),
            {'SCIS': ['Ann', 'Cat'], 'LKCSB': ['Bob']}))
    t(check('alternating', dict_from_alternating(['Ann', 'a@x', 'Bob', 'b@x']), {'Ann': 'a@x', 'Bob': 'b@x'}))
    em = {'Ann': 'a@x'}
    t(check('set_and_return_old', (set_and_return_old(em, 'Ann', 'z@x'), set_and_return_old(em, 'Bo', 'b')),
            ('a@x', None)))
    t(check('kv pairs', parse_key_value_pairs('id:1\tname:Ann'), {'id': '1', 'name': 'Ann'}))
    t(check('date range', in_date_range((2023, 10, 20), (2023, 10, 3), (2023, 11, 15)), True))
    t(check('hhmm', (hhmm_to_minutes('09:30'), minutes_to_hhmm(570)), (570, '09:30')))

    # [S8] boards
    t(check('board', board_from_moves(3, '11x20o22x10o00x'), ['x--', 'ox-', 'o-x']))
    t(check('who_won', (who_won(3, ['x--', 'ox-', 'o-x']), who_won(3, ['xox', 'oxo', 'oxo']),
                        who_won(3, ['xo-', '---', '---'])), ('x', 'tie', None)))
    g = ['---', '---', '---']
    drop_into_column(g, 1, 'x')
    drop_into_column(g, 1, 'o')
    t(check('gravity', g, ['---', '-o-', '-x-']))
    wallet = [5, 5, 1, 2]
    t(check('remove_items', (remove_items(wallet, [5, 5]), wallet, remove_items(wallet, [5])),
            (True, [1, 2], False)))

    # [S9]
    t(check('frog 1d counts', [all_jump_sequences_1d(m)[0] for m in ('A00**0*00B', 'A0000B', 'A000*****B')],
            [6, 13, 0]))
    t(check('frog 1d seqs', sorted(all_jump_sequences_1d('A00**0*00B')[1]),
            sorted([[2, 3, 2, 2], [1, 1, 3, 2, 2], [2, 3, 3, 1], [1, 1, 3, 3, 1], [2, 3, 2, 1, 1],
                    [1, 1, 3, 2, 1, 1]])))
    t(check('frog 2d counts', [all_jump_sequences_2d(m)[0] for m in
                               (['A00*', '00*0', '**0B'], ['A***', '*000', '*000', '*00B'], ['A00', '000', '00B'])],
            [5, 0, 14]))
    t(check('frog 2d seqs', sorted(all_jump_sequences_2d(['A00*', '00*0', '**0B'])[1]),
            sorted([[(1, 'd'), (3, 'r'), (1, 'd')], [(1, 'r'), (1, 'd'), (2, 'r'), (1, 'd')],
                    [(1, 'd'), (1, 'r'), (2, 'r'), (1, 'd')], [(2, 'r'), (2, 'd'), (1, 'r')],
                    [(1, 'r'), (1, 'r'), (2, 'd'), (1, 'r')]])))
    t(check('grid paths', count_grid_paths(['000', '000', '000']), 6))
    t(check('combinations', combinations_of([1, 2, 3], 2), [(1, 2), (1, 3), (2, 3)]))
    t(check('closest subsets', closest_subsets_at_least([5, 5, 1, 2], 9), [(5, 5)]))
    t(check('min alloc 1d', [min_allocation_1d(r) for r in
                             ([3], [0, 3, 5], [9, 6, 5, 2], [0, 3, 3, 5], [7, 6, 6, 3], [2, 6, 5, 6, 2])],
            [[1], [1, 2, 3], [4, 3, 2, 1], [1, 2, 1, 2], [2, 1, 2, 1], [1, 2, 1, 2, 1]]))
    t(check('min alloc grid', [min_allocation_grid(gr) for gr in
                               ([[1, 0, 2], [0, 1, 2]],
                                [[1, 2, 3, 1], [0, 1, 5, 2], [2, 3, 4, 1]],
                                [[1, 2, 3, 1, 7], [0, 1, 7, 2, 1], [2, 3, 4, 1, 5]],
                                [[3, 2, 1, 1, 7], [0, 1, 7, 2, 2], [2, 4, 4, 1, 5], [6, 5, 4, 4, 5]])],
            [[[2, 1, 2], [1, 2, 3]],
             [[2, 3, 4, 1], [1, 2, 5, 2], [2, 3, 4, 1]],
             [[2, 3, 4, 1, 2], [1, 2, 5, 2, 1], [2, 3, 4, 1, 2]],
             [[4, 3, 1, 1, 2], [1, 2, 3, 2, 1], [2, 3, 2, 1, 2], [5, 4, 1, 2, 3]]]))

    # [S10]
    t(check('triangle', triangle_lines('*', 3), ['  *', ' ***', '*****']))
    t(check('frame', frame_lines('#', 3, 4), ['####', '#  #', '####']))

    print(f'{sum(results)}/{len(results)} checks passed')
