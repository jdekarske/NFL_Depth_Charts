from bs4 import BeautifulSoup
import urllib.request

position=['','Team','QB','RB','WR','TE','K']

#depth = urllib.request.urlopen('http://www.thehuddle.com/2018-nfl-depth-charts.php').read()

with open("depth.html","r") as depthchart:
    depth = depthchart.read()

depthsoup = BeautifulSoup(depth,'html5lib')

for depthtable in depthsoup.find_all('table'):
    for depthtbody in depthtable.find_all('tbody'):
        for trs in depthtbody.find_all('tr'):
            team=''
            tdcntr=0
            for tds in trs.find_all('td'):
                tdcntr=tdcntr+1
                poscntr=0
                for links in tds.find_all('a'):
                    if team =='':
                        team=links.string
                    else:	
                        if len(links) > 0 and len(links.text.lstrip()) > 0:
                            players = links.text.lstrip().rstrip().split('\n')
                            for plyr in players:
                                poscntr = poscntr + 1
                                print(team,position[tdcntr],poscntr,plyr.lstrip().rstrip())