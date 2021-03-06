import requests
import sys
from bs4 import BeautifulSoup

def check_if_URL_is_valid():
    if len(sys.argv) != 2:
        print("Please provide the URL of the website as an argument")
        sys.exit()
    if not sys.argv[1].startswith("https://www.washingtonpost.com"):
        print("This scraper works only with Washington Post articles. Please make sure that the provided URL is from the Washington Post")
        sys.exit()

def print_text_from_webpage(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(attrs={"class":"article-body"})
    for article in results:
        for paragraph in article.find_all(['p', 'span']):
            print(paragraph.getText())

check_if_URL_is_valid()
URL = sys.argv[1]
print_text_from_webpage(URL)