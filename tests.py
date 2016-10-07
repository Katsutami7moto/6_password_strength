from password_strength import get_password_strength


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

# Testing with lowercase
assert get_password_strength('fjhkhjgvbsrcnvjsknkbjhsvbk')[0] == 2
assert get_password_strength('gtnshd')[0] == 2
assert get_password_strength('jgfjfdkfdfj')[0] == 2

# Testing with lowercase and digits
assert get_password_strength('f46vbt57tvi3nh4bh')[0] >= 3
assert get_password_strength('h3k4u5g1k9i')[0] >= 3

# Testing with lowercase and uppercase
assert get_password_strength('gHssDTVjTHffgf')[0] >= 3
assert get_password_strength('hGyRlOiUmHi')[0] >= 3

# Testing with lowercase, uppercase and digits
assert get_password_strength('sjd563HFGHJ836Hhjgs')[0] >= 4
assert get_password_strength('h7Yt4E9oJ8B6')[0] >= 4
assert get_password_strength('bvsbvrjsbI7')[0] >= 4

# Testing with all printable
assert get_password_strength('s8H~1wG@i8U+o')[0] >= 5
assert get_password_strength('65><:[hg_fd=TO')[0] >= 5

assert get_password_strength('s8H~1wE@i8U+o{}:><')[0] >= 5
assert get_password_strength('i8U+o{}:><86tgGFH')[0] >= 5

assert get_password_strength('a;L80}iJ^6Bxr#G5@zjU7')[0] >= 5
assert get_password_strength('|?/756jfVHHBH$5ub7$%#%UHB%$CT%Y')[0] >= 5
