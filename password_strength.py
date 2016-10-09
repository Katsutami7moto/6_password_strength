import re


def divide_to_substrings(password: str, minimum: int) -> set:
    substrings = {password}
    for x in range(len(password)):
        for y in range(len(password)):
            temp = password[x:y]
            if len(temp) > (minimum - 1):
                substrings.add(temp)
    return substrings


def check_in_list(password: str, filepath: str) -> set:
    with open(filepath, encoding='utf-8', newline='\n') as handle:
        blacklist = set(map(lambda x: x[:-1], filter(lambda x: len(x) > 3, handle)))
        substrings = divide_to_substrings(password, 4)
        return substrings.intersection(blacklist)


def check_black_or_english(password: str) -> bool:
    check_black = check_in_list(password, 'blacklist_1kk.txt')
    check_black_leet = check_in_list(simple_leet_decoding(password), 'blacklist_1kk.txt')
    check_eng = check_in_list(password.lower(), 'english.txt')
    check_eng_leet = check_in_list(simple_leet_decoding(password.lower()), 'english.txt')
    return check_black or check_eng or check_black_leet or check_eng_leet


def simple_leet_decoding(password: str) -> str:
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
    lookup = list(password)
    for index, letter in enumerate(lookup):
        if letter in leet:
            lookup[index] = leet[letter]
    return "".join(lookup)


def has_dates(password: str) -> bool:
    return re.search(r"(\d{2}(\d{2})?(\.|/)?){3}", password)


def has_repeates(password: str) -> bool:
    return re.search(r"(.)\1\1+", password) or re.search(r"(...+)\1+", password)


def is_weak(password: str) -> bool:
    return check_black_or_english(password) or has_dates(password) or has_repeates(password)


def is_ascii(password: str) -> bool:
    return re.fullmatch(r"[a-zA-Z0-9_`~!@#$%\^&*()\-+=/{\}\[\]\\|;':\",.<>?]+", password)


def has_special(password: str) -> bool:
    return re.search(r"[_`~!@#$%\^&*()\-+=/{\}\[\]\\|;':\",.<>?]", password)


def has_digits(password: str) -> bool:
    return re.search(r"[0-9]", password)


def has_lower(password: str) -> bool:
    return re.search(r"[a-z]", password)


def has_upper(password: str) -> bool:
    return re.search(r"[A-Z]", password)


def get_password_strength(password: str) -> tuple:
    assert is_ascii(password)
    conditions = (
        password.isdigit(),
        has_lower(password) and not has_digits(password) and not has_upper(password) and not has_special(password),
        has_lower(password),
        has_digits(password),
        has_upper(password),
        has_special(password),
        has_digits(password) and not has_upper(password) and not has_special(password),
        not has_digits(password) and has_upper(password) and not has_special(password),
        has_digits(password) and has_upper(password) and not has_special(password),
        has_digits(password) and has_upper(password) and has_special(password)
    )
    score = 0
    text = []

    def count_entropy_bits() -> float:
        bits_for_symbol = 0
        if conditions[0]:
            bits_for_symbol = 3.3219
        elif conditions[1]:
            bits_for_symbol = 4.7004
        elif conditions[2]:
            if conditions[6]:
                bits_for_symbol = 5.1699
            elif conditions[7]:
                bits_for_symbol = 5.7004
            elif conditions[8]:
                bits_for_symbol = 5.9542
            elif conditions[9]:
                bits_for_symbol = 6.5699
        return bits_for_symbol * len(password)

    def count_entropy_bonus(bits: float) -> int:
        bonus = (bits - 20) // 20
        if bonus < 0:
            return 0
        else:
            return bonus

    if is_weak(password) or conditions[0]:
        score = 1
        text = ["Your password is very weak.\n",
                "Don't use:\n",
                "- Only digits: add other types of characters.\n",
                "- Simple passwords, like '1234567', 'password00', 'adm1n', etc.\n",
                "- English words inside your passwords, even with replacing some characters with digits.\n",
                "- Calendar dates like '131298', '12.28.78', '15/01/2014', etc.\n",
                "- Any kinds of repeates: 'aaa', 'a1A~a1A~', etc.\n"]
    elif conditions[1]:
        score = 2
        text = ["Your password consists only of lowercase latin letters.\n",
                "Add 0-9 digits, uppercase latin letters and special symbols (~, @, #, etc.).\n"]
    elif conditions[2]:
        score = 2
        if conditions[3]:
            score += 1
        if conditions[4]:
            score += 1
        if conditions[5]:
            score += 1
        score += count_entropy_bonus(count_entropy_bits())
        if conditions[6]:
            text = ["Your password consists only of 0-9 digits and lowercase latin letters.\n",
                    "Add uppercase latin letters and special symbols (~, @, #, etc.).\n"]
        elif conditions[7]:
            text = ["Your password consists only of lowercase and uppercase latin letters.\n",
                    "Add 0-9 digits and special symbols (~, @, #, etc.).\n"]
        elif conditions[8]:
            text = ["Your password consists only of 0-9 digits, lowercase and uppercase latin letters.\n",
                    "Add special symbols (~, @, #, etc.).\n"]
        elif conditions[9]:
            text = ["This is good password! :)\n"]
        if score >= 10:
            score = 10
            text = ["Awesome password!\n",
                    "You don't need to do anything with it :)\n"]
        else:
            text.append("You may add more symbols to your password to make it stronger.\n")
    return int(score), "".join(text)


def display(message: tuple) -> bool:
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
