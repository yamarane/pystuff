# This program gets all headlines from google news web page !
# to make this prog work you need to install "pip install BeautifulSoup4" and requests module
# This code inspired from here http://www.practicepython.org/solution/2014/07/10/17-decode-a-web-page-solutions.html

import requests
from bs4 import BeautifulSoup

base_url = 'https://news.google.com/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

headlines = [story_heading.a.span.text for story_heading in soup.find_all(class_="esc-lead-article-title")]

print('*'*100, '\n', 'HEADLINES\n', '*'*99)
for headline in headlines:
    print(headline)
