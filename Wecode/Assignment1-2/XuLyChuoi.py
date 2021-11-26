import re

s = input().lower()
s = re.sub('[aoyeui]','',s)
s = list(s)
s = '.'.join(s)
print(f'.{s}')