import re


def divide_to_substrings(password) -> set:
    substrings = {password}
    for x in range(len(password)):
        for y in range(len(password)):
            temp = password[x:y]
            if len(temp) > 2:
                substrings.add(temp)
    return substrings


def is_blacklisted(password):
    """
    Cheking all substrings of 3+ symbols for being a password in the blacklist.
    USE RE.SEARCH !!!
    """
    pass


def has_english_word(password):
    from nltk.corpus import words
    psswrd = password.lower()
    english_vocab = filter(lambda x: len(x) > 2, set(word.lower() for word in words.words()))
    substrings = divide_to_substrings(psswrd)
    return substrings.intersection(english_vocab)


def simple_leet_decoding(password):
    leet = {
        '0': 'o',
        '1': 'i',
        '2': 'z',
        '3': 'e',
        '4': 'a',
        '5': 's',
        '6': 'g',
        '7': 't',
        '8': 'b',
        '9': 'q'
    }
    lookup = password.split()
    for index, letter in enumerate(lookup):
        if letter in leet:
            lookup[index] = leet[letter]
    return "".join(lookup)


def has_sequences(password):
    """
    Cheking all substrings of 3+ symbols for being a digit sequence, e.g. Pi, Fibonacci, factorials;
    or a letter sequence, e.g. 'abcdefg', 'zyxwvut', etc.
    USE RE.SEARCH !!!
    """
    pass


def has_dates(password):
    """
    Cheking all substrings of 3+ symbols for being a calendar date in any format, e.g.
    131298, 12.28.78, 15/01/2014, etc.
    USE RE.SEARCH !!!
    """
    pass


def has_repeates(password):
    """
    Cheking all substrings of 3+ symbols for being repeats of one symbol, e.g.
    'aaa', '777', '{{{', etc.
    USE RE.SEARCH !!!
    """
    pass


def is_weak(password):
    return is_blacklisted(password) or has_english_word(password) or has_sequences(password) \
           or has_dates(password) or has_repeates(password)


def is_ascii(password):
    return re.fullmatch(r"[a-zA-Z0-9_`~!@#$%\^&*()\-+=/{\}\[\]\\|;':\",.<>?]+", password)


def only_digits(password):
    return re.fullmatch(r"[0-9]+", password)


def only_lower(password):
    return re.fullmatch(r"[a-z]+", password)


def has_special(password):
    return re.search(r"[_`~!@#$%\^&*()\-+=/{\}\[\]\\|;':\",.<>?]", password)


def has_digits(password):
    return re.search(r"[0-9]", password)


def has_lower(password):
    return re.search(r"[a-z]", password)


def has_upper(password):
    return re.search(r"[A-Z]", password)


def get_password_strength(password) -> tuple:
    assert is_ascii(password)
    conditions = (
        only_digits(password),
        only_lower(password),
        has_lower(password),
        has_digits(password),
        has_upper(password),
        has_special(password)
    )
    score = 0
    text = None

    def count_entropy_bits():
        bits_for_symbol = 0
        if conditions[0]:
            bits_for_symbol = 3.3219
        if conditions[1]:
            bits_for_symbol = 4.7004
        if conditions[2]:
            if conditions[3] and not conditions[4] and not conditions[5]:
                bits_for_symbol = 5.1699
            if not conditions[3] and conditions[4] and not conditions[5]:
                bits_for_symbol = 5.7004
            if conditions[3] and conditions[4] and not conditions[5]:
                bits_for_symbol = 5.9542
            if conditions[3] and conditions[4] and conditions[5]:
                bits_for_symbol = 6.5699
        return bits_for_symbol * len(password)

    def count_entropy_bonus(bits):
        bonus = (bits - 40) // 20
        if bonus < 0:
            return 0
        else:
            return bonus

    if is_weak(password) or is_weak(simple_leet_decoding(password)):
        score = 0
        text = ("Your password is very weak.\n",
                "Don't use:\n",
                "- Simple passwords, like '1234567', 'password00', 'adm1n', etc.\n",
                "- English words inside your passwords, even with replacing some characters with digits.\n",
                "- Letter sequences like 'abcdef', 'qwertyuiop', etc.",
                "- Calendar dates like '131298', '12.28.78', '15/01/2014', etc.",
                "- Digit sequences like Pi or Fibonacci numbers.")
    elif conditions[0]:
        score = 1
        text = ("Your password consists only of 0-9 digits.\n",
                "Add lowercase and uppercase latin letters and special symbols (~, @, #, etc.).")
    elif conditions[1]:
        score = 2
        text = ("Your password consists only of lowercase latin letters.\n",
                "Add 0-9 digits, uppercase latin letters and special symbols (~, @, #, etc.).")
    elif conditions[3]:
        score = 2
        if conditions[4]:
            score += 1
        if conditions[5]:
            score += 1
        if conditions[6]:
            score += 1
        score += count_entropy_bonus(count_entropy_bits())
        if score > 10:
            score = 10
    return score, "".split(text)

