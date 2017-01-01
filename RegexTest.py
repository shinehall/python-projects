import re

txt = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
regex = re.compile(r'Agent (\w)')
#rs1 = regex.search(txt)
#print regex.sub('1****', txt)
print regex.sub(r'\1****', txt)
print regex.findall(txt)


