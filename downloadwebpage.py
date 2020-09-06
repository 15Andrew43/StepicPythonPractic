from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')

d = {}

arr_html = html.split('<code>')

for i in arr_html:
	if '</code>' in i:
		name = i[:i.find('</code>')]
		if name not in d:
			d[name] = 0
		d[name] += 1

res = [(cnt, name) for name, cnt in d.items()]

res.sort(reverse=True)

cnt = res[0][0]
i=0
while res[i][0] == cnt:
	print(res[i][1], end=' ')
	i += 1


