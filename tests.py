from password_strength import get_password_strength

# Testing with short passwords
assert get_password_strength('12345')[0] == 1
assert get_password_strength('1234')[0] == 1
assert get_password_strength('123')[0] == 1
assert get_password_strength('12')[0] == 1
assert get_password_strength('1')[0] == 1

# Testing with weak passwords
assert get_password_strength('987bearimiuhn98y8')[0] == 2

# Testing with digits
assert get_password_strength('272726654989')[0] == 3
assert get_password_strength('789456')[0] == 3
assert get_password_strength('000000000')[0] == 3
