import threading
import requests
from bs4 import BeautifulSoup

urls = [
   ' https://leetcode.com/progress/',

   ' https://takeuforward.org/graph/bridges-in-graph-using-tarjans-algorithm-of-time-in-and-low-time-g-55',

   ' https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads  =[]

for url in urls:
    thread = threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all webpages fetched")