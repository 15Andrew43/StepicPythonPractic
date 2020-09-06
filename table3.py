from urllib.request import urlopen
from bs4 import BeautifulSoup

# from table2 import Strip

html = urlopen('https://stepik.org/media/attachments/lesson/209723/5.html')
soup = BeautifulSoup(html, 'html.parser')

print(soup)

def main(line):
	arr = []
	start = end = -1
	for ind, ch in enumerate(line):
		if start == -1 and ch.isdigit():
			start = ind
		elif start != -1 and not ch.isdigit():
			end = ind
			arr.append(int(line[start:end]))
			start = -1
			end = -1
	return arr



print(sum(main(str(soup))))