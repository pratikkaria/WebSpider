import urllib2
from bs4 import BeautifulSoup
import sys
SpiUrl = []
SpiUrl2 = []
target_url = sys.argv[1]
url = urllib2.urlopen(target_url).read()
soup = BeautifulSoup(url)
for line in soup.find_all('a'):
 newline = line.get('href')
 try:
 if newline[:4] == "http":
 if target_url in newline:
 SpiUrl.append(str(newline))
 elif newline[:1] == "/":
 combline = target_url+newline SpiUrl.append(str(combline))
 except:
 pass
 for uurl in SpiUrl:
 url = urllib2.urlopen(uurl).read()
 soup = BeautifulSoup(url)
 for line in soup.find_all('a'):
 newline = line.get('href')
 try:
 if newline[:4] == "http":
 if target_url in newline:
 SpiUrl2.append(str(newline))
 elif newline[:1] == "/":
 combline = target_url+newline
 SpiUrl2.append(str(combline))
 except:
 pass
 SpiUrl3 = set(SpiUrl2)
 for value in SpiUrl3:
 print value