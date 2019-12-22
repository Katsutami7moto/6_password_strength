import re
import string

blacklist_1kk = {}
english_words_list = {}


def create_blacklist(filepath: str) -> set:
    with open(filepath, encoding='utf-8') as handle:
        blacklist = map(lambda x: re.sub('[^{}]'.format(string.ascii_letters), '', x[:-1].lower()), handle)
        return set(filter(lambda x: len(x) > 2 and re.search('[aeuioy]', x), blacklist))


def check_in_list(password: str, blacklist: set) -> bool:
    for bad_password in blacklist:
        if bad_password in password:
            return True
    return False


def check_black_or_english(password: str) -> bool:
    check_black = check_in_list(password, blacklist_1kk)
    check_black_leet = check_in_list(simple_leet_decoding(password), blacklist_1kk)
    check_eng = check_in_list(password.lower(), english_words_list)
    check_eng_leet = check_in_list(simple_leet_decoding(password.lower()), english_words_list)
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


def has_dates(password: str):
    return re.search(r"(\d{2}(\d{2})?([./])?){3}", password)


def has_repeates(password: str):
    return re.search(r"(.)\1\1+", password) or re.search(r"(...+)\1+", password)


def is_weak(password: str):
    return check_black_or_english(password) or has_dates(password) or has_repeates(password)


def is_ascii(password: str):
    return re.fullmatch(r"[a-zA-Z0-9_`~!@#$%^&*()\-+=/{\}\[\]\\|;':\",.<>?]+", password)


def has_special(password: str):
    return re.search(r"[_`~!@#$%^&*()\-+=/{\}\[\]\\|;':\",.<>?]", password)


def has_digits(password: str):
    return re.search(r"[0-9]", password)


def has_lower(password: str):
    return re.search(r"[a-z]", password)


def has_upper(password: str):
    return re.search(r"[A-Z]", password)


def count_entropy_bonus(bits: float) -> int:
    bonus = (bits - 20) // 20
    if bonus < 0:
        return 0
    else:
        return int(bonus)


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
        has_digits(password) and has_upper(password) and has_special(password),
        has_upper(password) and not has_lower(password) and not has_digits(password) and not has_special(password)
    )
    score = 0
    text = []

    def count_entropy_bits() -> float:
        """
        Source of entropy bits constants:
        https://en.wikipedia.org/wiki/Password_strength#Random_passwords
        """
        bits_for_symbol = 0
        if conditions[6]:
            bits_for_symbol = 5.170
        elif conditions[7]:
            bits_for_symbol = 5.700
        elif conditions[8]:
            bits_for_symbol = 5.954
        elif conditions[9]:
            bits_for_symbol = 6.555
        return bits_for_symbol * len(password)

    if is_weak(password) or conditions[0]:
        score = 1
        text = ["Your password is very weak.\n",
                "Don't use:\n",
                "- Only digits: add other types of characters.\n",
                "- Simple passwords, like '1234567', 'password00', 'adm1n', etc.\n",
                "- English words inside your passwords, even with replacing some characters with similar digits.\n",
                "- Vowels (a, e, i, o, u, y) and digits (0, 1, 3, 4) ",
                "to avoid taking a random combination of letters for a word.\n",
                "- Calendar dates like '131298', '12.28.78', '15/01/2014', etc.\n",
                "- Any kinds of repeates: 'aaa', 'a1A~a1A~', etc.\n"]
    elif conditions[1] or conditions[10]:
        score = 2
        text = ["Your password consists only of lowercase or uppercase latin letters.\n",
                "Add 0-9 digits, uppercase or lowercase latin letters and special symbols (~, @, #, etc.).\n"]
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
            text = ["This is a good password! :)\n"]
        if score >= 10:
            score = 10
            text = ["Awesome password!\n",
                    "You don't need to do anything with it :)\n"]
        else:
            text.append("You may add more symbols to your password to make it stronger.\n")
    return int(score), "".join(text)


def display(message: tuple):
    print("Password's strength: {0} out of 10.\n{1}\n".format(*message))


def unit_tests():
    # Testing weak passwords
    assert get_password_strength('987bearuhn98y8')[0] == 1
    assert get_password_strength('youaremynumberoneassisstantforever')[0] == 1
    assert get_password_strength('Password1')[0] == 1
    assert get_password_strength('adminadmin')[0] == 1
    assert get_password_strength('9w3r7yu10p')[0] == 1
    assert get_password_strength('jkjghg12121999,;].;')[0] == 1
    assert get_password_strength('d;Fs28/11/56]-g54')[0] == 1
    assert get_password_strength('272726654989')[0] == 1
    assert get_password_strength('789456')[0] == 1
    assert get_password_strength('000000000')[0] == 1

    # Testing with only lowercase/uppercase
    assert get_password_strength('fjhkhjgvbsrcnvjsknkbjhsvbk')[0] == 2
    assert get_password_strength('jgfjfdkfdfj')[0] == 2

    assert get_password_strength('FJHKHJGVBSRCNVJSKNKBJHSVBK')[0] == 2
    assert get_password_strength('JGFJFDKFDFJ')[0] == 2

    # Testing with lowercase and digits
    assert get_password_strength('zlr82f6ds98')[0] >= 3
    assert get_password_strength('h2k6b7g8k9w')[0] >= 3

    # Testing with lowercase and uppercase
    assert get_password_strength('gHssDTVjTHffgf')[0] >= 3
    assert get_password_strength('hGrRlDwNmHq')[0] >= 3

    # Testing with lowercase, uppercase and digits
    assert get_password_strength('sjd5G6H3FHJ8Hh6jgs')[0] >= 4
    assert get_password_strength('h7BtR9qJ8B6')[0] >= 4
    assert get_password_strength('bvsbvrjsbS7')[0] >= 4

    # Testing with all printable
    assert get_password_strength('s8H~1wG@g8P+o')[0] >= 5
    assert get_password_strength('65><:[hg_fd=TJ')[0] >= 5

    assert get_password_strength('s8H~1wE@i8U+o{}:><')[0] >= 5
    assert get_password_strength('i8U+o{}:><86tgGFH')[0] >= 5

    assert get_password_strength('a;L8}0qJ^6Bxr#G5@zjL7')[0] >= 5
    assert get_password_strength('|?/756jfVHHBH$5wb7$%#%QHB%$CT%J')[0] >= 5


if __name__ == "__main__":
    blacklist_1kk = create_blacklist('blacklist_1kk.txt')
    english_words_list = create_blacklist('english.txt')
    while True:
        example = input("Enter a password: ")
        if example:
            if example == 'test':
                unit_tests()
                print('Test completed successfully!')
                continue
            else:
                try:
                    result = get_password_strength(example)
                    display(result)
                except AssertionError:
                    print("Your password should contain only ASCII printable characters (except whitespace).")
                    continue
        else:
            break
