import urllib.request

blck = 'https://raw.githubusercontent.com/danielmiessler/'
lst = 'SecLists/master/Passwords/10_million_password_list_top_1000000.txt'
blcklst = blck + lst
urllib.request.urlretrieve(url=blcklst, filename='blacklist_1kk.txt')

nglsh = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
urllib.request.urlretrieve(url=nglsh, filename='english.txt')
