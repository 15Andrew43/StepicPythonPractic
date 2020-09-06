from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html')
soup = BeautifulSoup(html, 'html.parser')

def Strip(line):
	start = end = -1
	for ind, ch in enumerate(line):
		if ch.isdigit():
			start = ind
			break
	else:
		return None
	for i in range(len(line)-1, -1, -1):
		if line[i].isdigit():
			end = i
			break
	return line[start : end+1]



rows = soup.find_all('tr')
for i in range(len(rows)):
	rows[i] = list(map(lambda x: int(Strip(x.text)), rows[i].find_all('td')))
s=0
for row in rows:
	for i in row:
		s += i


print(s)