from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://stepik.org/media/attachments/lesson/209723/3.html')
soup = BeautifulSoup(html, 'html.parser')

rows = soup.find_all('tr')
for i in range(len(rows)):
	rows[i] = list(map(lambda x: int(x.text.strip()), rows[i].find_all('td')))
s=0
for row in rows:
	for i in row:
		s += i


print(s)