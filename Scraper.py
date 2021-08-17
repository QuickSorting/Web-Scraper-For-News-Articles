import requests
from bs4 import BeautifulSoup

URL = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all(attrs={"class":"article-body"})
for article in results:
    for paragraph in article.find_all(['p', 'span']):
        print(paragraph.getText())