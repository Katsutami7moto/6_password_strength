def is_common(password):
    pass


def has_english_word(password):
    pass


def has_modified_english_word(password):
    pass


def has_famous_digit_sequence(password):
    pass


def has_dates(password):
    pass


def is_weak(password):
    return is_common(password) or has_english_word(password) or has_modified_english_word(password)\
           or has_famous_digit_sequence(password) or has_dates(password)


def only_digits(password):
    for symbol in password:
        if not symbol.isdigit():
            return False
    return True


def get_password_strength(password):
    def pass_len(number):
        return len(password) > number

    if len(password) < 6:
        return tuple([1, "Your password should be 6 or more symbols long."])
    if is_weak(password):
        return tuple([2, "You are using one of common passwords or an english word inside your password."])
    if only_digits(password) and pass_len(5):
        return tuple([3, "Your password consists only of 0-9 digits."
                         "Add lowercase and uppercase latin letters and special symbols (~, @, # and so on)."])
    pass


def display(message):
    print("Mark: {0}.\n{1}".format(*message))


if __name__ == '__main__':
    psswrd = input("Enter a password: ")
    result = get_password_strength(psswrd)
    display(result)
