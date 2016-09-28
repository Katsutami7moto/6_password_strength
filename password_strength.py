
def is_weak(password):
    pass


def get_password_strength(password):
    if len(password) < 6:
        print(" Mark: 1. \n Your password should be 6 or more symbols long.")
        return
    if is_weak(password):
        print(" Mark: 2. \n You are using one of common passwords.")
        return
    pass


if __name__ == '__main__':
    psswrd = input("Enter a password: ")
    get_password_strength(psswrd)
