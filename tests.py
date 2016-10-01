from password_strength import get_password_strength

# Testing with short passwords
assert get_password_strength('12345')[0] == 1
assert get_password_strength('1234')[0] == 1
assert get_password_strength('123')[0] == 1
assert get_password_strength('12')[0] == 1
assert get_password_strength('1')[0] == 1

# Testing with weak passwords
assert get_password_strength('987bearuhn98y8')[0] == 2
assert get_password_strength('youaremynumberoneassisstantforever')[0] == 2
# assert get_password_strength('Password1')[0] == 2
# assert get_password_strength('adminadmin')[0] == 2
# assert get_password_strength('qw3r7yu10p')[0] == 2
# assert get_password_strength('jkjghg12121999,;].;')[0] == 2
# assert get_password_strength('d;Fs28/11/56]-g54')[0] == 2

# Testing with digits
assert get_password_strength('272726654989')[0] == 3
assert get_password_strength('789456')[0] == 3
assert get_password_strength('000000000')[0] == 3

# Testing with lowercase
assert get_password_strength('fjhkhjgvbsrcnvjsknkbjhsvbk')[0] == 4
assert get_password_strength('gggshd')[0] == 4
assert get_password_strength('jgfjfdkfdfj')[0] == 4

# Testing with lowercase and digits
assert get_password_strength('f46vbt574tvi3nh4bh')[0] == 5
assert get_password_strength('h3k4u5g1k9i')[0] == 5
assert get_password_strength('ghhhhhhhhhhhhhhh8')[0] == 5

# Testing with lowercase and uppercase
assert get_password_strength('gHssDdTVjTHffgf')[0] == 6
assert get_password_strength('hGyRlOiUmHi')[0] == 6
assert get_password_strength('ghhhhhhhhhhhhhhhE')[0] == 6

# Testing with lowercase, uppercase and digits
assert get_password_strength('sjd76563HFGHJ836Hhjgs')[0] == 7
assert get_password_strength('h7Yt4E9oJ8B6')[0] == 7
assert get_password_strength('bvsbvrjsbI7')[0] == 7

# Testing with all printable
assert get_password_strength('s8H~1wG@i8U+o')[0] == 8
assert get_password_strength('9765><:[hgfdTO')[0] == 8
assert get_password_strength('ffffffffffJ8%')[0] == 8

assert get_password_strength('s8H~1wE@i8U+o{}:><')[0] == 9
assert get_password_strength('i8U+o{}:><86tgGFH')[0] == 9
assert get_password_strength('fffffffffffffJ8%')[0] == 9

assert get_password_strength('a;L80}iJ^6Bxr#G5@zjU7')[0] == 10
assert get_password_strength('|?/756jfVHHBH$5ub87$%#%UHB%$CT%Y')[0] == 10
assert get_password_strength('ffffffffffffffffJ8%')[0] == 10
