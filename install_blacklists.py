import urllib.request

blacklist_head = 'https://raw.githubusercontent.com/danielmiessler/'
blacklist_tail = 'SecLists/master/Passwords/10_million_password_list_top_1000000.txt'
blacklist = blacklist_head + blacklist_tail
urllib.request.urlretrieve(url=blacklist, filename='blacklist_1kk.txt')

english_list = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
urllib.request.urlretrieve(url=english_list, filename='english.txt')
