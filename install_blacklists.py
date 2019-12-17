import urllib.request

blacklist = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/' \
            'xato-net-10-million-passwords-1000000.txt'
urllib.request.urlretrieve(url=blacklist, filename='blacklist_1kk.txt')

english_list = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
urllib.request.urlretrieve(url=english_list, filename='english.txt')
