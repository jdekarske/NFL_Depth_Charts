from bs4 import BeautifulSoup
import urllib.request

depth = urllib.request.urlopen('http://www.thehuddle.com/2018-nfl-depth-charts.php').read()

depthsoup = BeautifulSoup(depth,'html5lib')

for depthtable in depthsoup.find_all('table'):
	for depthtbody in depthtable.find_all('tbody'):
		for trs in depthtbody.find_all('tr'):
			for tds in trs.find_all('td'):
				print(tds.text)