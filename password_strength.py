import re
from nltk.corpus import words


def is_common(password):
    """
    Cheking all substrings of 3+ symbols for being a common password.
    USE RE.SEARCH !!!
    """
    pass


def has_english_word(password):
    for word in words.words():
        if re.search(word, password):
            return True
    return False


def has_modified_english_word(password):
    """
    Cheking all substrings of 3+ symbols for being an english word with some symbols,
    replaced by digits or divided by special symbols.
    USE RE.SEARCH !!!
    """
    pass


def has_famous_digit_sequence(password):
    """
    Cheking all substrings of 3+ symbols for being a digit sequence, e.g. Pi, Fibonacci, factorials.
    USE RE.SEARCH !!!
    """
    pass


def has_dates(password):
    """
    Cheking all substrings of 3+ symbols for being a calendar date in any format, e.g.
    131298, 122878, 15012014, etc.
    USE RE.SEARCH !!!
    """
    pass


def is_weak(password):
    return is_common(password) or has_english_word(password) or has_modified_english_word(password) \
           or has_famous_digit_sequence(password) or has_dates(password)


def only_digits(password):
    return re.fullmatch(r"[0-9]+", password)


def is_ascii(password):
    return re.fullmatch(r"[a-zA-Z0-9_`~!@#$%\^&*()\-+=/{\}\[\]\\|;':\",.<>? ]+", password)


def only_lower(password):
    return re.fullmatch(r"[a-z]+", password)


def has_special(password):
    return re.search(r"[_`~!@#$%\^&*()\-+=/{\}\[\]\\|;':\",.<>? ]", password)


def has_digits(password):
    return re.search(r"[0-9]", password)


def has_lower(password):
    return re.search(r"[a-z]", password)


def has_upper(password):
    return re.search(r"[A-Z]", password)


def get_password_strength(password):
    def pass_bigger(number):
        return len(password) > number

    assert is_ascii(password)

    if len(password) < 6:
        return tuple([1, "Your password's length should be more than 6."])
    if is_weak(password):
        return tuple([2, "Your password is very weak.\n"
                         "Don't use:\n"
                         "- Simple passwords, like '1234567', 'password00', 'adm1n'.\n"
                         "- English words inside your passwords, even with replacing some characters with digits.\n"
                         "- Calendar dates or digit sequences like Pi or Fibonacci numbers."])
    if pass_bigger(5):
        if only_digits(password):
            return tuple([3, "Your password consists only of 0-9 digits.\n"
                             "Add lowercase and uppercase latin letters and special symbols (~, @, #, etc.)."])
        if only_lower(password):
            return tuple([4, "Your password consists only of lowercase latin letters.\n"
                             "Add 0-9 digits, uppercase latin letters and special symbols (~, @, #, etc.)."])
    if pass_bigger(9) and not has_special(password):
        if has_digits(password) and has_lower(password) and not has_upper(password):
            return tuple([5, ""])
        if not has_digits(password) and has_lower(password) and has_upper(password):
            return tuple([6, ""])
        if has_digits(password) and has_lower(password) and has_upper(password):
            return tuple([7, ""])
    if has_digits(password) or has_lower(password) or has_upper(password)\
            and not pass_bigger(9) and not has_special(password):
        return tuple([4, "Your password's length should be more than 9 to have bigger score.\n"
                         "Also you should add special symbols (~, @, #, etc.)."])
    if has_special(password) and has_digits(password) and has_lower(password) and has_upper(password):
        if pass_bigger(12):
            return tuple([8, ""])
        elif pass_bigger(15):
            return tuple([9, ""])
        elif pass_bigger(18):
            return tuple([10, ""])
        else:
            return tuple([7, "Your password's length should be more than 12 to have bigger score."])


def display(message):
    print("Score: {0} out of 10.\n{1}".format(*message))


if __name__ == '__main__':
    psswrd = input("Enter a password: ")
    result = get_password_strength(psswrd)
    display(result)