# if len(password) < 6:
#     return 1, "Your password's length should be more than 6."
# if is_weak(password) or is_weak(simple_leet_decoding(password)):
#     return (2, "Your password is very weak.\n"
#                "Don't use:\n"
#                "- Simple passwords, like '1234567', 'password00', 'adm1n', etc.\n"
#                "- English words inside your passwords, even with replacing some characters with digits.\n"
#                "- Calendar dates or digit sequences like Pi or Fibonacci numbers.")
# if pass_bigger(5):
#     if only_digits(password):
#         return (3, "Your password consists only of 0-9 digits.\n"
#                    "Add lowercase and uppercase latin letters and special symbols (~, @, #, etc.).")
#     if only_lower(password):
#         return (4, "Your password consists only of lowercase latin letters.\n"
#                    "Add 0-9 digits, uppercase latin letters and special symbols (~, @, #, etc.).")
# if pass_bigger(9) and not has_special(password):
#     if has_digits(password) and has_lower(password) and not has_upper(password):
#         return (5, "Your password consists only of 0-9 digits and lowercase latin letters.\n"
#                    "Add uppercase latin letters and special symbols (~, @, #, etc.).")
#     if not has_digits(password) and has_lower(password) and has_upper(password):
#         return (6, "Your password consists only of lowercase and uppercase latin letters.\n"
#                    "Add 0-9 digits and special symbols (~, @, #, etc.).")
#     if has_digits(password) and has_lower(password) and has_upper(password):
#         return (7, "Your password consists only of 0-9 digits, lowercase and uppercase latin letters.\n"
#                    "Add special symbols (~, @, #, etc.).")
# if (has_digits(password) or has_lower(password) or has_upper(password))\
#         and (not pass_bigger(9) and not has_special(password)):
#     return (4, "Your password's length should be more than 9 to have bigger strength.\n"
#                "Also you should add special symbols (~, @, #, etc.).")
# if has_special(password) and has_digits(password) and has_lower(password) and has_upper(password):
#     if pass_bigger(12) and not pass_bigger(15) and not pass_bigger(18):
#         return 8, "This is good password! Add more symbols to make it stronger."
#     elif pass_bigger(15) and not pass_bigger(18):
#         return 9, "This is great password! Add more symbols to make it stronger."
#     elif pass_bigger(18):
#         return 10, "This is awesome password! Add more symbols to make it stronger."
#     else:
#         return 7, "Your password's length should be more than 12 to have bigger strength."


def display(message: tuple):
    print("Password's strength: {0} out of 10.\n{1}\n".format(*message))


if __name__ == "__main__":
    while True:
        example = input("Enter a password: ")
        if example:
            try:
                result = get_password_strength(example)
                display(result)
            except AssertionError:
                print("Your password should contain only ASCII printable characters (except whitespace).")
                continue
        else:
            break
