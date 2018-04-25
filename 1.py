
# Starting with 
# https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
import requests
from bs4 import BeautifulSoup
url = "https://www.npr.org/programs/all-things-considered/"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
audioLabels = soup.find_all(class_='audio-tool-label')
n=1
for a in audioLabels: 
  if (a.text == 'Download'):
    p=a.parent
    href=p.get('href')
    href=href.split('?')[0]
    print("wget -O %d.mp3 %s" % (n, href))
    n += 1

